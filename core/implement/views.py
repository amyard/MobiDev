from django.shortcuts import render
from django.views.generic import View, ListView
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect

from core.implement.models import UrlModel
from core.implement.forms import UrlForm


class MainUrlView(View):
    template_name = 'implement/main.html'
    model = UrlModel
    form = UrlForm
    paginate_by = 5
    message_send = 'Success: URL was created.'

    def get(self, request, *args, **kwargs):

        # PAGINATION
        p = Paginator(self.model.objects.all(), self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        urls = p.get_page(page_number)

        context = {
            'form': self.form,
            'urls': urls
        }
        return render(self.request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = self.form(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(self.request, self.message_send)
            return HttpResponseRedirect('/')

        # отображает страницу, где находится данный атрибут
        p = Paginator(self.model.objects.all(), self.paginate_by)
        if '?page=' in self.request.META.get('HTTP_REFERER'):
            num = self.request.META.get('HTTP_REFERER').split('?page=')[-1]
        else:
            num = 1
        page_number = request.GET.get('page', num)
        urls = p.get_page(page_number)

        context = {
            'form':self.form(request.POST or None),
            'urls': urls,

        }
        return render(self.request, self.template_name, context)





