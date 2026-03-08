import json
import logging
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


async def generate_user_queries_answer_not_in_context(
    agent_instructions: str,
    knowledge_context: str,
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
        f"""Using the Knowledge Context provided above, generate **exactly {k}** user queries.

        Strict requirements:
        - The answers to these questions should **NOT** be available or should be clearly insufficient in the Knowledge Context
        - The questions must still be relevant and reasonable for this agent to receive

        All queries must be written in **{language.to_instruction()}**.

        Make them natural, diverse, and realistic. These queries will test how the agent handles cases where it lacks sufficient information (e.g. whether it honestly says “I don’t know”).

        Respond ONLY by calling the tool `generate_user_queries_for_agent`. Do not output any additional text.
        """  # noqa: E501
    )

    model_response = await openai_model.get_response(
        system_instructions=f"## Agent Instructions\n{agent_instructions}\n\n## Knowledge Context\n{knowledge_context}",  # noqa: E501
        input=[{"role": "user", "content": user_content}],
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
