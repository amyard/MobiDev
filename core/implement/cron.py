from core.implement.models import UrlModel
from datetime import date, timedelta


def delete_url_after_14_days():
    UrlModel.objects.filter(created__lt = date.today()-timedelta(days=14)).delete()