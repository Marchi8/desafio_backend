from django.urls import path
from . import views

# from drf_spectacular.views import (
#     SpectacularAPIView,
#     SpectacularSwaggerView,
#     SpectacularRedocView,
# )

urlpatterns = [
    path("parse/", views.ParseView.as_view()),
]
