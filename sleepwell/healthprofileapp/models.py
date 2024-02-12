from django.db import models

# Create your models here.


class Occupation(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False,unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class HealthProfile(models.Model):
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]

    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    occupations = models.ForeignKey(Occupation, blank=False,null=False,default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


