# Generated by Django 4.2.5 on 2023-11-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0008_remove_cv_describtion_remove_cv_education_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='skils',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('experienc', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
