# Generated by Django 2.2 on 2021-06-30 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lrapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='poster',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_quote', to='lrapp.User'),
            preserve_default=False,
        ),
    ]
