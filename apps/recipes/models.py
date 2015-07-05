from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


    class Meta:
            verbose_name_plural = 'Categories'

    def __unicode__(self):
            return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category)
    description = models.TextField()
    photo = models.FileField()
    ingredients = models.TextField()
    method = models.TextField()

    cooktime = models.IntegerField()
    fat = models.FloatField()
    carbs = models.FloatField()
    protein = models.FloatField()
    calories = models.FloatField()

    def __unicode__(self):
        return self.title
