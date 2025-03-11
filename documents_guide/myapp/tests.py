from django.test import TestCase
from .models import Process, Institution, District, City, CustomUser

class ModelTests(TestCase):
    def setUp(self):
        # Test verileri oluştur
        self.city = City.objects.create(name="Test City")
        self.district = District.objects.create(name="Test District", city=self.city)
        self.institution = Institution.objects.create(
            name="Test Institution",
            address="Test Address",
            phone="1234567890",
            email="test@example.com",
            website="https://example.com",
            city=self.city,
            district=self.district,
        )
        self.process = Process.objects.create(
            name="Test Process",
            description="Test Description",
            steps="Test Steps",
            city=self.city,
            district=self.district,
        )
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword123",
            city=self.city,
            district=self.district,
        )

    def test_city_creation(self):
        self.assertEqual(self.city.name, "Test City")

    def test_district_creation(self):
        self.assertEqual(self.district.name, "Test District")
        self.assertEqual(self.district.city.name, "Test City")

    def test_institution_creation(self):
        self.assertEqual(self.institution.name, "Test Institution")
        self.assertEqual(self.institution.city.name, "Test City")
        self.assertEqual(self.institution.district.name, "Test District")

    def test_process_creation(self):
        self.assertEqual(self.process.name, "Test Process")
        self.assertEqual(self.process.city.name, "Test City")
        self.assertEqual(self.process.district.name, "Test District")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.city.name, "Test City")
        self.assertEqual(self.user.district.name, "Test District")