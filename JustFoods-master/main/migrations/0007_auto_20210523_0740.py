# Generated by Django 3.1.7 on 2021-05-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210522_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='category',
            field=models.CharField(choices=[('OnSite', 'OnSite'), ('OffSite', 'OffSite'), ('Direct Pickup', 'Direct Pickup')], default='OnSite', max_length=255),
        ),
    ]
