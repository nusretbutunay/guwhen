from django.db import models

# Create your models here.

class Hizmet(models.Model):
    hizmet = models.CharField(max_length=150)
    detay=models.TextField()
    fiyat=models.IntegerField()
    indirim=models.BooleanField(blank=False, null=False)
    pic=models.TextField(max_length=100)
    class Meta:
        verbose_name_plural = "Hizmetler"
    def __str__(self):
        return self.hizmet