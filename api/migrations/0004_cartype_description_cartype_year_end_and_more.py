# Generated by Django 5.1.1 on 2024-10-04 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_cartype_model_alter_cartype_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cartype',
            name='year_end',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='cartype',
            name='year_start',
            field=models.IntegerField(default=2000),
        ),
    ]
