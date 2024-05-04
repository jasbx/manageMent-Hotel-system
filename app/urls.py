from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name='home'),
    path('form',views.customers,name='form'),
    path('Reservations',views.reservations,name='Reservations'),
    path('meals',views.meals,name='meals'),
    # path('blank/',views.blank,name='blank'),
    # path('updateBook/<str:pk>',views.update,name='update'),
    # path('deleteBook/<str:pk>',views.delete,name='delete'),
    # path('<slug:slug>/',views.detal_Book,name='detail'),
    

]