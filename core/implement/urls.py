from django.urls import path
from core.implement.views import MainUrlView, UrlDeleteView, UrlUpdateView, FirstTagCrawler


app_name='core'

urlpatterns = [
    path('', MainUrlView.as_view(), name='base-view'),
    path('delete/<int:pk>', UrlDeleteView.as_view(), name='delete_url'),
    path('update/<int:pk>', UrlUpdateView.as_view(), name='update_url'),
    path('crawler', FirstTagCrawler.as_view(), name='crawler')
]