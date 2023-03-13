from django.test import TestCase

from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Chocokate", price=90, inventory=200)

    def test_getall(self):
        self.setup()
        menus = Menu.objects.all()
        menus_ser = MenuSerializer(menus, many=True)
        self.assertEqual(len(menus_ser.data), 2)
