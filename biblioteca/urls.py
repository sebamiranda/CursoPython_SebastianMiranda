"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', BookView.as_view(), name='book'),
    path('book/<str:author_name>', BookView.as_view(), name='book'),
    path('book/update/<int:book_id>', BookView.as_view(), name='book'),
    path('book/delete/<int:book_id>', BookView.as_view(), name='book'),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<str:category_name>', CategoryView.as_view(), name='category'),
    path('category/update/<int:category_id>', CategoryView.as_view(), name='category'),
    path('category/delete/<int:category_id>', CategoryView.as_view(), name='category'),
    path('author/', AuthorView.as_view(), name='author'),
    path('author/<str:last_name>', AuthorView.as_view(), name='author'),
    path('author/update/<int:author_id>', AuthorView.as_view(), name='author'),
    path('author/delete/<int:author_id>', AuthorView.as_view(), name='author'),
    path('partner/', PartnerView.as_view(), name='partner'),
    path('partner/<str:partner_name>', PartnerView.as_view(), name='partner'),
    path('partner/update/<int:partner_id>', PartnerView.as_view(), name='partner'),
    path('partner/delete/<int:partner_id>', PartnerView.as_view(), name='partner'),
    path('bookloan/', BookLoan.as_view(), name='bookloan'),
    path('bookloan/<str:category_name>', BookLoan.as_view(), name='bookloan'),
    path('bookloan/update/<int:category_id>', BookLoan.as_view(), name='bookloan'),
    path('bookloan/delete/<int:category_id>', BookLoan.as_view(), name='bookloan'),
]
