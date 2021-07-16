# Generated by Django 2.2 on 2021-07-01 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lrapp', '0002_quote_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='quote',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]