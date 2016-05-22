#!/usr/bin/env python
#-*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class Company(models.Model):
    companyid = models.IntegerField(primary_key = True, unique = True)
    company_name = models.CharField(max_length = 100)
    tagline = models.CharField(max_length = 200)

    class Meta:
        verbose_name = '公司名称'
        verbose_name_plural = '公司名称'

    def __unicode__(self):
        return self.company_name

class Author(models.Model):
    author_name = models.CharField(max_length = 200)
    email = models.EmailField()

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

    def __unicode__(self):
        return self.author_name

class Content(models.Model):
    contentid = models.ForeignKey(Company, to_field = 'companyid', db_column = 'blog')
    headline = models.CharField(max_length = 255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)

    class Meta:
        verbose_name = '文章列表'
        verbose_name_plural = '文章列表'

    def __unicode__(self):
        return self.headline

class ImgHead(models.Model):
    img = models.ImageField(upload_to = 'uploading')
    headline = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.headline
