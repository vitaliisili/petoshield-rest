"""Insurance rate calculator"""

from apps.pet.models import Pet

# Mock data for testing

# class Breed():
#     def __init__(self) -> None:
#         self.age_min = 12
#         self.age_max = 18
#         self.risk_level = 4
# class Pet():
#     def __init__(self) -> None:
#         self.name = 'Snoopy'
#         self.age = 5
#         self.gender = 'M'
#         self.species = 'dog'
#         self.breed = Breed()


def get_policy_price(pet: Pet):
    BASE_PRICE = 10 # base monthly price of the policy - 10€ per month
    
    # cat lifespan 12-18
    # dog lifespan 10-13
    
    average_life_expectancy = (pet.breed.age_min + pet.breed.age_max)/2
    
    # calculate species quotient
    if pet.species == 'cat':
        q_species = 1
    else:
        q_species = 1.1
    
    # calcalate gender quotient
    if pet.gender == 'M':
        q_gender = 1.1
    else:
        q_gender = 1.0
    
    # calculate age quotient
    if pet.age < average_life_expectancy*0.5:
        q_age = 1
    elif pet.age < average_life_expectancy*0.75:
        q_age = 1.1
    elif pet.age < average_life_expectancy*0.85:
        q_age = 1.4
    else: 
        q_age = 1.9
    
    # calculate risk quotient
    if pet.breed.risk_level < 3:
        q_risk = 0.8
    elif pet.breed.risk_level < 6:
        q_risk = 1
    elif pet.breed < 8:
        q_risk = 1.2
    else:
        q_risk = 1.4

    return f'{(BASE_PRICE * q_species * q_gender * q_age * q_risk):.2f}'


# For testing purposes

# if __name__ == "__main__":
#     pet = Pet()
    
#     print(get_policy_price(pet))
