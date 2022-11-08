"""management URL Configuration

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
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', UserRegistration.as_view() , name='signup'),
    path('login/', UserLogin.as_view() , name='login'),
    path('bookview/', BookView.as_view() , name='Allbookview'),
    path('bookview/<int:id>/', BookView.as_view() , name='bookview'),
    path('bookentry/', BookEntryView.as_view() , name='bookentry'),
    path('bookupdate/<int:id>/', BookUpdate.as_view() , name='bookupdate'),
    path('bookdelete/<int:id>/', BookDelete.as_view() , name='bookdelete'),
    path('lendbook/', LendBookView.as_view() , name='lendbook'),
    
    
    


]
