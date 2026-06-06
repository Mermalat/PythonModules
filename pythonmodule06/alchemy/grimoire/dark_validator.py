from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    normalized_ingredients = ingredients.casefold()
    allowed_ingredients = dark_spell_allowed_ingredients()
    is_valid = any(
        ingredient in normalized_ingredients
        for ingredient in allowed_ingredients
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
