import pytest
from apps.pet.models import Pet, Breed
from apps.policy.utils import get_policy_price


@pytest.fixture
def mock_breed(db):
    breed = Breed.objects.create(
        name='German Shepherd',
        age_min=1,
        age_max=8,
        risk_level=1,
        species='dog'
    )
    assert breed.name == 'German Shepherd'
    return breed


@pytest.fixture
def mock_pet(mock_breed, simple_user):
    custom_mock_pet = Pet.objects.create(
        name='Lenore',
        age=5,
        gender='M',
        species='dog',
        breed=mock_breed,
        user=simple_user)
    assert custom_mock_pet.name == 'Lenore'
    return custom_mock_pet


class TestPolicyUtils:
    def test_get_policy_price(self, mock_pet):
        price = get_policy_price(mock_pet)
        assert price == 19.97

    def test_get_policy_price_with_cat(self, mock_pet):
        mock_pet.species = 'cat'
        price = get_policy_price(mock_pet)
        assert price == 18.15

    def test_get_policy_price_with_female(self, mock_pet):
        mock_pet.gender = 'F'
        price = get_policy_price(mock_pet)
        assert price == 18.15

    def test_get_policy_price_with_young_mock_pet(self, mock_pet):
        mock_pet.age = 1
        price = get_policy_price(mock_pet)
        assert price == 13.31

    def test_get_policy_price_with_old_mock_pet(self, mock_pet):
        mock_pet.age = 8
        price = get_policy_price(mock_pet)
        assert price == 19.97

    def test_get_policy_price_with_low_risk_breed(self, mock_pet):
        mock_pet.breed.risk_level = 1
        price = get_policy_price(mock_pet)
        assert price == 19.97

    def test_get_policy_price_with_middle_risk_breed(self, mock_pet):
        mock_pet.breed.risk_level = 5
        price = get_policy_price(mock_pet)
        assert price == 21.78

    def test_get_policy_price_with_high_risk_breed(self, mock_pet):
        mock_pet.breed.risk_level = 9
        price = get_policy_price(mock_pet)
        assert price == 25.41


class TestPolicyUnitTest:
    def test_policy_string_representation(self, policy):
        assert str(policy) == policy.policy_number


class TestInsuranceCaseUnitTest:
    def test_insurance_case_string_representation(self, insurance_case):
        assert str(insurance_case) == f'{insurance_case.claim_date}-{insurance_case.status}'


class TestIncomingInvoiceUnitTest:
    def test_incoming_invoice_string_representation(self, incoming_invoice):
        assert str(incoming_invoice) == str(incoming_invoice.amount)


class TestServiceProviderUnitTest:
    def test_service_provider_string_representation(self, service_provider):
        assert str(service_provider) == service_provider.company_name
