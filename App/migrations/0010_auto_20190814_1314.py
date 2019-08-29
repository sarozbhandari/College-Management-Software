# Generated by Django 2.2 on 2019-08-14 07:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20190813_0753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionmanagement',
            name='course_code',
        ),
        migrations.RemoveField(
            model_name='sessionmanagement',
            name='course_credit',
        ),
        migrations.RemoveField(
            model_name='sessionmanagement',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sessionmanagement',
            name='session_session',
        ),
        migrations.AddField(
            model_name='sessionmanagement',
            name='end_date',
            field=models.DateField(default=datetime.date(2019, 8, 14)),
        ),
        migrations.AddField(
            model_name='sessionmanagement',
            name='start_date',
            field=models.DateField(default=datetime.date(2019, 8, 14)),
        ),
        migrations.AlterField(
            model_name='deadline',
            name='end_date',
            field=models.DateField(default=datetime.date(2019, 8, 14)),
        ),
        migrations.AlterField(
            model_name='deadline',
            name='start_date',
            field=models.DateField(default=datetime.date(2019, 8, 14)),
        ),
        migrations.AlterField(
            model_name='sessionmanagement',
            name='session_name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='date_created',
            field=models.DateField(default=datetime.date(2019, 8, 14)),
        ),
        migrations.AlterField(
            model_name='studentmanagement',
            name='enrolled_year',
            field=models.DateField(default=datetime.date(2019, 8, 14)),
        ),
        migrations.CreateModel(
            name='SessionCourseManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_session', models.CharField(max_length=200)),
                ('course_credit', models.IntegerField()),
                ('offer', models.CharField(default=False, max_length=3)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.CourseManagement')),
                ('session_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.SessionManagement')),
            ],
        ),
    ]
