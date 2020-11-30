from django.db import models
from django.http import HttpResponseRedirect

class houses(models.Model):
    size_meters = models.IntegerField()
    address = models.TextField(50)
    vendor_name = models.CharField(25)
    
    def __str__(self):
        return self.vendor_name
    
    def get_absolute_url():
        return HttpResponseRedirect(reverse('house_url'))
