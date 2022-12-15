from django.urls import path,re_path
from django.views.generic import TemplateView
from . import views




urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("",views.getRoutes,name="routes"),
    path('events/',views.getEvents,name="events"),
    path('event/<str:pk>',views.getEvent,name="events"),
    path('users/profile/',views.getUserProfile,name="user-profile"),
    path('users/',views.getUsers,name="users"),
    path('users/register/',views.registerUser,name="register")

]