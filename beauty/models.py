from django.db import models

class PushNotifications(models.Model):
    title = models.CharField(max_length=60)
    message = models.TextField()



def interiorImage(instance, filename):
    return '/'.join( ['interior', str(instance.id), filename] )

class InteriorImage(models.Model):
    image = models.ImageField(
        upload_to='interiorImage',
        max_length=254, blank=True, null=True
    )




def worksOfMastersImage(instance, filename):
    return '/'.join( ['worksofmasters', str(instance.id), filename] )

class WorksOfMastersImage(models.Model):
    image = models.ImageField(
        upload_to='worksOfMastersImage',
        max_length=254, blank=True, null=True
    )


