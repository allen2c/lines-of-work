import json
import logging
import random
from textwrap import dedent
from typing import Optional, Union

from agents import (
    FunctionTool,
    ModelSettings,
    ModelTracing,
    OpenAIChatCompletionsModel,
    OpenAIResponsesModel,
)
from google_language_support import LanguageCodes
from openai.types.responses import ResponseFunctionToolCall

logger = logging.getLogger(__name__)


async def generate_open_queries(
    agent_instructions: str,
    k: int = 3,
    *,
    language: Optional["LanguageCodes"] = None,
    openai_model: Union["OpenAIResponsesModel", "OpenAIChatCompletionsModel"],
) -> list[str]:

    language = language or random.choice(
        [
            LanguageCodes.ENGLISH,
            LanguageCodes.CHINESE_SIMPLIFIED,
            LanguageCodes.CHINESE_TRADITIONAL,
            LanguageCodes.HINDI,
            LanguageCodes.SPANISH,
            LanguageCodes.FRENCH,
            LanguageCodes.BENGALI,
            LanguageCodes.RUSSIAN,
            LanguageCodes.PORTUGUESE,
            LanguageCodes.INDONESIAN,
            LanguageCodes.GERMAN,
            LanguageCodes.JAPANESE,
            LanguageCodes.MARATHI,
            LanguageCodes.TELUGU,
            LanguageCodes.TURKISH,
            LanguageCodes.TAMIL,
            LanguageCodes.VIETNAMESE,
            LanguageCodes.THAI,
        ]
    )

    tool: dict = {
        "type": "function",
        "function": {
            "name": "generate_user_queries_for_agent",
            "description": "Generate user queries for the agent to answer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "queries": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "What user might ask the agent.",
                        },
                        "description": "The queries to generate.",
                    },
                },
                "required": ["queries"],
            },
        },
    }

    user_content = dedent(
        f"""Generate **exactly {k}** diverse, natural, and realistic user queries that a real user in this agent's **broad domain** would commonly ask.

        Important requirements:
        - First infer the general **domain / topic / area** from the Agent Instructions (examples: weather → meteorology & daily life, recipe bot → cooking & food, fitness coach → exercise & health, etc.)
        - Questions should feel like very plausible, common questions someone might ask an assistant / app / expert / service operating in that domain
        - The questions can be **somewhat general** and are allowed to go beyond the exact scope/tools described in the Agent Instructions
        - They should still feel like realistic things people actually ask in that space

        Requirements:
        - Vary significantly in topic (within the domain), phrasing, length, and tone (casual, serious, beginner, impatient, detailed, vague, etc.)
        - Sound like authentic, everyday questions a real person might ask
        - Do NOT make the questions extremely narrow or hyper-specific to capabilities explicitly listed in the instructions — aim for broader domain-typical questions

        All queries must be written in **{language.to_instruction()}**.

        Respond ONLY by calling the tool `generate_user_queries_for_agent`.
        Do not output any additional text.
        """  # noqa: E501
    ).strip()

    model_response = await openai_model.get_response(
        system_instructions="You are a taciturn",
        input=[
            {
                "role": "system",
                "content": f"## Agent Instructions\n{agent_instructions}",
            },
            {"role": "user", "content": user_content},
        ],
        model_settings=ModelSettings(tool_choice="required"),
        tools=[
            FunctionTool(
                name=tool["function"]["name"],
                description=tool["function"]["description"],
                params_json_schema=tool["function"]["parameters"],
                on_invoke_tool=lambda ctx, args_str: None,
            )
        ],
        handoffs=[],
        tracing=ModelTracing.DISABLED,
        output_schema=None,
    )

    for response_output_item in model_response.output:
        if isinstance(response_output_item, ResponseFunctionToolCall):
            arg_data = json.loads(response_output_item.arguments)
            queries = arg_data["queries"]
            if len(queries) < k:
                logger.warning(
                    f"Only {len(queries)} queries generated, but {k} are required. "
                    f"Returning all {len(queries)} queries."
                )
            return queries[:k]

        else:
            raise ValueError(f"Unexpected response output item: {response_output_item}")

    else:
        raise ValueError("Unexpected completion — no tool call returned")
