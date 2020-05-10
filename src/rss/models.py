from django.db import models


class Newspaper(models.Model):
    title = models.CharField(max_length=63, null=True)
    link = models.URLField(max_length=255, unique=True, null=True)

    def __repr__(self):
        return "<Newspaper '{}'>".format(self.link)
