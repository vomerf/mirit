# Generated by Django 3.2 on 2023-05-21 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(default=1, max_length=50, verbose_name='Middle name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('CUSTOMER', 'customer'), ('PERFOMER', 'perfomer')], max_length=8, verbose_name='User status'),
        ),
    ]