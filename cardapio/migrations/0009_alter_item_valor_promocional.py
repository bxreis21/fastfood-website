# Generated by Django 4.0.3 on 2022-11-27 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0008_alter_item_preco_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='valor_promocional',
            field=models.FloatField(),
        ),
    ]
