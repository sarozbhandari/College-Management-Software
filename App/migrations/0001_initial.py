# Generated by Django 2.2 on 2019-08-06 03:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseManagement',
            fields=[
                ('course_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('prerequisite', models.CharField(max_length=50)),
                ('credit', models.IntegerField()),
                ('session', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StudentManagement',
            fields=[
                ('university_id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('enrolled_session', models.CharField(max_length=50)),
                ('enrolled_year', models.DateField(default=datetime.date(2019, 8, 6))),
                ('date_created', models.DateField(default=datetime.date(2019, 8, 6))),
                ('password', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=40)),
                ('student_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GradeManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('grades', models.CharField(max_length=1)),
                ('status', models.CharField(max_length=40)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.CourseManagement')),
                ('university_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.StudentManagement')),
            ],
        ),
        migrations.CreateModel(
            name='DeadLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date(2019, 8, 6))),
                ('end_date', models.DateField(default=datetime.date(2019, 8, 6))),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.CourseManagement')),
            ],
        ),
    ]
