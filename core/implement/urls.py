from django.urls import path
from core.implement.views import MainUrlView


app_base='core'

urlpatterns = [
    path('', MainUrlView.as_view(), name='base-view'),
]