from django.urls import path
from .views import main_page, contact,show_contacts

urlpatterns = [
    path("", main_page, name="main_page"),
    path("contact/", contact, name="contact"),
    path("contacts/",show_contacts,name="show_contacts")
]