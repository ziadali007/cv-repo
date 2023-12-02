from django.db import models

# Create your models here.



class skils(models.Model):
   
    id = models.AutoField(primary_key=True)
    experienc=models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.title




class jop(models.Model):
    id = models.AutoField(primary_key=True)
    salay= models.CharField(max_length=20,null=True)
    describtion=models.CharField(max_length=20,null=True)
    title=models.CharField(max_length=30,null=True)
    location=models.CharField(max_length=40,null=True)
  
   
    def __str__(self):
        return self.title
    



class department(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,null=True)
   
    def __str__(self):
        return self.name
    



class company(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=20,null=True)
    joptitle=models.CharField(max_length=30,blank=True,null=True)
    location=models.CharField(max_length=40,null=True)
    jops=models.ManyToManyField(jop)
    depart = models.OneToOneField(department,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
   




class Applicant(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=20,null=True)
    phone= models.CharField(max_length=20,null=True)
    birthdate=models.DateField(null=True)
    jops=models.ManyToManyField(jop)
    cvl=models.URLField(max_length=200,null=True) 
    depart = models.OneToOneField(department,null=True, on_delete=models.CASCADE)
    skil=models.ManyToManyField(skils)
    def __str__(self):
        return self.name
    
      



class education(models.Model):
    
    id = models.AutoField(primary_key=True)
    describtion=models.CharField(max_length=20,null=True)
    app=models.ForeignKey(Applicant,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
          

class cv(models.Model):
   
    def __str__(self):
        return self.title
    


