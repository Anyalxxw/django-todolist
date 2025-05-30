from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('signup/', views.signup_views, name='signup'),    
]
