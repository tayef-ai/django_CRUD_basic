
from django.contrib import admin
from django.urls import path
from enroll.views import add_show, delete_data, edit_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', add_show, name='home'),
    path('delete/<int:id>/', delete_data, name='delete'),
    path('edit/<int:id>/', edit_data, name='edit'),
]
