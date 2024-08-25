from django.db import models

# Create your models here.
class TaskCatagory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    catagory = models.ForeignKey(TaskCatagory, on_delete=models.CASCADE)
    timeCompleted = models.DateTimeField(null=True, blank=True)
    timeOfTask = models.DateTimeField(null=True, blank=True)

class Class(models.Model):
    name = models.CharField(max_length=100)
    timeOfClass = models.TimeField(null=True, blank=True)
    daysOfClass = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    classOfAssignment = models.ForeignKey(Class, on_delete=models.CASCADE)
    timeCompleted = models.DateTimeField(null=True, blank=True)
    timeOfAssignment = models.DateTimeField(null=True, blank=True)
    grade = models.FloatField(null=True, blank=True)

class ClassTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    classOfTask = models.ForeignKey(Class, on_delete=models.CASCADE)
    timeCompleted = models.DateTimeField(null=True, blank=True)
    timeOfClassTask = models.DateTimeField(null=True, blank=True)

