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
    occupation = models.ForeignKey(Occupation, blank=False,null=False,default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import HealthProfile

class HealthRecord(models.Model):

    SLEEP_DISORDER_CHOICES = [
        ('No', 'No'),
        ('Insomnia', 'Insomnia'),
        ('Sleep Apnea', 'Sleep Apnea'),
        ('Narcolepsy', 'Narcolepsy'),
        ('Restless Legs Syndrome (RLS)', 'Restless Legs Syndrome (RLS)'),
        ('Periodic Limb Movement Disorder (PLMD)', 'Periodic Limb Movement Disorder (PLMD)'),
        ('Parasomnias', 'Parasomnias'),
        ('Circadian Rhythm Sleep Disorders', 'Circadian Rhythm Sleep Disorders'),
        ('Hypersomnia', 'Hypersomnia'),
        ('Sleep-related movement disorders', 'Sleep-related movement disorders'),
        ('Sleep-related breathing disorders', 'Sleep-related breathing disorders'),
    ]

    BMI_LEVELS_CHOICES = [
        ('Severe Thinness', 'Severe Thinness'),
        ('Moderate Thinness', 'Moderate Thinness'),
        ('Mild Thinness', 'Mild Thinness'),
        ('Normal', 'Normal'),
        ('Overweight', 'Overweight'),
        ('Obese Class I', 'Obese Class I'),
        ('Obese Class II', 'Obese Class II'),
        ('Obese Class III', 'Obese Class III'),
    ]

    healthprofile = models.ForeignKey(HealthProfile, on_delete=models.CASCADE, related_name='sleep_records')
    height = models.FloatField(verbose_name='Height', help_text='Enter height in meters', default=0,blank=False, null=False)
    weight = models.FloatField(verbose_name='Weight', help_text='Enter weight in kilograms', default=0,blank=False, null=False)

    physical_activity = models.PositiveIntegerField(verbose_name='Physical Activity', default=0, help_text='Enter level of physical activity in minutes',blank=False, null=False)
    daily_steps = models.PositiveIntegerField(verbose_name='Daily Steps', help_text='Enter daily steps count', default=0,blank=False, null=False)

    blood_pressure = models.CharField(verbose_name='Blood Pressure', max_length=20, help_text='Enter blood pressure measurement',default='120/80 mmHg',blank=False, null=False)
    heart_rate = models.PositiveIntegerField(verbose_name='Heart Rate', help_text='Enter heart rate', default=0,blank=False, null=False)

    sleep_duration = models.FloatField(verbose_name='Sleep Duration', help_text='Enter sleep duration in hours', default=0,blank=False, null=False)

    quality_of_sleep = models.IntegerField(verbose_name='Quality of Sleep', help_text='Enter quality of sleep on a scale of 1 to 10', blank=True, null=True)
    stress_level = models.IntegerField(verbose_name='Stress Level', help_text='Enter stress level on a scale of 1 to 10', blank=True, null=True)
    bmi = models.CharField(verbose_name='BMI', max_length=50, choices=BMI_LEVELS_CHOICES, blank=True, null=True)
    sleep_disorder = models.CharField(verbose_name='Sleep Disorder', max_length=50, choices=SLEEP_DISORDER_CHOICES , blank=True, null=True)

    def save(self, *args, **kwargs):
        # BMI Calculation and saving logic
        if self.height > 0 and self.weight > 0:
            bmi_val = self.weight / (self.height ** 2)
            print(f"bmi value = {bmi_val}")
            if bmi_val < 16:
                self.bmi = 'Severe Thinness'
            elif 16 <= bmi_val < 17:
                self.bmi = 'Moderate Thinness'
            elif 17 <= bmi_val < 18.5:
                self.bmi = 'Mild Thinness'
            elif 18.5 <= bmi_val < 25:
                self.bmi = 'Normal'
            elif 25 <= bmi_val < 30:
                self.bmi = 'Overweight'
            elif 30 <= bmi_val < 35:
                self.bmi = 'Obese Class I'
            elif 35 <= bmi_val < 40:
                self.bmi = 'Obese Class II'
            else:
                self.bmi = 'Obese Class III'

        super().save(*args, **kwargs)

    


