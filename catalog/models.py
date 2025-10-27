# 模型
from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Genre(models.Model):
    """书籍类别"""

    name = models.CharField(max_length=200, help_text="输入书籍类别(如科幻小说、文学等)")

    def __str__(self):
        """字符串表示"""
        return self.name
    
    
class Book(models.Model):
    """书籍模型"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)  
    summary = models.TextField(max_length=1000, help_text="输入书籍简介(不超过1000个字符)")
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text="输入书籍ISBN(13位数字)")
    genre = models.ManyToManyField(Genre, help_text="选择书籍类别")

    def __str__(self):
        """字符串表示"""
        return self.title
    
    def get_absolute_url(self):
        """返回书籍详情页的URL"""
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        """创建一个字符串，用于在Admin中显示书籍类别"""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = '类别'
    
    
class BookInstance(models.Model):
    """书籍实例模型(特定书籍的具体副本)"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="书籍唯一ID")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)  
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', '维护中'),
        ('o', '已借出'),
        ('a', '可借'),
        ('r', '预订中'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='书籍当前状态',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """字符串表示"""
        return f'{self.id} ({self.book.title})'
    

class Author(models.Model):
    """作者模型"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('逝世日期', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """返回作者详情页的URL"""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """字符串表示"""
        return f'{self.last_name}, {self.first_name}'
    
@property
def is_overdue(self):
    """判断书籍实例是否逾期"""
    if self.due_back and date.today() > self.due_back:
        return True
    return False