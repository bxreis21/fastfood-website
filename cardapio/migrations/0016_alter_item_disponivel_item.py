# Generated by Django 4.0.3 on 2023-01-02 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0015_alter_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='disponivel_item',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
