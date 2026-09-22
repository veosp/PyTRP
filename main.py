import sys

from src.py_trp.models import Category, Ingredient, Recipe, User


def find_recipes_by_ingredients(
    recipes: list[Recipe], available_ingredients: list[Ingredient]
) -> list[Recipe]:
    return [
        recipe
        for recipe in recipes
        if recipe.can_be_cooked_with(available_ingredients)
    ]


def print_recipes(recipes: list[Recipe]) -> None:
    if not recipes:
        print("Подходящих рецептов не найдено.")
        return

    print("Можно приготовить:")
    for recipe in recipes:
        print(f"- {recipe.name} ({recipe.category.name})")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    breakfast = Category("Завтраки", "Простые блюда для начала дня")

    eggs = Ingredient("Яйца")
    milk = Ingredient("Молоко")
    salt = Ingredient("Соль")
    cheese = Ingredient("Сыр")

    recipes = [
        Recipe(
            name="Омлет",
            category=breakfast,
            ingredients=[eggs, milk, salt],
            instructions="Смешать ингредиенты и обжарить на сковороде.",
        ),
        Recipe(
            name="Сырный омлет",
            category=breakfast,
            ingredients=[eggs, milk, salt, cheese],
            instructions="Смешать ингредиенты, добавить сыр и обжарить.",
        ),
    ]

    available_ingredients = [eggs, milk, salt]
    found_recipes = find_recipes_by_ingredients(recipes, available_ingredients)
    print_recipes(found_recipes)

    user = User("Анна")
    if found_recipes:
        user.add_to_favorites(found_recipes[0])
        print(f"В избранном у {user.username}: {user.favorite_recipes[0].name}")


if __name__ == "__main__":
    main()
