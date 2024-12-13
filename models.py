from pydantic import BaseModel, field_validator

class RecipesRequest(BaseModel):
    main_ingredient: str
    ingredients: list

    class Config:
        extra = "forbid"

    @field_validator('main_ingredient')
    def main_ingredient_not_empty(cls, value):
        if not value:
            raise ValueError('main_ingredient cannot be empty')
        return value

    @field_validator('ingredients')
    def ingredients_not_empty(cls, value):
        if not value:
            raise ValueError('ingredients cannot be empty')
        return value
