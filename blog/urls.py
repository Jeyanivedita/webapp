from django.urls import path


from blog import views

urlpatterns = [
    path('home', views.home, name='home-url'),
    path('about', views.about, name='about-url'),
    path('createpost', views.createPost, name='createpost-url'),

]
