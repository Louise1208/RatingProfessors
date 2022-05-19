from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import settings
# Create models here.
class Teacher(models.Model):
    '''
    Teacher Table
    '''
    name = models.CharField(max_length=200)
    name_brief = models.CharField(max_length=20)
    def __str__(self):
        return self.name_brief + ", " + self.name

class Courses(models.Model):
    """
    course table
    """
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=5)
    year = models.DateField(default=None)
    semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    taught_by = models.ForeignKey('Teacher', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name + ", taught by " + str(self.taught_by) + ", semester " + str(self.semester)
class Rate(models.Model):
    """
    rate table
    """
    course = models.ForeignKey('Courses', on_delete=models.CASCADE, default=None)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)], default=5)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True)