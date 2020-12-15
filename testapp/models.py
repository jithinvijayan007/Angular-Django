from django.db import models

# Create your models here.

class UserDetails(models.Model):
    pk_bint_id = models.BigAutoField(primary_key = True)
    vchr_name = models.CharField(max_length = 120)
    vchr_address = models.CharField(max_length = 200)
    dat_dob = models.DateField()
    vchr_gender = models.CharField(max_length = 100)
    vchr_email = models.EmailField(unique=True)
    vchr_languages = models.CharField(max_length = 200)


    def __str__(self):
        return self.vchr_name

    class Meta:
        managed = False
        db_table = "user_details"
