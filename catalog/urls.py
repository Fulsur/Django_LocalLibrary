from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),        # catalog/ 映射到 views.index 视图函数
    path('books/', views.BookListView.as_view(), name='books'),  # 列出所有书籍
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # 书籍详情页
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),  # 当前用户借阅的书籍列表
    path('book/<uuid:pk>/renew/',views.renew_book_librarian, name='renew-book-librarian'),  # 图书续借
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),  # 创建作者
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),  # 更新作者
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),  # 删除作者
]