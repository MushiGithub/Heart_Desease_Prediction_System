from django.urls import path
from .views import Home, Predict

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('predict/', Predict.as_view(), name='predict'),
]
