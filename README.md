# Django 图书管理系统

## 项目简介
基于 Python + Django + MySQL 开发的图书后台管理系统，实现了图书、出版社、作者信息的一体化管理。

## 技术栈
- 后端：Python 3.x + Django
- 数据库：MySQL
- 前端：Bootstrap + jQuery

## 核心功能
- 实现图书、出版社、作者三大模块的完整 CRUD 操作
- 支持一对一、一对多、多对多数据库关联模型
- 使用 Django 模板继承搭建响应式前端页面
- 静态资源统一管理，表单数据处理与前后端联动

## 运行方式
1.  创建 MySQL 数据库 `book`
2.  修改项目 `settings.py` 中的数据库配置
3.  执行数据库迁移：
    bash
    python manage.py makemigrations
    python manage.py migrate
    
4.  启动项目：
    bash
    python manage.py runserver
    
