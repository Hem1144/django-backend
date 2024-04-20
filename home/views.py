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

    text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum ullam impedit totam! Atque, debitis officiis amet sed veritatis voluptatibus. Voluptate, sed impedit quae suscipit magni cumque eum optio, dignissimos dicta cupiditate tenetur corrupti sequi amet dolorum earum soluta pariatur nemo aliquam nobis laboriosam explicabo, distinctio provident. A sunt voluptatem quaerat hic rem quisquam reprehenderit quod quo repellendus, veritatis, earum dignissimos voluptatum quasi eos minima provident omnis quas. Qui tempora facere suscipit asperiores earum est distinctio tenetur, quam dignissimos eum porro veniam expedita sequi voluptatem! Expedita velit, necessitatibus libero sed, fugit et molestias ipsum iusto, totam rerum maiores. Amet, provident eaque."""

    return render(
        request,
        "index.html",
        context={"peoples": pepoles, "text": text, "vegetables": vegetables},
    )


def success_page(request):

    print("*" * 10)
    return HttpResponse("<h1>This is a Success Page</h1>")
