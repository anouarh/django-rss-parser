from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=63, null=True)
    link = models.URLField(max_length=255, unique=True, null=True)

    def __repr__(self):
        return "<Feed '{}'>".format(self.link)

""" class Item(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField()
    link = models.URLField(max_length=255)
    pub_date = models.DateField("date published")

    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date"]

    def __str__(self):
        return f"{self.feed}: {self.title}"
 """
