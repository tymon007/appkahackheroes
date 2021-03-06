# Generated by Django 2.2.6 on 2019-10-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your name', max_length=200)),
                ('email', models.EmailField(help_text='Enter your email', max_length=200)),
                ('password', models.CharField(help_text='Enter your password', max_length=500)),
                ('HowManyPepopleInHome', models.CharField(help_text='Enter how many people are in your home', max_length=200)),
            ],
        ),
    ]
