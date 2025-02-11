from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import ClientViewSet, ProjectViewSet, UserReadOnlyViewSet
# from django.views.generic import RedirectView

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'users', UserReadOnlyViewSet, basename='user')
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),    
    path('', include(router.urls)),
]