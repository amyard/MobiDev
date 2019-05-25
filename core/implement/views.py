from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from core.implement.models import UrlModel
from core.implement.forms import UrlForm, UrlUpdateForm
from core.common.utils import crawling

from bootstrap_modal_forms.generic import BSModalUpdateView, BSModalDeleteView


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




class UrlDetailView(DetailView):
    model = UrlModel
    template_name='implement/url_detail.html'
    context_object_name = 'url'

    def get_context_data(self, *args, **kwargs):
        context = super(UrlDetailView, self).get_context_data(*args, **kwargs)
        context['domain'] = '/'.join(self.get_object().full_url.split('/')[:3])+'/'
        return context


class UrlDeleteView(BSModalDeleteView):
    model = UrlModel
    template_name = 'implement/url_delete.html'
    success_message = 'Success: URL was deleted.'

    def get_success_url(self, **kwargs):
        if 'url_detail' in self.request.META.get("HTTP_REFERER"):
            return reverse('core:base-view')
        return self.request.META.get('HTTP_REFERER')



class UrlUpdateView(BSModalUpdateView):
    model = UrlModel
    template_name = 'implement/url_update.html'
    form_class = UrlUpdateForm
    success_message = 'Success: URL was updated.'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(UrlUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['pk'] = self.kwargs['pk']
        return kwargs

    def get_success_url(self, **kwargs):
        return self.request.META.get('HTTP_REFERER')


class FirstTagCrawler(View):
    def get(self, request, *args, **kwargs):
        url = self.request.GET.get('url')
        UrlModel.objects.filter(full_url=url).update(text=crawling(url))
        messages.add_message(self.request, messages.SUCCESS, f'Success: You have got a text from first tag from {url}')
        data = {}
        return JsonResponse(data)


class ClicksCountView(View):
    def get(self, request, *args, **kwargs):
        url_pk = self.request.GET.get('ids')
        click_number = int(self.request.GET.get('click_number'))
        UrlModel.objects.filter(pk=url_pk).update(clicks=click_number+1)
        data = { 'number':click_number+1 }
        return JsonResponse(data)