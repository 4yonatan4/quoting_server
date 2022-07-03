import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .models import QuotationRequest


@api_view(["POST"])
@csrf_exempt
def quotation(request):
    if request.method == 'POST':
        quotation_request = QuotationRequest(request.data)
        quotation_response = quotation_request.create_quotation()
        return JsonResponse(quotation_response)
