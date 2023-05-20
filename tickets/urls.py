from django.urls import path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register("user", views.UserViewSet, basename="user")
router.register("ticket", views.TicketViewSet, basename="ticket")
router.register("category", views.CategoryViewSet, basename="category")

urlpatterns = router.urls