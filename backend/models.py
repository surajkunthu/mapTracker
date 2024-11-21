# import required libraries
import os
from typing import Optional, List
from pymongo import ReturnDocument
from bson import ObjectId, DatetimeMS, _get_date
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

# Taken from MongoDB documentation
PyObjectId = Annotated[str, BeforeValidator(str)] 

class PlaceModel(BaseModel):
    """
    Container for a single place
    """

    # The primary key for the PlaceModel, stored as a `str` on the instance.
    # This will be aliased to `_id` when sent to MongoDB,
    # but provided as `id` in the API requests and responses.
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    address: str = Field(...)
    neighborhood: str = Field(...)
    category: str
    comments: list[str]
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            'example': {
                'name': "Applebee's",
                'address': "9601 W Broad St, Glen Allen, VA, 23060",
                "neighborhood": "Short Pump",
                "category": ["Restuarant", "Bars-Brewery", "Fun Activities"],
                "comments": ["001"]
            }
        }
    )
