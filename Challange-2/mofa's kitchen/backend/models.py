from pydantic import BaseModel, Field, validator, ConfigDict
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from typing_extensions import Annotated

class PyObjectId(str):
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        return {'type': 'string'}

    @classmethod
    def validate(cls, v):
        if not isinstance(v, (str, ObjectId)):
            raise ValueError('Invalid ObjectId')
        return str(v)

class Ingredient(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )

    id: Annotated[Optional[PyObjectId], Field(alias='_id')] = None
    name: str = Field(..., min_length=2, max_length=100)
    quantity: float
    unit: str
    category: Optional[str] = None
    expiry_date: Optional[datetime] = None

    @validator('quantity')
    def quantity_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Quantity must be positive')
        return v

class Recipe(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )

    id: Annotated[Optional[PyObjectId], Field(alias='_id')] = None
    name: str
    ingredients: List[str]
    instructions: List[str]
    preparation_time: int  # minutes
    difficulty_level: str
    cuisine: Optional[str] = None
    dietary_tags: Optional[List[str]] = []

class UserProfile(BaseModel):
    username: str
    dietary_preferences: List[str]
    allergies: List[str]
    cooking_skill_level: str