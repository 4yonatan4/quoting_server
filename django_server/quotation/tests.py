import json

from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from .models import HealthClassTable, RatesTable, QuotationRequest


class QuotationTest(APITestCase):
    def test_quotation_request(self):
        """
        E2E check if all the process work as expected
        """
        data = {
            "term": 10,
            "coverage": 250000,
            "age": 25,
            "height": "5 ft 1",
            "weight": 160
        }
        response = self.client.post('/api/v1/quotation/', json.dumps(data),
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = response.json()
        self.assertEqual(res['price'], 107.275)
        self.assertEqual(res['health-class'], 'Preferred')
        self.assertEqual(res['term'], 10)
        self.assertEqual(res['coverage'], 250000)


class FindRateTestCase(TestCase):

    def test_find_rate(self):
        """ Check if the function of find rate works well """
        quotation_dict = {
            "term": 10,
            "coverage": 250000,
            "age": 25,
            "height": "5 ft 1",
            "weight": 160,
            "health_class": 'Preferred Plus'
        }
        quotation_request = QuotationRequest(quotation_dict)
        self.assertEqual(0.3024, RatesTable().find_rate(quotation_request))


class FindHealthClassTestCase(TestCase):

    def test_find_health_class(self):
        """ Check if the function of find health class works well """
        quotation_dict = {
            "term": 10,
            "coverage": 250000,
            "age": 25,
            "height": "6 ft 6",
            "weight": 292,
        }
        quotation_request = QuotationRequest(quotation_dict)
        self.assertEqual('Standard Plus', HealthClassTable().find_health_class(quotation_request))
