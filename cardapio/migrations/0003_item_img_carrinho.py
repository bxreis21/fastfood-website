# Generated by Django 4.0.3 on 2022-11-22 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cardapio', '0002_combos_disponivel_item_item_disponivel_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img',
            field=models.ImageField(default=False, upload_to=''),
        ),
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itens', models.ManyToManyField(to='cardapio.item')),
                ('user_carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
