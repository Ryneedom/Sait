# Generated by Django 4.1.4 on 2022-12-28 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birja', '0002_rename_applicant_id_applicant_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]