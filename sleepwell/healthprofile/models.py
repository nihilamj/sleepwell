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
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHERS','OTHERS'),
    ]

    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    occupation = models.ForeignKey(Occupation, blank=False,null=False,default=1,on_delete=models.CASCADE)
    is_active  = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)