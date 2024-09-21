from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=50)
    dloc=models.CharField(max_length=50)
    def __str__(self):
        return self.dname
    

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=50)
    job=models.CharField(max_length=50)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    hiredate=models.DateField(auto_now_add=True)
    sal=models.DecimalField(max_digits=20,decimal_places=3)
    comm=models.DecimalField(max_digits=20,decimal_places=3)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE) 
    def __str__(self):
        return self.ename

class Salgrad(models.Model):
    grade=models.DecimalField(max_digits=20,decimal_places=3)
    losal=models.DecimalField(max_digits=20,decimal_places=3)
    hisal=models.DecimalField(max_digits=20,decimal_places=3)
    
    
      