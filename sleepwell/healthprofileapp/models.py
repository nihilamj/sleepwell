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

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import HealthProfile

class HealthRecord(models.Model):

    SLEEP_DISORDER_CHOICES = [
        ('NORMAL', 'NORMAL'),
        ('CIRCADIAN RHYTHM SLEEP DISORDERS', 'CIRCADIAN RHYTHM SLEEP DISORDERS'),
        ('HYPERSOMNIA DISORDERS', 'HYPERSOMNIA DISORDERS'),
        ('INSOMNIA', 'INSOMNIA'),
        ('PARASOMNIAS ', 'PARASOMNIAS '),
        ('SLEEP APNEA', 'SLEEP APNEA'),
    ]

    BMI_LEVELS_CHOICES = [
        ('SEVERE THINNESS', 'SEVERE THINNESS'),
        ('MODERATE THINNESS', 'MODERATE THINNESS'),
        ('MILD THINNESS', 'MILD THINNESS'),
        ('NORMAL', 'NORMAL'),
        ('OVER WEIGHT', 'OVER WEIGHT'),
        ('OBESE CLASS I', 'OBESE CLASS I'),
        ('OBESE CLASS II', 'OBESE CLASS II'),
        ('OBESE CLASS III', 'OBESE CLASS III'),
    ]

    BP_LEVELS_CHOICES = [
        ('NORMAL', 'NORMAL'),
        ('LOW', 'LOW'),
        ('HIGH BLOOD PRESSURE', 'HIGH BLOOD PRESSURE'),
        ('VERY HIGH BLOOD PRESSURE', 'VERY HIGH BLOOD PRESSURE'),
    ]

    healthprofile = models.ForeignKey(HealthProfile, on_delete=models.CASCADE, related_name='sleep_records')

    height = models.FloatField(verbose_name='Height', default=150,blank=False, null=False)
    weight = models.FloatField(verbose_name='Weight', default=50,blank=False, null=False)
    bmi_value = models.FloatField(verbose_name='BMI Value', blank=True, null=True)
    bmi = models.CharField(verbose_name='BMI', max_length=50, choices=BMI_LEVELS_CHOICES, blank=True, null=True)

    physical_activity = models.PositiveIntegerField(verbose_name='Physical Activity', default=1 ,blank=False, null=False)
    screen_time = models.PositiveIntegerField(verbose_name='Screen Time', default=1, blank=False, null=False)

    stress_level = models.PositiveIntegerField(verbose_name='Stress Level', default=5, blank=False, null=False)
    heart_rate = models.PositiveIntegerField(verbose_name='Heart Rate',  default=80,blank=False, null=False)

    systolic_pressure = models.PositiveIntegerField(verbose_name='Systolic Pressure', default=105, blank=False, null=False)
    systolic_pressure_bp = models.CharField(verbose_name='Systolic Pressure BP', max_length=50, choices=BP_LEVELS_CHOICES, blank=True, null=True)
    diastolic_pressure = models.PositiveIntegerField(verbose_name='Diastolic Pressure', default=70, blank=False, null=False)
    diastolic_pressure_bp = models.CharField(verbose_name='Diastolic Pressure BP', max_length=50, choices=BP_LEVELS_CHOICES, blank=True, null=True)



    sleep_duration = models.PositiveIntegerField(verbose_name='Sleep Duration',  default=300,blank=False, null=False)
    quality_of_sleep = models.PositiveIntegerField(verbose_name='Quality of Sleep', default=5,blank=False, null=True)
    
    sleep_disorder = models.CharField(verbose_name='Sleep Disorder', max_length=50, choices=SLEEP_DISORDER_CHOICES , blank=True, null=True)

    def save(self, *args, **kwargs):
        # BMI Calculation and saving logic
        if self.height > 0 and self.weight > 0:
            self.bmi_value = self.weight / (self.height ** 2)
            print(f"bmi value = {self.bmi_value}")
            if self.bmi_value < 16:
                self.bmi = 'SEVERE THINNESS'
            elif 16 <= self.bmi_value < 17:
                self.bmi = 'MODERATE THINNESS'
            elif 17 <= self.bmi_value < 18.5:
                self.bmi = 'MILD THINNESS'
            elif 18.5 <= self.bmi_value < 25:
                self.bmi = 'NORMAL'
            elif 25 <= self.bmi_value < 30:
                self.bmi = 'OVER WEIGHT'
            elif 30 <= self.bmi_value < 35:
                self.bmi = 'OBESE CLASS I'
            elif 35 <= self.bmi_value < 40:
                self.bmi = 'OBESE CLASS II'
            else:
                self.bmi = 'OBESE CLASS III'
        
        if self.systolic_pressure < 90:
            self.systolic_pressure_bp = 'LOW'
        elif 90 <= self.systolic_pressure < 120:
            self.systolic_pressure_bp = 'NORMAL'
        elif 120 <= self.systolic_pressure < 139:
            self.systolic_pressure_bp = 'HIGH BLOOD PRESSURE'
        else:
            self.systolic_pressure_bp = 'VERY HIGH BLOOD PRESSURE'

        if self.diastolic_pressure < 60:
            self.diastolic_pressure_bp = 'LOW'
        elif 60 <= self.diastolic_pressure < 80:
            self.diastolic_pressure_bp = 'NORMAL'
        elif 80 <= self.diastolic_pressure < 90:
            self.diastolic_pressure_bp = 'HIGH BLOOD PRESSURE'
        else:
            self.diastolic_pressure_bp = 'VERY HIGH BLOOD PRESSURE'

        super().save(*args, **kwargs)

    


