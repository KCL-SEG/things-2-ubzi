from django import forms
from django.test import TestCase
from .forms import ThingForm
from .models import Thing

class ThingFormTestCase(TestCase):

    def setUp(self):
        self.form_input = {
            'name': 'box',
            'description': 'a box',
            'quantity': 2,
        }

    def test_valid_sign_up_form(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_uses_model_validation(self):
        self.form_input['quantity'] = -3
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
