from django.urls import path
import views

urlpatterns = [
	path('/', views.home, name="home") # For calling this application in home page
]