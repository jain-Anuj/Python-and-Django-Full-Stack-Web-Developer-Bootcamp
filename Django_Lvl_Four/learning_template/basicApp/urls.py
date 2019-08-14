from django.conf.urls import url
from basicApp import views

app_name = 'basicApp'

urlpatterns = [
    url('relative/',views.relative, name = 'relative'),
    url('other/', views.other, name = 'other'),
]
