# Generated by Django 4.1.7 on 2023-02-21 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_tag_order_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
        migrations.AddField(
            model_name='products',
            name='tag',
            field=models.ManyToManyField(to='myapp.tag'),
        ),
    ]
