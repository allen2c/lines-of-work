import json
import logging
from textwrap import dedent
from typing import Optional, Union

from agents import OpenAIChatCompletionsModel, OpenAIResponsesModel
from google_language_support import LanguageCodes

logger = logging.getLogger(__name__)


async def generate_open_queries(
    agent_instructions: str,
    k: int = 3,
    *,
    language: Optional["LanguageCodes"] = None,
    openai_model: Union["OpenAIResponsesModel", "OpenAIChatCompletionsModel"],
) -> list[str]:
    from lines_of_work.utils.get_random_language import get_random_language

    language = language or get_random_language()

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

    chat_completion = await openai_model._client.chat.completions.create(
        model=openai_model.model,
        messages=[
            {
                "role": "system",
                "content": f"## Agent Instructions\n{agent_instructions}",
            },
            {"role": "user", "content": user_content},
        ],
        tools=[tool],
        tool_choice="required",
    )

    if not chat_completion.choices or not chat_completion.choices[0].message.tool_calls:
        raise ValueError("Unexpected completion — no tool call returned")

    tool_call = chat_completion.choices[0].message.tool_calls[0]
    if tool_call.type != "function":
        raise ValueError("Unexpected tool call type — expected function")

    arg_data: dict = json.loads(tool_call.function.arguments)
    queries = arg_data["queries"]
    if len(queries) < k:
        logger.warning(
            f"Only {len(queries)} queries generated, but {k} are required. "
            f"Returning all {len(queries)} queries."
        )
    return queries[:k]
