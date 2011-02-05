from django.db import models
from django.contrib.auth.models import User

class Ballot(models.Model):
    start_date = models.DateField()
    d_day = models.DateField()
    subject = models.TextField()
    description = models.TextField()

class Vote(models.Model):
    ''' a specific vote by a specific user '''
    voter = models.ForeignKey(User, related_name='votes')
    vote = models.DecimalField(decimal_places=2, max_digits=2)
    why = models.TextField()
    when = models.DateField()
    what = models.ForeignKey(Ballot, related_name='votes')
    # TODO: decide on a privacy policy
    # is_public = models.BooleanField(default=False)
