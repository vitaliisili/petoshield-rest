from apps.pet.models import Pet
from config import settings


def get_policy_price(pet: Pet) -> float:
    """Calculates the policy price for a given pet.
    Args:
        pet (Pet): The pet for which the policy price is calculated.
    Returns:
        float: The calculated policy price.
    """

    average_life_expectancy = (pet.breed.age_min + pet.breed.age_max) / 2
    quote_species = 1.0 if pet.species == 'cat' else 1.1
    quote_gender = 1.0 if pet.gender == 'F' else 1.1

    if pet.age < average_life_expectancy * 0.5:
        quote_age = 1
    elif pet.age < average_life_expectancy * 0.75:
        quote_age = 1.1
    elif pet.age < average_life_expectancy * 0.85:
        quote_age = 1.3
    else:
        quote_age = 1.5

    if pet.breed.risk_level < 3:
        quote_risk = 1.1
    elif pet.breed.risk_level < 6:
        quote_risk = 1.2
    elif pet.breed.risk_level < 8:
        quote_risk = 1.3
    else:
        quote_risk = 1.4

    price = settings.POLICY_BASE_PRICE * quote_species * quote_gender * quote_age * quote_risk
    return round(price, 2)
