import json
import logging
from textwrap import dedent
from typing import Optional, Union

from agents import OpenAIChatCompletionsModel, OpenAIResponsesModel
from google_language_support import LanguageCodes

logger = logging.getLogger(__name__)


async def generate_user_queries_answer_in_context(
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
        f"""Using ONLY the Knowledge Context provided above, generate **exactly {k}** user queries.

        Strict requirements:
        - The complete answer to each question MUST be directly findable and fully answerable from the Knowledge Context
        - Do not create questions that require any information outside the given context

        All queries must be written in **{language.to_instruction()}**.

        Make the questions natural, varied, and realistic. These will be used to test whether the agent can correctly retrieve and use the provided knowledge.

        Respond ONLY by calling the tool `generate_user_queries_for_agent`. Do not output any additional text.
        """  # noqa: E501
    )

    chat_completion = await openai_model._client.chat.completions.create(
        model=openai_model.model,
        messages=[
            {
                "role": "system",
                "content": f"## Agent Instructions\n{agent_instructions}\n\n## Knowledge Context\n{knowledge_context}",  # noqa: E501
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
