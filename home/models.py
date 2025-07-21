from django.db import models

from accounts.models import Student

# Create your models here.

class DareExchange(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    title = models.CharField(max_length = 20)

    deadline = models.DateField(blank=True, null=True)

    dare_image = models.ImageField(upload_to = "dare_images/", blank = True, null = True)

    is_edited = models.BooleanField(default = False)

    dare = models.TextField()

    
# ================================================================




