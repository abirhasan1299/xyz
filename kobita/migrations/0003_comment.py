# Generated by Django 4.2.4 on 2023-09-07 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobita', '0002_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500)),
                ('fullname', models.CharField(max_length=500)),
                ('cmt', models.TextField(max_length=5000)),
                ('date_time', models.DateTimeField()),
                ('poem_unique_id', models.IntegerField()),
            ],
        ),
    ]