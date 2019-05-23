from django.urls import path
from core.implement.views import MainUrlView, UrlDeleteView, UrlUpdateView


app_base='core'

urlpatterns = [
    path('', MainUrlView.as_view(), name='base-view'),
    path('delete/<int:pk>', UrlDeleteView.as_view(), name='delete_url'),
    path('update/<int:pk>', UrlUpdateView.as_view(), name='update_url'),
]