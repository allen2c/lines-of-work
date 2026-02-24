from typing import NewType

from pydantic import BaseModel

IndustryID = NewType("IndustryID", str)
SubcategoryID = NewType("SubcategoryID", str)
WorkID = NewType("WorkID", str)
KnowledgeID = NewType("KnowledgeID", str)


class Agent(BaseModel):
    name: str
    description: str
    instructions: str
    version: str = "0.0.1"


class Knowledge(BaseModel):
    title: str
    content: str
    version: str = "0.0.1"


class Subcategory(BaseModel):
    id: SubcategoryID
    name: str
    description: str


class Industry(BaseModel):
    id: IndustryID
    name: str
    description: str
    subcategories: list[Subcategory]
