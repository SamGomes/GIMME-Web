from email.policy import default
import os
import uuid
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from multiselectfield import MultiSelectField

from django.core.validators import MaxValueValidator, MinValueValidator

from django import forms


ROLE = (('designer', 'designer'),
       ('professor', 'professor'),
       ('student', 'student'))


GENDER = (('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'))


class ModelAuxMethods():

    def pathAndRename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            # get filename
            if instance.pk:
                filename = '{}.{}'.format(instance.pk, ext)
            else:
                # set filename as random string
                filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
            return os.path.join(path, filename)
        return wrapper



# class Subject(models.Model):
#     subjectId = models.CharField(max_length=1020,primary_key=True)
#     description = models.TextField(max_length=1020)
#     studentIds = models.CharField(max_length=1020)



class UserProfile(models.Model):

    # included from 
    # https://stackoverflow.com/questions/15140942/django-imagefield-change-file-name-on-upload
  
    user = models.OneToOneField(User, 
        on_delete=models.CASCADE,
        primary_key=True,
        db_constraint=False)

    role = MultiSelectField(choices=ROLE, max_choices=1, max_length=9)
    
    fullName = models.CharField(max_length=1020)
    age = models.IntegerField()
    gender = MultiSelectField(choices=GENDER, max_choices=1, max_length=6)
    description = models.TextField(blank=True, max_length=3072)


    currState = models.TextField(max_length=3072)
    pastModelIncreasesDataFrame = models.TextField(max_length=3072)
    preferences = models.CharField(max_length=1020)

    
    # subjectIds = models.CharField(max_length=1020)
    grade = models.CharField(max_length=1020)


    avatar = models.ImageField(upload_to=ModelAuxMethods.pathAndRename('images/userAvatars/'), default='images/userAvatars/avatarPH.png')


    def __str__(self):
        return self.user.username




class Task(models.Model):
    taskId = models.CharField(max_length=100,primary_key=True)

    creator = models.CharField(max_length=1020)
    creationTime = models.CharField(max_length=1020)
    description = models.TextField(blank=True, max_length=3072)
    minReqAbility = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    profile = models.CharField(max_length=1020)
    
    profileWeight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    difficultyWeight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])


    initDate = models.DateField()
    finalDate = models.DateField()


    files = models.FileField(upload_to=ModelAuxMethods.pathAndRename('taskFiles/'), default='taskFiles/placeholder')


    def __str__(self):
        return self.taskId

class ServerState(models.Model):
    currAdaptationState = models.TextField(max_length=3072, default="[]")

    currSelectedUsers = models.TextField(max_length=3072, default="[]")
    currFreeUsers = models.TextField(max_length=3072, default="[]")

    currSelectedTasks = models.TextField(max_length=3072, default="[]")
    currFreeTasks = models.TextField(max_length=3072, default="[]")

    readyForNewActivity = models.CharField(max_length=1020, default="false")

    initDate = models.CharField(max_length=1020, default="[]")
    finalDate = models.CharField(max_length=1020, default="[]")
    
    
    simIsLinkShared = models.BooleanField(default=False)
    simIsTaskCreated = models.BooleanField(default=False)
    simWeekOneUsersEvaluated = models.BooleanField(default=False)
    simSimulateReaction = models.BooleanField(default=False)
    simWeekFourDoneOnce = models.BooleanField(default=False)

    simulationWeek = models.IntegerField(default=0)
    simStudentToEvaluate = models.CharField(max_length=1020)
    simUnavailableStudent = models.CharField(max_length=1020)
    simStudentX = models.CharField(max_length=1020)
    simStudentY = models.CharField(max_length=1020)
    simStudentW = models.CharField(max_length=1020)
    simStudentZ = models.CharField(max_length=1020)
