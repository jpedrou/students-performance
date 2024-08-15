from api import views
from django.urls import path

urlpatterns = [path("api/makepredictions", views.make_predictions, name="makepredictions")]
