from django.db import models
from django.utils import timezone
DELIVERED=(
    ("True","True"),
    ("False", "False")
)


class Category(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Item(models.Model):
    name=models.CharField(max_length=200, null=False)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.IntegerField(null=False, blank=False)
    description=models.TextField(max_length=1000, null=True, blank=True)
    image=models.TextField(default='https://th.bing.com/th/id/R.eef165ce3d85779436c21fac35fb52bf?rik=ye5wclB7Tdn11w&riu=http%3a%2f%2fwww.pngmart.com%2ffiles%2f14%2fColorful-Shopping-Bag-Transparent-PNG.png&ehk=SY8Ni2y8vUMhDfyQr4GEhsTBHLL0CPYyea3hwjCI3hY%3d&risl=&pid=ImgRaw&r=0')

    def __str__(self):
        return self.name


class Supplier(models.Model):
    itemname=models.CharField(max_length=200)
    ordername=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    qty=models.IntegerField(default=1)
    date=models.DateTimeField(default=timezone.now)
    delivered=models.CharField(max_length=20, choices=DELIVERED, default='False')
    
    def __str__(self):
        return self.ordername

