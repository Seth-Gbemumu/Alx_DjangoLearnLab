from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListAPIView



router = DefaultRouter()
router.register(r'Book', BookListAPIView)

urlpatterns = [

    path('api/', include(router.urls)),
]