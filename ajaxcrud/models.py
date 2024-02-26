from django.db import models

  
class employee_information(models.Model):
    em_name = models.CharField(max_length=50)
    em_email = models.EmailField()
    em_phn =  models.CharField(max_length=14) 


    def __str__(self):
        return self.em_name
  