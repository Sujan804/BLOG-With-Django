from django.db import models 

class HomeInfo(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    email = models.EmailField()
    fblink = models.CharField(max_length=50)
    igling=  models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    description = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.name
