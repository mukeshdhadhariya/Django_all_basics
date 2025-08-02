from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE=[
        ('ML','masala'),
        ('GR','ginger'),
        ('PL','plain')
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE)
    discription=models.TextField(default='')

    def __str__(self):
        return self.name

class ChaiReviews(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    

class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varities=models.ManyToManyField(ChaiVarity,related_name='stores')
    
    def __str__(self):
        return self.name
    

class chaiCertificate(models.Model):
    chai=models.OneToOneField(ChaiVarity,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=100)
    issue_date=models.DateTimeField(default=timezone.now)
    valid_till=models.DateTimeField()

    def __str__(self):
        return f'certificate for {self.chai.name}'
    