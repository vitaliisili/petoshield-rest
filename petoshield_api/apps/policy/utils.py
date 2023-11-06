"""Insurance rate calculator"""

from apps.pet.models import Pet

def get_policy_price(pet: Pet):
    BASE_PRICE = 10 # base monthly price of the policy
    
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
    elif:
        q_risk = 1.4

    return BASE_PRICE * q_species * q_gender * q_age * q_risk