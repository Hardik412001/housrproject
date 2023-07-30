from django.contrib import admin
from loginsys import views
from django.urls import include, path


app_name = 'loginsys'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignUpPage,name='signup'),
    path("login/", views.LoginPage, name="login"),
    # path('home/', views.Homepage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),

]