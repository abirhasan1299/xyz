# Generated by Django 4.2.4 on 2023-09-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_person_death'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='qr_code_name',
            field=models.CharField(default=1245, max_length=10000000),
            preserve_default=False,
        ),
    ]