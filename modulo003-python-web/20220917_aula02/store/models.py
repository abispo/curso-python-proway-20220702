from django.db import models


class ItemsList(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()


class Item(models.Model):
    item_list = models.ForeignKey(ItemsList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
