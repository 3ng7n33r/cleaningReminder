from django.db import models


class Tenant(models.Model):
    first_name = models.CharField(max_length=30)
    room_number = models.CharField(max_length=30, blank=True)
    high_tenant = models.BooleanField()

    def __str__(self):
        return self.first_name

class Task(models.Model):
    task_name = models.CharField(max_length=30)
    people_needed = models.DecimalField(decimal_places=0, max_digits=1)
    for_ground_tenant = models.BooleanField()

    def __str__(self):
        return self.task_name
