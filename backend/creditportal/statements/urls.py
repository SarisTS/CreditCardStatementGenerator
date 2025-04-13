from django.urls import path
from .views import generate_statement

urlpatterns = [
    path('generate-statement/', generate_statement),
]
