from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("therapy/", views.therapy, name="therapy"),
    path("about/", views.about, name="about"),
    path("meditation/", views.meditation, name="meditation"),
    path("contact/", views.contact_view, name="contact"),
    path("course/", views.course, name="course"),
    path("happiness/", views.happiness, name="happiness"),
    path("approach/", views.approach_form_view, name="approach"),
    path("free-trial/", views.free_trial_view, name="free_trial"),
    path("payment/", views.payment_view, name="payment"),
    path("success/", views.success_view, name="success"),
    

]
