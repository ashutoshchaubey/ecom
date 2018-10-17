from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
	path('', views.home, name='home'),
	path('upload-design/', views.model_form_upload, name='model_form_upload'),
]