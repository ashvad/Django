from django.urls import path
from customer import views

urlpatterns = [
    path("home", views.CustomerIndex.as_view(), name="customer"),
    path("accounts/register",views.SignUpview.as_view(),name="signup"),
    path('accounts/login',views.SignInview.as_view(),name="signin"),
    path('accounts/logout',views.signout,name="signout"),
    path('accounts/password/reset',views.PasswordResetview.as_view(),name="passwordreset"),
    path('carts/items/add/<int:id>',views.add_to_cart,name="addtocart"),
    path('carts/all',views.ViewMycart.as_view(),name="viewmycart"),
    path('carts/items/remove/<int:id>',views.remove_from_cart,name="removeitem"),
    path('order/add/<int:c_id>/<int:p_id>',views.OrderCreateView.as_view(),name="ordercreate"),
    path('oredrs/all',views.OrdersListView.as_view(),name="listorders"),
    path('orders/reviews/add/<int:id>',views.CommentView.as_view(),name="addreview"),
    path('detail/<int:id>',views.DetailallView.as_view(),name="detailall")
]
