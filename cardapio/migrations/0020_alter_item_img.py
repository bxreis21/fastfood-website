# Generated by Django 4.0.3 on 2023-01-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0019_alter_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(default='templates/media/default.jpg', upload_to='templates/media'),
        ),
    ]
