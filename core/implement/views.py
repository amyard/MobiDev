from django.shortcuts import render
from django.views.generic import View


from core.implement.models import UrlModel
from core.implement.forms import UrlForm


# def index(request):
#     return render(request, template_name = 'implement/main.html', context={'test': 'Awesome, work it!!!'})


class MainUrlView(View):
    template_name = 'implement/main.html'
    model = UrlModel
    form = UrlForm

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form,
            'urls': self.model.objects.all()
        }
        return render(self.request, self.template_name, context)