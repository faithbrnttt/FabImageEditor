from django.urls import path
from  .views import PhotoList, PhotoDetail, PhotoUpload, PhotoUpdate, PhotoDelete, AccountLogin,  AccountRegister
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', AccountLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', AccountRegister.as_view(), name='register'),
    path('', PhotoList.as_view(), name='photos'),
    path('photo/<int:pk>/', PhotoDetail.as_view(), name='photo'),
    path('upload/', PhotoUpload.as_view(), name='upload'),
    path('update/<int:pk>/', PhotoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name='delete'),
   
   
 

    
]