from django.conf import settings
from django.db import models

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # 1. def get_absolute_url(self):
    # 2. Getting the instance(url) of the class Note,
    # 3. instead of referencing the URL itself
    def get_delete_url(self):
        return "/notes/{}/delete".format(self.pk)

    def get_update_url(self):
        return "/notes/{}/update".format(self.pk)
