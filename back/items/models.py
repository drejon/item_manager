from django.db import models

class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    item_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
