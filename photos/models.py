from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Image(models.Model):
    title =models.CharField(max_length =60)
    post_date = models.DateTimeField(auto_now_add=True)
    location= models.ForeignKey(Location)
    category= models.ForeignKey(Category)
    image = models.ImageField(upload_to ='images/' ,default='DEFAULT VALUE')


    