from django.test import TestCase
from restaurant import models

class MenuItemTest(TestCase):
    def test_1(self):
        self.assertTrue(1 == 1)
        
    def test_create_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")