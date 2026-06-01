from django.db import models


# Create your models here.
# 图书表
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    publish_date = models.DateField(auto_now_add=True)
    # 书和出版社一对多:一本书由一个出版社进行出版, 一个出版社可以出版多本书
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)  # 外键字段进行数据库迁移会自动加'属性名_id'当做字段名
    # 书和作者多对多:一本书可以由多个作者编写,一个作者可以写多本书
    author = models.ManyToManyField(to='Author')  # 自动创建关联表'book_author',不会在表中产生字段


# 出版社表
class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    email = models.EmailField()    # 邮箱格式:xxx@xxx.com


# 作者表
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 一对一作者详情:
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)


# 作者详情表
class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=64)