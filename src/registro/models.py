from django.db import models

# Model do registro

class Register(models.Model):
    class Meta:
        db_table = 'register'
    

    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    testtype = models.CharField(max_length=100)
    testresult = models.CharField(max_length=100)

    def __str__(self):
        return self.name
