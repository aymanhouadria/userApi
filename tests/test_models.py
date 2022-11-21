from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase
from users_api.models import User, Address


class TestSetUp(APITestCase):
    def setUp(self):
        self.address_1 = Address.objects.create(street="Castellana", state="Madrid", city="Madrid", country="Spain",
                                                zip="12678")
        self.address_2 = Address.objects.create(street="5th Avenue", state="New Jersey", city="New York",
                                                country="United States", zip="1783")
        self.address_3 = Address.objects.create(street="10th Avenue", state="New Jersey", city="New York",
                                                country="United States", zip="1783")

    def test_create_user(self):
        user = User.objects.create(name="Juan", email="juan@gmail.com", birthdate="2002-10-12", address=self.address_1)
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "juan@gmail.com")
        self.assertEqual(user.name, "Juan")
        self.assertEqual(user.address, self.address_1)

    def test_delete_user(self):
        user = User.objects.create(name="Jose", email="jose@gmail.com", birthdate="2001-11-11", address=self.address_1)
        pk = user.pk
        user.delete()
        self.assertFalse(User.objects.filter(pk=pk).exists())

    def test_update_user(self):
        user = User.objects.create(name="Miguel", email="migui@gmail.com", birthdate="2001-11-11",
                                   address=self.address_1)
        user.email = "miguel@yahoo.es"
        user.address = self.address_2
        user.save()

        self.assertEqual(user.email, "miguel@yahoo.es")
        self.assertEqual(user.address, self.address_2)

    def test_create_user_wrong_address(self):
        user = User.objects.create(name="Cristian", email="cristian", birthdate="2001-11-11",
                                   address=self.address_3)

        self.assertRaises(ValidationError, user.full_clean)

    def test_create_address(self):
        address = Address.objects.create(street="6th Avenue", state="New Jersey", city="New York",
                                         country="United States", zip="1783")
        self.assertIsInstance(address, Address)
        self.assertEqual(address.street, "6th Avenue")
        self.assertEqual(address.state, "New Jersey")
        self.assertEqual(address.city, "New York")
        self.assertEqual(address.country, "United States")
        self.assertEqual(address.zip, "1783")

    def test_delete_address(self):
        address = Address.objects.create(street="7th Avenue", state="New Jersey", city="New York",
                                         country="United States", zip="1783")
        pk = address.pk
        address.delete()
        self.assertFalse(Address.objects.filter(pk=pk).exists())

    def test_update_address(self):
        address = Address.objects.create(street="8th Avenue", state="New Jersey", city="New York",
                                         country="United States", zip="1783")
        address.street = "Calle la Llosa"
        address.state = "C.Valenciana"
        address.city = "Nules"
        address.save()

        self.assertEqual(address.street, "Calle la Llosa")
        self.assertEqual(address.state, "C.Valenciana")
        self.assertEqual(address.city, "Nules")

    def test_create_address_wrong_params(self):
        address = Address.objects.create(state="Paris")

        self.assertRaises(ValidationError, address.full_clean)
