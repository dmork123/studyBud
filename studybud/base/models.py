from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # one room can have one topic but you can have multtiple topics in different rooms
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = models
    updated = models.DateTimeField(auto_now=True) # takes a snapshot everytime there is an update
    created = models.DateTimeField(auto_now_add=True) # only takes a snapshot when we create this instance
    
    class Meta:
        ordering = ['-updated', 'created']
        
    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # establishes the relationship of a one to many, one room -> many comments
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # takes a snapshot everytime
    created = models.DateTimeField(auto_now=True) # only takes a snapshot when we create this

    def __str__(self):
        return self.body[0:50] # want the first 50 characters