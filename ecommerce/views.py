
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    details={
        "customer_name":"John Doe",
        "product_count":12,
    }
    return render(request, "ecommerce/index.html",details)

def about(request):
    return render(request,"ecommerce/about.html")

def contact(request):
    return render(request,"ecommerce/contact.html")

def collection(request):
    products=[
        {
            "id":1,
            "name":"Gold Ring",
            "price": 25000,
            "stock": True,
            "image":"images/goldenring.jpeg"
        },
        {
            "id": 2,
            "name":"Diamond Necklace",
            "price": 500000,
            "stock":False,
            "image":"images/DiamondNeck.jpeg"
        },
        {
            "id":3,
            "name":"Golden Bracelete",
            "price": 1000000,
            "stock":True,
            "image":"images/goldenbrace.jpeg"

        },
        {
            "id":4,
            "name":"Daimond Ring",
            "price": 2000000,
            "stock":False,
            "image":"images/diamondring.jpg"

        },
        {
            "id":5,
            "name":"Platinum Ring",
            "price": 3000000,
            "stock":True,
            "image":"images/platium.jpeg"

        },
        {
            "id":6,
            "name":"Silver Necklace",
            "price": 650000,
            "stock": False,
            "image":"images/silverneck.jpeg"

        },
    ]
    
    return render(request,"ecommerce/collection.html",{"products": products})


