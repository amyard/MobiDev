from django.shortcuts import render



def index(request):
    return render(request, template_name = 'implement/main.html', context={'test': 'Awesome, work it!!!s'})