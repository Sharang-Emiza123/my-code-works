from django.db import models

class pground(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

    
class cities(models.Model):
    city_id = models.IntegerField(default=1)
    name = models.CharField(max_length=50)
    description = models.TextField()
    famous_for = models.CharField(max_length=255)

    def __str__(self):
        return self.name