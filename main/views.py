import math
from django.shortcuts import render

def index(request):
    team_members = [
        {"name": "John Smith", "role": "Clinical Director / Psychologist", "img": "images/user3.avif"},
        {"name": "Brady John", "role": "Psychologist", "img": "images/filial-therapy.jpg"},
        {"name": "Sarah Lee", "role": "Therapist", "img": "images/joseph.jpg"},
        {"name": "Emily Davis", "role": "Counselor", "img": "images/pascal.jpg"},
        {"name": "Michael Brown", "role": "Therapist", "img": "images/sharon.jpg"},
        {"name": "Sophia Taylor", "role": "Psychologist", "img": "images/sebene.jpg"},
        {"name": "David Wilson", "role": "Therapist", "img": "images/user4.jpg"},
        {"name": "Emma Johnson", "role": "Counselor", "img": "images/user2.avif"},
    ]

    slides = math.ceil(len(team_members) / 4)

    

    articles = [
        {
            "title": "Therapy Isn’t Just for Crisis—Here’s Why It Matters Every Day",
            "date": "April 21 2025",
            "category": "News",
            "image": "images/art1.jpg",
        },
        {
            "title": "How Family Therapy Builds Stronger Bonds",
            "date": "April 15 2025",
            "category": "Family",
            "image": "images/art2.jpeg",
        },
        {
            "title": "Meditation for Stress Relief: A Beginner’s Guide",
            "date": "April 10 2025",
            "category": "Wellness",
            "image": "images/art3.jpg",
        },
    ]
    return render(
    request,
    "index.html",
    {
        "team_members": team_members,
        "slides": range(slides),
        "articles": articles,
    },
)


def home(request):
    return render(request, "home.html")

def therapy(request):
    return render(request, "therapy.html")

def family_therapy(request):
    return render(request, "family_therapy.html")

def about(request):
    return render(request, "about.html")

def meditation(request):
    return render(request, "meditation.html")

def course(request):
    return render(request, "course.html")

def success_view(request):
    return render(request, "success.html")



def happiness(request):
    return render(request, "happiness.html")

from django.shortcuts import render

def family_therapy(request):
    cards = [
        {
            "title": "Understanding ‘Family Of Origin‘ Work in Therapy",
            "img": "images/family1.jpg",
            "reviewer": "Rotary - LCP",
        },
        {
            "title": "How structural Family Therapy Works",
            "img": "images/family2.jpg",
            "reviewer": "Carno - MD",
        },
        {
            "title": "What to Know About Internal Family System (IFS) Therapy",
            "img": "images/family3.jpg",
            "reviewer": "Rotary - MD",
        },
        {
            "title": "What Is Filial Therapy?",
            "img": "images/family4.jpg",
            "reviewer": "Rotary - LCP",
        },
        {
            "title": "Parent - Child Interaction Therapy",
            "img": "images/family5.jpg",
            "reviewer": "Rotary - LCP",
        },
        {
            "title": "How to Mentally Prepare For Motherhood, According to Parenting Coach",
            "img": "images/family6.jpg",
            "reviewer": "Rotary - LCP",
        },
    ]
    return render(request, "family_therapy.html", {"cards": cards})


from django.shortcuts import render, redirect
from .forms import ApproachForm

def approach_form_view(request):
    if request.method == "POST":
        form = ApproachForm(request.POST)
        if form.is_valid():
            # Save or process the form
            form.save()   # only works if it's a ModelForm
            return redirect("success")
    else:
        form = ApproachForm()   # ✅ form always initialized here

    return render(request, "approach_form.html", {"form": form})

from django.shortcuts import render

def meditation_view(request):
    return render(request, "meditation.html")

from django.shortcuts import render

def free_trial_view(request):
    # Example meditation list (could come from DB later)
    meditations = [
        {
            "name": "Pascal Auclair",
            "title": "Rediscover the Familiar",
            "description": "This is the first time you’ve ever been here, now. Pascal invites you to discover the vivid and mysterious experience of this new moment.",
            "image": "images/pascal.jpg",
            "duration": "5:00"
        },
        {
            "name": "Alexis Santos",
            "title": "Natural mindful walking meditation",
            "description": "Taking a relaxed walk mindfully will soothe the nervous system, get you outside, and can refresh you mentally when you’re feeling low or off.",
            "image": "images/alexis.jpg",
            "duration": "12:00"
        },
        {
            "name": "Sharon Salzberg",
            "title": "Being with Big Emotions",
            "description": "Bring an open minded curiosity to your big emotions and get to know yourself more fully, developing resilience to deal with all the feels.",
            "image": "images/sharon.jpg",
            "duration": "9:50"
        },
        {
            "name": "Joseph Goldstein",
            "title": "Balanced Compassion",
            "description": "We're living in challenging times. Try practicing balance, letting you open to the suffering of the world without becoming overwhelmed.",
            "image": "images/joseph.jpg",
            "duration": "7:00"
        },
        {
            "name": "Sebene Selassie",
            "title": "Self-kindness for stress",
            "description": "Showing self compassion to ourselves in hard times bolsters our resilience, so we can learn from setbacks rather than getting stuck in rumination.",
            "image": "images/sebene.jpg",
            "duration": "12:09"
        },
    ]
    return render(request, "free_trial.html", {"meditations": meditations})
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect("success")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


from django.shortcuts import render, redirect
from .forms import PaymentForm

def payment_view(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            # You could save or process payment method here
            print("Selected Method:", form.cleaned_data["payment_method"])
            return redirect("success")  # go to success page
    else:
        form = PaymentForm()
    return render(request, "payment.html", {"form": form})





