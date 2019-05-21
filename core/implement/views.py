from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator


from core.implement.models import UrlModel
from core.implement.forms import UrlForm


# def index(request):
#     return render(request, template_name = 'implement/main.html', context={'test': 'Awesome, work it!!!'})


class MainUrlView(View):
    template_name = 'implement/main.html'
    model = UrlModel
    form = UrlForm
    paginate_by = 1

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