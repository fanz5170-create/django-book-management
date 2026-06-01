from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def home(request):
    return render(request, 'home.html')


def book_list(request):
    # 获取所有图书进行展示
    book_queryset = models.Book.objects.all()
    return render(request, 'book_list.html', locals())


def book_add(request):
    # get请求传递前端页面
    # 获取所有的出版社和作者信息让用户进行选择
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    # 让管理员输入书籍信息,通过post请求传递后端接受信息
    # 保存图书到数据库
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        date = request.POST.get('date')
        publish_id = request.POST.get('publish_id')
        author_list = request.POST.getlist('author')  # 获取完整的列表
        book_obj = models.Book.objects.create(title=title, price=price,
                                              publish_date=date, publish_id=publish_id)
        book_obj.author.add(*author_list)  # 括号内传入多个作者的id,用逗号隔开
        # *author_list:将列表变成位置参数传给函数
        return redirect('book_list')
    return render(request, 'book_add.html', locals())


def book_edit(request):
    edit_id = request.GET.get('edit_id')
    book_obj = models.Book.objects.filter(id=edit_id).first()
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    if request.method == 'POST':
        # 接受前端传递的修改的数据,进行更新
        book_obj.title = request.POST.get('title')
        book_obj.price = request.POST.get('price')
        book_obj.publish_date = request.POST.get('date')
        book_obj.publish_id = request.POST.get('publish_id')
        book_obj.save()
        author_list = request.POST.getlist('author')
        book_obj.author.set(author_list)  # set括号内传入可迭代对象
        return redirect('book_list')
    return render(request, 'book_edit.html', locals())


def book_delete(request, delete_id):
    models.Book.objects.filter(id=delete_id).delete()
    return redirect('book_list')


def publish_list(request):
    publish_queryset = models.Publish.objects.all()
    return render(request, 'publish_list.html', locals())


def publish_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        email = request.POST.get('email')
        models.Publish.objects.create(name=name, addr=addr, email=email)
        return redirect('publish_list')
    return render(request, 'publish_add.html')


def publish_edit(request, edit_id):
    publish_obj = models.Publish.objects.filter(id=edit_id).first()
    if request.method == 'POST':
        publish_obj.name = request.POST.get('name')
        publish_obj.addr = request.POST.get('addr')
        publish_obj.email = request.POST.get('email')
        publish_obj.save()
        return redirect('publish_list')
    return render(request, 'publish_edit.html', locals())


def publish_delete(request, delete_id):
    models.Publish.objects.filter(id=delete_id).delete()
    return redirect('publish_list')


def author_list(request):
    author_queryset = models.Author.objects.all()
    return render(request, 'author_list.html', locals())


def author_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        addr = request.POST.get('addr')
        # 先创建作者详情,再创建作者
        ad_obj = models.AuthorDetail.objects.create(phone=phone, addr=addr)
        models.Author.objects.create(name=name, age=age, author_detail=ad_obj)
        return redirect('author_list')
    return render(request, 'author_add.html')


def author_edit(request, edit_id):
    author_obj = models.Author.objects.filter(id=edit_id).first()
    if request.method == 'POST':
        author_obj.name = request.POST.get('name')
        author_obj.age = request.POST.get('age')
        author_obj.save()
        phone = request.POST.get('phone')
        addr = request.POST.get('addr')
        models.AuthorDetail.objects.filter(author__id=edit_id).update(phone=phone, addr=addr)
        return redirect('author_list')
    return render(request, 'author_edit.html', locals())


def author_delete(request, delete_id):
    # 删除作者详情,就能将关联的作者也删掉
    models.AuthorDetail.objects.filter(author__id=delete_id).delete()
    return redirect('author_list')