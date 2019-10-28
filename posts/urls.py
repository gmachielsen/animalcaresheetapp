from django.urls import path
from . import views

urlpatterns = [
        path('', views.post_list, name='post_list'),
        path('post_detail.html', views.post_detail, name='post_detail'),
        path('post_form.html', views.add_animal, name='add_animal'),
]
