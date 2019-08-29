from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_save


 
# Student Management Model
class StudentManagement(models.Model):
    student_id = models.ForeignKey(User, on_delete = models.CASCADE)
    university_id = models.IntegerField(primary_key = True)
    full_name = models.CharField(max_length = 40)
    email = models.EmailField(max_length = 40, unique = True)
    enrolled_session = models.CharField(max_length = 50)
    enrolled_year = models.DateField(default = timezone.now().date())
    date_created = models.DateField(default = timezone.now().date())
    password = models.CharField(max_length=50)
    status = models.CharField(max_length = 40)

    def  __str__(self):
        return self.full_name


   

# Course Management Model  
class CourseManagement(models.Model):
    course_code = models.CharField(max_length = 10, primary_key = True)
    course_name = models.CharField(max_length = 100)
    prerequisite = models.CharField(max_length =50)
    credit = models.IntegerField()

    


class SessionManagement(models.Model):
    session_name = models.CharField(primary_key = True, max_length = 200)
    session_year = models.IntegerField()
    max_credit = models.IntegerField()
    offered = models.CharField(max_length = 3)
    start_date = models.DateField(default = timezone.now().date())
    end_date = models.DateField(default = timezone.now().date())

    class Meta:
        ordering = ('-start_date',)
    

class SessionCourseManagement(models.Model):
    session_name  =models.ForeignKey(SessionManagement, on_delete = models.CASCADE)
    session_session = models.CharField(max_length = 200)
    course_code = models.ForeignKey(CourseManagement, on_delete = models.CASCADE)
    course_credit = models.IntegerField()
    offer = models.CharField(max_length = 3, default = False)


    



class DeadLine(models.Model):
    course_code = models.ForeignKey(CourseManagement, on_delete = models.CASCADE)
    start_date = models.DateField(default = timezone.now().date())
    end_date = models.DateField(default = timezone.now().date())


class OfferedCourses(models.Model):
    course_id = models.IntegerField(primary_key = True)
    course_code = models.ForeignKey(CourseManagement, on_delete = models.CASCADE)
    offered_session = models.CharField(max_length = 100)
    


class CourseEnrollment(models.Model):
    university_id = models.ForeignKey(StudentManagement, on_delete = models.CASCADE)
    course_code = models.ForeignKey(CourseManagement, on_delete = models.CASCADE)



#Grade Management
class GradeManagement(models.Model):
    university_id=models.ForeignKey(StudentManagement,on_delete=models.CASCADE)
    course_code= models.ForeignKey(CourseManagement,on_delete=models.CASCADE)
    marks = models.FloatField(default=0)
    internal_marks = models.FloatField(default=0)
    grades = models.CharField(max_length=299)
    status = models.CharField(max_length=288)
    total_marks = models.FloatField(default=0)

    def set_grades_and_status(sender,instance,**kwargs):
        if instance.marks >= 80 and instance.marks <= 100:
            instance.status = 'Pass'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 80 and instance.total_marks <= 100:
                instance.grade = "A"

        elif instance.marks >= 75 and instance.marks <= 79:
            instance.status = 'Pass'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 75 and instance.total_marks <= 79:
                instance.grade = "A-"

        elif instance.marks >= 70 and instance.marks <= 74:
            instance.status = 'Pass'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 80 and instance.total_marks <= 100:
                instance.grade = "B+"

        elif instance.marks >= 65 and instance.marks <= 69:
            instance.status = 'Pass'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 65 and instance.total_marks <= 69:
                instance.grade = "B"

        elif instance.marks >= 60 and instance.marks <= 64:
            instance.status = 'Pass'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 60 and instance.total_marks <= 64:
                instance.grade = "B-"

        elif instance.marks >= 55 and instance.marks <= 59:
            instance.status = 'Pass'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 55 and instance.total_marks <= 59:
                instance.grade = "C+"

        elif instance.marks >= 50 and instance.marks <= 54:
            instance.status = 'Pass'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 50 and instance.total_marks <= 54:
                instance.grade = "C"

        elif instance.marks >= 40 and instance.marks <= 49:
            instance.status = 'Fail'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 40 and instance.total_marks <= 49:
                instance.grade = "C-"

        elif instance.marks >= 35 and instance.marks <= 39:
            instance.status = 'Fail'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 35 and instance.total_marks <= 39:
                instance.grade = "D+"

        elif instance.marks >= 33 and instance.marks <= 34:
            instance.status = 'Fail'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 33 and instance.total_marks <= 34:
                instance.grade = "D"

        elif instance.marks >= 31 and instance.marks <= 32:
            instance.status = 'Fail'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 31 and instance.total_marks <= 32:
                instance.grade = "D-"

        elif instance.marks >= 0 and instance.marks <= 30:
            instance.status = 'Fail'
            instance.total_marks = float(instance.marks+instance.internal_marks)
            if instance.total_marks >= 0 and instance.total_marks <= 30:
                instance.grade = "F"

        else:
            instance.grades = 'NA'
            instance.status = 'NA'
pre_save.connect(GradeManagement.set_grades_and_status,sender=GradeManagement)

