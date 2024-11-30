from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test data for the Menu model
        self.menu_item1 = Menu.objects.create(title="Pizza", price=120.00, inventory=50)
        self.menu_item2 = Menu.objects.create(title="Burger", price=80.00, inventory=30)
        self.client = APIClient()

    def test_getall(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
