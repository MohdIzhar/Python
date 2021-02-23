from datetime import time

from django.db import models

# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=100)
    floor_number = models.IntegerField(default=0)
    room_number = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.room_name}: Floor {self.floor_number} Room {self.room_number}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} at {self.start_time} on {self.date}"
