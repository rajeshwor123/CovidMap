from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.patientAdd, name='patientUpdate'),
    path('delete/<int:id>',views.patientDelete, name ='patientDelete'),
    path('patientAdd.html', views.patientAdd, name = 'patientAdd'),
]
