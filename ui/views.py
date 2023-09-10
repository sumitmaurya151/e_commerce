from django.shortcuts import render
from ui.models import Product

def index_view(request):

    all_products = Product.objects.all()

    products = []
    for product in all_products:
        prod = {}
        discount = product.product_price - ((product.product_price * product.product_discount) / 100)
        prod["discount_price"] = discount
        prod["discount"] = product.product_discount
        prod["title"] = product.product_title
        prod["price"] = product.product_price
        prod["url"] = product.product_slug
        prod["img"] = product.product_pic
        products.append(prod)

    # Your view logic goes here
    context = {'products': products, "profile":""}
    return render(request, 'index.html', context= context)
