# Generated by Django 3.2.7 on 2021-09-29 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=10)),
                ('studentId', models.IntegerField()),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_register.year')),
            ],
        ),
    ]
