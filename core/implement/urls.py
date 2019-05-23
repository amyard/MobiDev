from django.urls import path
from core.implement.views import MainUrlView, UrlDeleteView, UrlUpdateView, FirstTagCrawler, UrlDetailView


app_name='core'

urlpatterns = [
    path('', MainUrlView.as_view(), name='base-view'),
    path('url_detail/<int:pk>', UrlDetailView.as_view(), name='url_detail'),
    path('delete/<int:pk>', UrlDeleteView.as_view(), name='delete_url'),
    path('update/<int:pk>', UrlUpdateView.as_view(), name='update_url'),
    path('crawler', FirstTagCrawler.as_view(), name='crawler')
]