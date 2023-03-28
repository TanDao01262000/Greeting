from django.shortcuts import render
from .models import GreetLanguage

# Create your views here.
def home(request):
    lang_objs = GreetLanguage.objects.all()
    context = {
        'obj':lang_objs,
    }

    return render(request, 'multilang_greet/home.html', context)