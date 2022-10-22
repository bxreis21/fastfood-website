# Generated by Django 4.0.3 on 2022-10-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=30)),
                ('telefone', models.IntegerField(max_length=15)),
                ('admin', models.BooleanField()),
            ],
        ),
    ]
