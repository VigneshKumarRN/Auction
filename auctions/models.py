from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class AuctionListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name_of_item = models.CharField(max_length=84)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listing_category")
    image_url = models.URLField()
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name_of_item} posted by {self.user}"

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"bid on item: {self.name} by {self.user} with price: {self.bid}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.comment} - {self.user}"

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    watching = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} : {self.user}'
