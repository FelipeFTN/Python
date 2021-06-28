from django.urls import path
from hello import views

urlpatterns = [
	path("", views.index, name="index"),
    path("felipe", views.felipe, name="felipe"),
    path("brian", views.brian, name="brian"),
    path("<str:name>", views.greet, name="greet")
]