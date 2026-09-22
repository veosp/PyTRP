from dataclasses import dataclass, field

from .category import Category
from .ingredient import Ingredient


@dataclass
class Recipe:

    name: str
    category: Category
    ingredients: list[Ingredient] = field(default_factory=list)
    instructions: str = ""

    def can_be_cooked_with(self, available_ingredients: list[Ingredient]) -> bool:
        available_names = {ingredient.name.lower() for ingredient in available_ingredients}
        return all(
            ingredient.name.lower() in available_names
            for ingredient in self.ingredients
        )
