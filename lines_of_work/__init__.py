import importlib
import pkgutil

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
