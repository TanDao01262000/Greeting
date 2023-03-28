from django.contrib import admin
from .models import Language, Greeting, GreetLanguage
# Register your models here.
admin.site.register(Language)
admin.site.register(Greeting)
admin.site.register(GreetLanguage)
