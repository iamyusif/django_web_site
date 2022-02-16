
from django.db import models








# Create your models here.

# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=40)
    greetings_2 = models.CharField(max_length=40)
    picture = models.FileField(upload_to='picture/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.FileField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)



class Services(models.Model):
    title = models.CharField(max_length=30,verbose_name="Title Services")
    content = models.CharField(max_length=250,verbose_name="Content Services")
    cart1Title = models.CharField(max_length=25,verbose_name="Cart One Title")
    cart1Content = models.CharField(max_length=100,verbose_name="Cart One Content")
    cart2Title = models.CharField(max_length=25,verbose_name="Cart Two Title")
    cart2Content = models.CharField(max_length=100,verbose_name="Cart Two Content")
    cart3Title = models.CharField(max_length=25,verbose_name="Cart Three Title ")
    cart3Content = models.CharField(max_length=100,verbose_name="Cart Three Content")
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class Portfolio(models.Model):
    image = models.FileField(upload_to='portfolio/')
    title = models.CharField(max_length=100,verbose_name="Title")
    def __str__(self):
        return self.title



