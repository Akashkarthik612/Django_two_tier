from django.http import JsonResponse

def process_payment(request):
    return JsonResponse(f"message: Payment successful")