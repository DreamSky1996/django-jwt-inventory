from django.db import models

class Product(models.Model):
    data = models.CharField(max_length=255, null=False)
    del_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.data