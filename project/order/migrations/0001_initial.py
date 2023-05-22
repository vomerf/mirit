# Generated by Django 3.2 on 2023-05-21 08:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('pub_date', models.DateField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_order', to=settings.AUTH_USER_MODEL)),
                ('perfomer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='perfomer_order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]