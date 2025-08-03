from django.http import JsonResponse
cart =[]
def add_to_cart(request):
    cart.append({"id": 1, "name": "Phone", "price": 500})
    return JsonResponse(f"message: Added to cart {cart}")