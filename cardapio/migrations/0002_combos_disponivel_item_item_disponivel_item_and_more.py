# Generated by Django 4.0.3 on 2022-11-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='combos',
            name='disponivel_item',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='disponivel_item',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='combos',
            name='itens_combo',
        ),
        migrations.AddField(
            model_name='combos',
            name='itens_combo',
            field=models.ManyToManyField(to='cardapio.item'),
        ),
    ]
