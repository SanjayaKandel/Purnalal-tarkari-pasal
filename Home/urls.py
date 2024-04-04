from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name="index"),
    path('Tarkari/',views.add_veg,name='add_veg'),
    path('update_veg/<int:id>/',views.update_veg,name='update_veg'),
    path('retrive_veg/<int:id>/',views.retrive_veg, name="retrive_veg"),
    path('falful/', views.add_fruit, name="falful"),
    path('update_fruit/<int:id>/', views.update_fruit, name="Fruit_update"),
    path('retrive_fruit/<int:id>/',views.retrive_fruit,name="fruit_det"),
    path('delete_veg/<int:id>/', views.delete_veg, name="delete_veg"),
    path('delete_fruit/<int:id>/', views.delete_fruit, name="delete_fruit"),
    
]