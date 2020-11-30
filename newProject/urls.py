from django.contrib import admin
from django.urls import path
from newProject import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('initial/', views.hello),
    path('houses/',views.house_view, name='houses')
]
