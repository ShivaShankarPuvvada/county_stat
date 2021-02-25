from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
]
