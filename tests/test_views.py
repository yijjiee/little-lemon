from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Chocolate", price=30, inventory=10)
        Menu.objects.create(title="Prata", price=40, inventory=200)
        
    def test_getall(self):
        icecream = Menu.objects.get(title="IceCream")
        chocolate = Menu.objects.get(title="Chocolate")
        prata = Menu.objects.get(title="Prata")
        self.assertEqual(str(icecream), "IceCream : 80.00")
        self.assertEqual(str(chocolate), "Chocolate : 30.00")
        self.assertEqual(str(prata), "Prata : 40.00")