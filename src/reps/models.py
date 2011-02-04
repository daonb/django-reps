from django.db import models 
from django.contrib.auth.models import User

class Park(models.Model):
    since = models.DateField()
    owner = models.ForeignKey(User, null=True, related_name='parkings')
    rep = models.ForeignKey(User, null=True, related_name='supporters')

