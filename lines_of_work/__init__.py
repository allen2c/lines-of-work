import importlib
import logging
import pkgutil
from typing import TYPE_CHECKING, Generator, Optional, Union

from lines_of_work.types import (
    Agent,
    Industry,
    IndustryID,
    Knowledge,
    KnowledgeID,
    Subcategory,
    SubcategoryID,
    WorkID,
)
from lines_of_work.version import __version__

if TYPE_CHECKING:
    import agents
    import tiktoken
    from google_language_support import LanguageCodes
    from openai_embeddings_model import (
        AsyncOpenAIEmbeddingsModel,
    )
    from openai_embeddings_model import ModelSettings as EmbeddingsModelSettings

logger = logging.getLogger(__name__)

__all__ = [
    "__version__",
    "Agent",
    "Industry",
    "IndustryID",
    "Knowledge",
    "KnowledgeID",
    "Subcategory",
    "SubcategoryID",
    "Work",
    "WorkID",
    "list_industry_ids",
    "list_subcategory_ids",
    "list_work_ids",
]


def list_industry_ids() -> list[IndustryID]:
    try:
        import lines_of_work.industries as _pkg

        return [IndustryID(m.name) for m in pkgutil.iter_modules(_pkg.__path__)]
    except ModuleNotFoundError:
        return []


def list_subcategory_ids(industry_id: IndustryID) -> list[SubcategoryID]:
    try:
        pkg = importlib.import_module(f"lines_of_work.industries.{industry_id}")
        return [SubcategoryID(m.name) for m in pkgutil.iter_modules(pkg.__path__)]
    except ModuleNotFoundError:
        return []


def list_work_ids(
    industry_id: IndustryID, subcategory_id: SubcategoryID
) -> list[WorkID]:
    try:
        pkg = importlib.import_module(
            f"lines_of_work.industries.{industry_id}.{subcategory_id}"
        )
        return [WorkID(m.name) for m in pkgutil.iter_modules(pkg.__path__)]
    except ModuleNotFoundError:
        return []


def iter_all_works() -> Generator["Work", None, None]:
    for industry_id in list_industry_ids():
        for subcategory_id in list_subcategory_ids(industry_id):
            for work_id in list_work_ids(industry_id, subcategory_id):
                yield Work(industry_id, subcategory_id, work_id)


class Work:
    def __init__(
        self,
        industry_id: IndustryID,
        subcategory_id: SubcategoryID,
        work_id: WorkID,
    ) -> None:
        self._module_base = (
            f"lines_of_work.industries.{industry_id}.{subcategory_id}.{work_id}"
        )
        agent_mod = importlib.import_module(f"{self._module_base}.agent")
        self.agent = Agent(
            name=agent_mod.name,
            description=agent_mod.description,
            instructions=agent_mod.instructions,
            language=getattr(agent_mod, "language", "en"),
            version=getattr(agent_mod, "version", "0.0.1"),
        )
        self.industry_id = industry_id
        self.subcategory_id = subcategory_id
        self.work_id = work_id

    def list_knowledge_ids(self) -> list[KnowledgeID]:
        try:
            knowledge_pkg = importlib.import_module(f"{self._module_base}.knowledge")
            return [
                KnowledgeID(m.name)
                for m in pkgutil.iter_modules(knowledge_pkg.__path__)
            ]
        except ModuleNotFoundError:
            return []

    def get_knowledge(self, knowledge_id: KnowledgeID) -> Knowledge:
        mod = importlib.import_module(f"{self._module_base}.knowledge.{knowledge_id}")
        return Knowledge(
            title=mod.title,
            content=mod.content,
            version=getattr(mod, "version", "0.0.1"),
        )

    def iter_all_knowledge(self) -> Generator[Knowledge, None, None]:
        for knowledge_id in self.list_knowledge_ids():
            yield self.get_knowledge(knowledge_id)

    def sample_knowledge_context(
        self,
        *,
        max_tokens: int = 4096,
        encoding: Optional["tiktoken.Encoding"] = None,
        seed: Optional[int] = None,
    ) -> str:
        import random

        from .utils.truncate_str import truncate_str

        random = random if seed is None else random.Random(seed)

        all_knowledge = list(self.iter_all_knowledge())
        random.shuffle(all_knowledge)

        return truncate_str(
            "\n\n".join(
                [f"### {k.title}\n\n{k.content}" for k in all_knowledge]
            ).strip(),
            max_tokens=max_tokens,
            encoding=encoding,
        )

    async def generate_open_queries(
        self,
        k: int = 3,
        *,
        language: Optional["LanguageCodes"] = None,
        openai_model: Union[
            "agents.OpenAIResponsesModel", "agents.OpenAIChatCompletionsModel"
        ],
    ) -> list[str]:
        from .utils.generate_agent_open_queries import (
            generate_open_queries,
        )

        return await generate_open_queries(
            agent_instructions=self.agent.instructions,
            k=k,
            language=language,
            openai_model=openai_model,
        )

    async def generate_user_queries_answer_in_context(
        self,
        k: int = 3,
        knowledge_context: Optional[str] = None,
        *,
        max_tokens: int = 4096,
        encoding: Optional["tiktoken.Encoding"] = None,
        language: Optional["LanguageCodes"] = None,
        openai_model: Union[
            "agents.OpenAIResponsesModel", "agents.OpenAIChatCompletionsModel"
        ],
        seed: Optional[int] = None,
    ) -> list[str]:
        from .utils.generate_user_queries_answer_in_context import (
            generate_user_queries_answer_in_context,
        )

        knowledge_context = knowledge_context or self.sample_knowledge_context(
            max_tokens=max_tokens,
            encoding=encoding,
            seed=seed,
        )

        return await generate_user_queries_answer_in_context(
            agent_instructions=self.agent.instructions,
            knowledge_context=knowledge_context,
            k=k,
            language=language,
            openai_model=openai_model,
        )

    async def generate_user_queries_answer_not_in_context(
        self,
        k: int = 3,
        knowledge_context: Optional[str] = None,
        *,
        max_tokens: int = 4096,
        encoding: Optional["tiktoken.Encoding"] = None,
        language: Optional["LanguageCodes"] = None,
        openai_model: Union[
            "agents.OpenAIResponsesModel", "agents.OpenAIChatCompletionsModel"
        ],
        seed: Optional[int] = None,
    ) -> list[str]:
        from .utils.generate_user_queries_answer_not_in_context import (
            generate_user_queries_answer_not_in_context,
        )

        knowledge_context = knowledge_context or self.sample_knowledge_context(
            max_tokens=max_tokens,
            encoding=encoding,
            seed=seed,
        )

        return await generate_user_queries_answer_not_in_context(
            agent_instructions=self.agent.instructions,
            knowledge_context=knowledge_context,
            k=k,
            language=language,
            openai_model=openai_model,
        )

    async def retrieve_knowledge(
        self,
        query: str,
        *,
        top_k: int = 3,
        openai_embeddings_model: "AsyncOpenAIEmbeddingsModel",
        model_settings: "EmbeddingsModelSettings",
    ) -> list["Knowledge"]:
        if not query:
            raise ValueError("Query is required")

        knowledge_documents: list[Knowledge] = list(self.iter_all_knowledge())

        if not knowledge_documents:
            raise ValueError(f"No knowledge documents found in work {self.agent.name}")

        similarity_res = await openai_embeddings_model.get_similarity(
            query=query,
            documents=[
                f"{k.title}\n\n{k.content}".strip() for k in knowledge_documents
            ],
            model_settings=model_settings,
        )

        ranked_knowledge_documents = [
            knowledge_documents[r.index] for r in similarity_res.results
        ]
        ranked_knowledge_documents = ranked_knowledge_documents[:top_k]

        return ranked_knowledge_documents
