# Generated by Django 2.2 on 2019-08-11 02:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20190809_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemanagement',
            name='course_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='deadline',
            name='end_date',
            field=models.DateField(default=datetime.date(2019, 8, 11)),
        ),
        migrations.AlterField(
            model_name='deadline',
            name='start_date',
            field=models.DateField(default=datetime.date(2019, 8, 11)),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='date_created',
            field=models.DateField(default=datetime.date(2019, 8, 11)),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='enrolled_year',
            field=models.DateField(default=datetime.date(2019, 8, 11)),
        ),
        migrations.AlterUniqueTogether(
            name='coursemanagement',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='SessionManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=200)),
                ('session_year', models.IntegerField()),
                ('session_session', models.CharField(max_length=100)),
                ('session_credit', models.IntegerField()),
                ('offered', models.CharField(max_length=3)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.CourseManagement')),
            ],
        ),
        migrations.CreateModel(
            name='OfferedCourses',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('offered_session', models.CharField(max_length=100)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.CourseManagement')),
            ],
        ),
        migrations.RemoveField(
            model_name='coursemanagement',
            name='session',
        ),
        migrations.RemoveField(
            model_name='coursemanagement',
            name='year',
        ),
    ]
