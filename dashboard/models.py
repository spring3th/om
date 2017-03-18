from django.db import models

class Dashboard_status(models.Model):
    up = models.IntegerField(null=True, blank=True)
    down = models.IntegerField(null=True, blank=True)
    accepted = models.IntegerField(null=True, blank=True)
    unaccepted = models.IntegerField(null=True, blank=True)
    rejected = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return u'%s %s %s %s %s' % (self.up, self.down, self.accepted, self.unaccepted, self.rejected)

