from django.test import TestCase, Client
from django.urls import reverse
from core import models


class RecipeTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.recipes = []
        for i in models.Recipe.objects.all():
            self.recipes.append(i)

    def test_list(self):
        response = self.client.get(reverse('core:recipes'))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        responses = []
        for i in self.recipes:
            response = self.client.get(reverse('core:recipe', kwargs=i.pk))
            self.assertEqual(response.status_code, 200)

    def test_create(self):
        data = {
            'name': 'recipe',
            'description': 'description',
            'count': 5
        }
        response = self.client.post(reverse('core:recipe_create'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)


class ComponentTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_list(self):
        response = self.client.get(reverse('core:components'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        data = {
            'name': 'name',
            'price': 1000,
        }
        response = self.client.post(reverse('core:component_create'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)


class ToolTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_list(self):
        response = self.client.get(reverse('core:tools'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        data = {
            'name': 'tool',
            'cost': 1000,
            'usage': 5
        }
        response = self.client.post(reverse('core:tool_create'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

