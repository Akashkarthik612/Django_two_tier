from django.http import JsonResponse

def product_list(request):
    products = [{"id": 1, "name": "Phone", "price": 500},
        {"id": 2, "name": "Laptop", "price": 1000},]
    
    return JsonResponse(products, safe = False)