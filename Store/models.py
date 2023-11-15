from django.db import models
from django.utils.html import mark_safe
import datetime
import os
import secrets


def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)


class Category(models.Model):
    slug = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=650, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_key = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '1. Category'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    small_description = models.TextField(max_length=200, null=False, blank=False)
    location = models.TextField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    starting_price = models.FloatField()
    status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_key = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '2. Product'

    def __str__(self):
        return self.name

"""
# TBL Banner
class Banner(models.Model):
    img = models.ImageField(upload_to="banner_imgs/")
    alt_text = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '1. Banner'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text
"""

"""
class Estates(models.Model):
    title = models.CharField(max_length=200, null=False)
    images = models.ImageField(upload_to="estates_imgs/", null=True)
    description = models.TextField()
    location = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '2. Estates'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.images.url))

    def __str__(self):
        return self.title
"""

