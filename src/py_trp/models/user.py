from dataclasses import dataclass, field

from .recipe import Recipe


@dataclass
class User:

    username: str
    favorite_recipes: list[Recipe] = field(default_factory=list)

    def add_to_favorites(self, recipe: Recipe) -> None:
        if recipe not in self.favorite_recipes:
            self.favorite_recipes.append(recipe)
