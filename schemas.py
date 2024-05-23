from enum import Enum
from typing import List
from pydantic import BaseModel

class PlatformConfig(BaseModel):
    platform: str | None = "aks"
    prefix: str | None = None

class DeployPlatform(BaseModel):
    platform: str | None = "aks"
    someConfig: str | None = None

class DeployContent(BaseModel):
    content: str | None = "I don't know"
    someConfig: str | None = None


class Rule(BaseModel):
    alwaysShow: bool | None = True
    parentField: str | None = None
    parentBool: bool | None = None
    parentStrings: List[str] | None = None
    parentNumbers: List[float] | None = None

class Type(str, Enum):
    boolean = 'boolean'
    text = 'text'
    number = 'number'
    textArea = 'textArea'
    enum = 'enum'

class Field(BaseModel):
    name: str | None = None
    label: str | None = None
    type: Type
    default: str | None = None
    placeholder: str | None = None
    regex: str | None = None
    min: float | None = None
    max: float | None = None
    step: float | None = None
    enumValues: List[str] | None = None
    platformPath: str | None = None
    contentPath: str | None = None
    rule: Rule

class Group(BaseModel):
    name: str | None = None
    label: str | None = None
    rule: Rule
    fields: List[Field]
