from django.db import models


class OrderList(models.Model):
    order_info = models.CharField(max_length=200)
    order_success = models.CharField(max_length=10,default=0)