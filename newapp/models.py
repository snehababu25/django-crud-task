from django.db import models
import datetime
class Member(models.Model):
    name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    dof=models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.name