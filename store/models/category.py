from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)


    @staticmethod
    def ge_all_category():
        return Category.objects.all()

    def __str__(self):
        return self.name