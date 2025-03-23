from django.db import models


class FundamentalRights(models.Model):

    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)

    img1 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex1 = models.CharField(max_length=500,  null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex2 = models.CharField(max_length=500 ,  null=True, blank=True)




    def __str__(self):
        return self.Title

class CivilRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)
    img1 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex1 = models.CharField(max_length=500 ,  null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex2 = models.CharField(max_length=500 ,  null=True, blank=True)


    def __str__(self):
        return self.Title

class EnvironmentalRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)
    img1 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex1 = models.CharField(max_length=500,  null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex2 = models.CharField(max_length=500,  null=True, blank=True)


    def __str__(self):
        return self.Title

class EconomicRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)
    img1 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex1 = models.CharField(max_length=500,  null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex2 = models.CharField(max_length=500,  null=True, blank=True)


    def __str__(self):
        return self.Title

class humanRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)
    img1 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex1 = models.CharField(max_length=500,  null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex2 = models.CharField(max_length=500,  null=True, blank=True)


    def __str__(self):
        return self.Title

class LegalRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)
    img1 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex1 = models.CharField(max_length=500,  null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex2 = models.CharField(max_length=500,  null=True, blank=True)


    def __str__(self):
        return self.Title

class politicalRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)
    img1 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex1 = models.CharField(max_length=500, null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex2 = models.CharField(max_length=500,  null=True, blank=True)


    def __str__(self):
        return self.Title
  
class DirectivePrincipleofOurStatePolicy(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=50002)
    img1 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex1 = models.CharField(max_length=500,  null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex2 = models.CharField(max_length=500,  null=True, blank=True)


    def __str__(self):
        return self.Title
    
class CriminalLaw(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=50002)
    img1 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex1 = models.CharField(max_length=500,  null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex2 = models.CharField(max_length=500,  null=True, blank=True)


    def __str__(self):
        return self.Title

class PersonalLaw(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=50002)
    img1 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex1 = models.CharField(max_length=500,  null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex2 = models.CharField(max_length=500,  null=True, blank=True)


    def __str__(self):
        return self.Title
    

class UnionTerritory(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=50002)
    img1 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex1 = models.CharField(max_length=500,  null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default='images/default_image.png')
    ex2 = models.CharField(max_length=500,  null=True, blank=True)


    def __str__(self):
        return self.Title
  
  
from django.contrib.auth.models import User

class Lawyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)

    img = models.ImageField(upload_to='lawyerpic/',default='images/default_image.png')
    name= models.CharField(max_length = 50)
    phone = models.CharField(max_length=10, null=True, blank=True)
    doc = models.ImageField(upload_to='lawyerdoc/',default='images/default_image.png')
    specialization = models.CharField(max_length=200)
    bio = models.TextField()
    location = models.CharField(max_length=100,default="Unknown")

    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
    


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Reply(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='replies')
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'replay by{self.lawyer.name}'
    
