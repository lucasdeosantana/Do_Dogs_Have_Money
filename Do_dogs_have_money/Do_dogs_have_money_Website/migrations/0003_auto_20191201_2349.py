# Generated by Django 2.2.7 on 2019-12-02 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Do_dogs_have_money_Website', '0002_auto_20191201_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Transaction_Date',
            field=models.DateField(auto_now_add=True),
        ),
    ]