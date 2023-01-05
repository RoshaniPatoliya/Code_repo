from django.db import models

class Student_info(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Course = models.CharField(max_length=100)
    College = models.CharField(max_length=500)

    def __str__(self):
        return self.Name + '  ' +self.Course +'  ' +self.College