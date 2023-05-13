"""mathoperation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from calculation import views
from Book import views as bv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('operations/add',views.add),
    path('operations/sub',views.sub),
    path('operations/mul',views.mul),
    path('operations/div',views.div),
    path('operations/vowels',views.vowels),
    path('operations/cbv/add',views.Addview.as_view(),name="addition"),
    path('operations/cbv/sub',views.Subview.as_view(),name="substraction"),
    path('operations/cbv/mul', views.Mulview.as_view(),name="multiplication"),
    path('operations/cbv/div', views.Divview.as_view(),name="division"),
    path('',views.Indexview.as_view(),name="Index"),
    path('books/add',bv.BookView.as_view(),name="addbook"),
    path('books/all',bv.BookList.as_view(),name="allbooks"),
    path('books/<int:id>',bv.Bookdetails.as_view(),name="bookdetails"),
    path('book/remove/<int:id>',bv.BookdeleteView.as_view(),name="bookdelete"),
    path('book/change/<int:id>',bv.ChangeBook.as_view(),name="changebook"),
    path('customers/',include("customer.urls")),
    path('books/dashboard',bv.DashboardView.as_view(),name="dashboard"),
    path('books/order/<int:id>',bv.OrderdetailView.as_view(),name="orderdetail"),
    path('books/update/<int:id>',bv.OrderUpdateView.as_view(),name="updateorder")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
