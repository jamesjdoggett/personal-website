from django.shortcuts import render


def home(request):
    courses = [
        {"name": "Web Development", "completed": False},
        {"name": "Programming Fundamentals", "completed": True},
        {"name": "Networking", "completed": True},
        {"name": "Cybersecurity", "completed": False},
        {"name": "Database Management", "completed": True},
    ]

    return render(request, "home.html", {"items": courses})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
