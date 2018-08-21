from django.conf.urls import url
from . import views

app_name = "accounts"

urlpattern = [
	url(r'^$',views.index,name='index'),

]


