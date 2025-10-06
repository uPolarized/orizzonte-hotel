from django.db import models

class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=200, blank=True, help_text="URL ou caminho do ícone")
    order = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title
