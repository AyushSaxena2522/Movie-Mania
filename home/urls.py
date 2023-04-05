from django.urls import path
from . import views



urlpatterns = [
    path('', views.index,name='home'),
    path('search/',views.search,name='search'),
    path('tv/<int:id>/',views.tv_detail,name='tvdetail'),
    path('movie/<int:id>/',views.movie_detail,name='moviedetail'),
    path('person/<int:id>/',views.people_detail,name='peopledetail'),
    path('trending_movies/',views.trending_movies,name='trending_movies'),
    path('trending_tvshows/',views.trending_tvshows,name='trending_tvshows'),
    path('trending_people/',views.trending_people,name='trending_people'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('sign_up',views.sign_up,name='sign_up')
]