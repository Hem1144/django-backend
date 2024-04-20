from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    pepoles = [
        {"name": "Hemlal", "age": 24},
        {"name": "Ram", "age": 40},
        {"name": "Demo", "age": 34},
        {"name": "Sandeep", "age": 31},
        {"name": "Pradeep", "age": 13},
    ]

    vegetables = ["Pumpkin", "Tomato", "Cauliflower", "Cabbage"]

    return render(
        request,
        "home/index.html",
        context={
            "peoples": pepoles,
            "page": "Django Tutorial",
            "vegetables": vegetables,
        },
    )


def about(request):
    context = {"page": "About"}
    return render(request, "home/about.html", context)


def contact(request):
    context = {"page": "Contact"}
    return render(request, "home/contact.html", context)


def success_page(request):
    return HttpResponse("<h1>This is a Success Page</h1>")
