from datetime import datetime
from django.db import models 
from django.contrib.auth.models import User

class Park(models.Model):
    from_time = models.DateTimeField(default=datetime.now)
    to_time = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True, related_name='parkings')
    rep = models.ForeignKey(User, null=True, related_name='supporters')

    @property
    def is_current(self):
        return not self.to_time or self.to_time>datetime.now()

    def save(self, *args, **kwargs):
        ''' close all open parkings '''
        now = datetime.now()
        for p in self.owner.parkings.filter(to_time__isnull=True):
            p.to_time = now
            super(Park, p).save()

        super(Park, self).save(*args, **kwargs)
