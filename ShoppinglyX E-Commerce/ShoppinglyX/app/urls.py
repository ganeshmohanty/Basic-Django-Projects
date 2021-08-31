from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import *
urlpatterns = [
    #path('', views.home),
    path('',views.ProductView.as_view(),name='home'),
    #path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>',views.ProductViewDetail.as_view(),name='product-detail'),
    path('search/',views.search,name="search"),
    path('review/',views.review,name="review"),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('pluscart/',views.plus_cart,name='pluscart'),
    path('minuscart/',views.minus_cart,name='minuscart'),
    path('removecart/',views.remove_cart,name='removecart'),

    #path('buy/<int:pk>', views.buy_now, name='buy-now'),

    #path('profile/', views.profile, name='profile'),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path('address/', views.address, name='address'),
    path('address/<int:pk>', views.address, name='addressdelete'),


    path('orders/', views.orders, name='orders'),
    #path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('fashion/',views.fashion,name='fashion'),
    path('fashion/<slug:data>',views.fashion,name='fashion'),
    #path('fashion/<int:rate>/',views.fashionfilter,name='fashionfilter'),

    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name="login"),
    #path('login/', views.login, name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page="login"),name="logout"),
    path('registration/',views.CustomerRegistraionView.as_view(),name='customerregistration'),
    #path('registration/', views.customerregistration, name='customerregistration'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name="app/passwordchange.html",form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name="passwordchange"),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name="app/passwordchangedone.html"),name="passwordchangedone"),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="app/password_reset.html",form_class=MyPasswordResetForm),name="password_reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html",form_class=MySetPasswordForm),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_complete.html"),name="password_reset_complete"),

    path('checkout', views.checkout, name='checkout'),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
