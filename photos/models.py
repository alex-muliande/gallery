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

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()

class Image(models.Model):
    title =models.CharField(max_length =60)
    post_date = models.DateTimeField(auto_now_add=True)
    location= models.ForeignKey(Location)
    category= models.ForeignKey(Category)
    image = models.ImageField(upload_to ='images/' ,default='DEFAULT VALUE')

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    @classmethod    
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod 
    def search_by_category(cls,search_term):
        images= cls.objects.filter(category__category__icontains=search_term)

        return images
    