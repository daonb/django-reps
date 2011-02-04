from django.db import models 
from django.contrib.auth.models import User

class UserProfile(models.Model):
    since = models.DateField()
    rep = models.ForeignKey(User, null=True, related_name='supporters')

class Ballot(models.Model):
    start_date = models.DateField()
    d_day = models.DateField()
    subject = models.TextField()
    description = models.TextField()

class Vote(models.Model):
    ''' a specific vote by a specific user '''
    voter = models.ForeignKey(User, related_name='votes')
    vote = models.DecimalField()
    why = models.TextField()
    when = models.DateField()
    what = models.ForeignKey(Ballot, related_names='votes')
    # TODO: decide on a privacy policy
    # is_public = models.BooleanField(default=False)
