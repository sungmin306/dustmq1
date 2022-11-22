# Generated by Django 3.2 on 2022-11-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('day', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('context', models.TextField(max_length=500)),
                ('pet_walk', models.CharField(choices=[('o', '1'), ('x', '0')], max_length=1)),
                ('pet_walk_num', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
