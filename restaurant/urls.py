#define URL route for index() view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view(), name="menu-list"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name="menu-detail"),
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),
]
