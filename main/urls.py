from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("home/", views.index, name='home'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("add/", views.add, name='add'),
    path('login/', views.userlogin, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.userlogout, name="logout"),
    path('delete/<int:id>', views.destroy, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
]
