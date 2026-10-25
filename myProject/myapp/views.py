from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import InputForm

def home(request):
    return render(request, "home.html")

def students_view(request):
    students = {}

    return HttpResponse("Empty student dictionary created")

def greet_time(request):
    hour = 15
    if(hour<12):
        return HttpResponse("Good MMorning")
    elif(hour<17):
        return HttpResponse("Good Afternoon")
    else:
        return HttpResponse("Good Evening")

def weather(request):
    weather = "rainy"
    if(weather=="sunny"):
        return HttpResponse("It's too hot")
    elif(weather=="rainy"):
        return HttpResponse("Take an umbrella")
    elif(weather=="snowy"):
        return HttpResponse("Too cold")
    else:
        return HttpResponse("Weather is normal")

def menuitems(request):
    items = {
        'pizza': "Pizza costs Rs. 500",
        'burger': "Burger costs Rs. 250",
        'noodles': "Noodles costs Rs. 300",
    }
    content = '<h1>Menu Items</h1>'
    for item, description in items.items():
        content += f'<li>{item}: {description}</li>'
    return HttpResponse(content)


items = {
    'pizza': "Pizza costs Rs. 500",
    'burger': "Burger costs Rs. 250",
    'noodles': "Noodles costs Rs. 300",
}
def menu(request, item):
    if item in items:
        data = items[item]
        return HttpResponse(data)
    else:
        return HttpResponse("No Data Found")


def greet(request, name):
    return HttpResponse(f"Welcome, {name}!")

def user_profile(request, username):
    return HttpResponse(
        f'User Profile: {username}'
    )

def item_detail(request, item_id):
    return HttpResponse(
        f'Item Detail: {item_id}'
        )

def restro_detail(request, category, subcategory):
    if not subcategory:
        message = f"Showing all items in {category}"
    else:
        message = f"Showing {subcategory} in {category}"

    return HttpResponse(message)

def handler404(request, exception):
    return HttpResponse(
        "Page not found (404)", 
        status=404
    )

def home(request):
    return render(request, "home.html")

def aboutus(request):
    context = {
        "name": "SHRISTI",
        "course": "B.Tech ",
        "semester": 7,
        "marks":50
    }
    return render(request, 'about.html', context)


# ques3
def marks(request, subject, marks):
    return HttpResponse(f"{subject}: {marks}")

#ques4
def book(request, book_name):
    return HttpResponse(f"Book Name: {book_name}")


def issue(request, issue_number):
    return HttpResponse(f"Issue Number: {issue_number}")


from django.shortcuts import render
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.utils.html import escape

def simple_form(request):
    name = request.POST.get("name", "")
    csrf_token = get_token(request)
    message = f"<p>Hello, {escape(name)}!</p>" if name else ""

    return HttpResponse(f"""
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
            <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
        {message}
    """)

def stu_add(request):
    if request.method == "POST":
        print(request.POST)
        Roll = request.POST.get("roll")
        Name = request.POST.get("name")
        Course = request.POST.get("course")
        marks = request.POST.get("marks")

        data = {
            "roll": Roll,
            "name": Name,
            "course": Course,
            "marks": marks,
        }

        return render(request, "stu_form.html", data)
    return render(request, "stu_form.html")

def newform(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            return HttpResponse("Form Submitted Successfully.")
    else:
        form = InputForm()
    return render(request, "stu_form.html", {"form":form})
