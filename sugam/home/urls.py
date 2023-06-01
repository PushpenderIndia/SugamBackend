from django.urls import path
from .views import upload, follow_up, comikify

urlpatterns = [
    # Other URL patterns
    path('upload', upload, name='upload'),
    path("follow_up", follow_up, name="follow_up"),
    path("comikify", comikify, name="comikify")
]