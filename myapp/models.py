from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django_countries.fields import CountryField
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def image_institute_path(instance, filename):   
    return f'user/{instance.user.id}/institute/{filename}'

def image_bank_path(instance, filename):   
    return f'user/{instance.user.id}/bank/{filename}'


# Create your models here.


def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError(
            _('Phone number must contain only digits.'),
            params={'value': value},
        )

def validate_url(value):
    validator = URLValidator()
    if not value.startswith(('http://', 'https://')):
        value = 'http://' + value
    try:
        validator(value)
    except ValidationError as e:
        raise ValidationError(
            _('Invalid URL: %(value)s'),
            params={'value': value},
        ) from e

class InstituteProfile(models.Model):
    user = models.OneToOneField(User, related_name='institute_profile', on_delete=models.CASCADE, blank=True, null=True)
    institute_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='institute_logos/')
    target_line = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, validators=[validate_phone_number])
    website_url = models.URLField(validators=[validate_url], blank=True, null=True) # blank and Null True 
    address = models.TextField()
    country = CountryField()

    def __str__(self):
        return self.institute_name
    # Bank 

class Bank(models.Model):
    user = models.ForeignKey(User , related_name = "banks" , on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 300)
    accountNumber = models.PositiveIntegerField()
    image =  models.ImageField(upload_to = image_bank_path)
    instructions = models.TextField(null = True, blank = True)


class GradingSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institute = models.OneToOneField(InstituteProfile, related_name = 'grading_system' ,  on_delete=models.CASCADE)


    def __str__(self):
        return f'Grading System for {self.institute.name}'

class Grade(models.Model):
    gradingSystem = models.ForeignKey(GradingSystem, related_name = 'grades' , on_delete=models.CASCADE)
    grade = models.CharField(max_length = 2)
    fromPercentage = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    toPercentage = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    status = models.CharField(max_length = 4)

    def __str__(self):
        return f'{self.grade} ({self.fromPercentage}% - {self.toPercentage}%)'
    
class FailCriteria(models.Model):
    gradingSystem = models.OneToOneField(GradingSystem, related_name = 'fail_criteria' , on_delete=models.CASCADE)
    overAllPercentage = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    subjectAllPercentage = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    noSubject = models.PositiveIntegerField()

    def __str__(self):
        return f'Fail Criteria for {self.gradingSystem.institute.name}'


