# seu_app/models.py

from django.db import models

class PollOption(models.Model):
    option_text = models.CharField(max_length=100, unique=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.option_text}"