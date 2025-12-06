from django.urls import path
from .views import DashboardVIEW
app_name = 'financeiro'
urlpatterns = [
    path('', DashboardVIEW.as_view(), name='financeiro'),
]