# Generated by Django 4.1.7 on 2023-03-26 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greet', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GreetLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multilang_greet.greeting')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multilang_greet.language')),
            ],
        ),
        migrations.AddField(
            model_name='greeting',
            name='language',
            field=models.ManyToManyField(through='multilang_greet.GreetLanguage', to='multilang_greet.language'),
        ),
    ]
