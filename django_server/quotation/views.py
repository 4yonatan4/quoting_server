import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import QuotationRequest


@csrf_exempt
def get_bid(request):
    if request.method == 'POST':
        quotation_request = QuotationRequest(json.loads(request.body))
        quotation = quotation_request.create_quotation()
        return JsonResponse(quotation)
