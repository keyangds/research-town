import uuid
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class BaseProfile(BaseModel):
    pk: str = Field(default_factory=lambda: str(uuid.uuid4()))
    embed: Optional[Any] = Field(default=None)


class AgentProfile(BaseProfile):
    name: Optional[str] = Field(default=None)
    bio: Optional[str] = Field(default=None)
    collaborators: Optional[List[str]] = Field(default=[])
    institute: Optional[str] = Field(default=None)


class PaperProfile(BaseProfile):
    authors: Optional[List[str]] = Field(default=[])
    title: Optional[str] = Field(default=None)
    abstract: Optional[str] = Field(default=None)
    url: Optional[str] = Field(default=None)
    timestamp: Optional[int] = Field(default=None)
    section_contents: Optional[Dict[str, str]] = Field(default=None)
    table_captions: Optional[Dict[str, str]] = Field(default=None)
    figure_captions: Optional[Dict[str, str]] = Field(default=None)
    bibliography: Optional[Dict[str, str]] = Field(default=None)
    keywords: Optional[List[str]] = Field(default=None)
    domain: Optional[str] = Field(default=None)
    references: Optional[List[Dict[str, str]]] = Field(default=None)
    citation_count: Optional[int] = Field(default=0)
    award: Optional[str] = Field(default=None)