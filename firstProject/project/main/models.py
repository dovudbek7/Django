from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='Turkum nomi', max_length=50)


class Review(models.Model):
    name = models.CharField(verbose_name='foydalanuvchi ismi', max_length=100)
    comment = models.TextField()


class Product(models.Model):
    name = models.CharField(verbose_name='Tobar nomi', max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    # Related
    # birga kop ulash product category ga biriktiriladi
    Category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 verbose_name='Tovar turkumi',
                                 related_name='products')
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='reviews')
    
    views = models.PositiveIntegerField(defualt=0)
    description = models.TextField()
    published = models.BooleanField(default=False)
    top = models.BooleanField(default=False)
    
    
