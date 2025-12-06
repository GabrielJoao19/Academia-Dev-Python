from django.urls import path
from .views import DashboardVIEW

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardVIEW.as_view(), name='dashboard'),
]