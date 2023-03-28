from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Greeting(models.Model):
    greet = models.TextField()
    language = models.ManyToManyField(Language, through='GreetLanguage')

    def __str__(self):
        return self.greet
    

class GreetLanguage(models.Model):
    greet = models.ForeignKey(Greeting, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f"Greeting in {self.language} is {self.greet}"
