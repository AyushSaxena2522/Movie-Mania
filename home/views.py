from django.shortcuts import render
import requests
from django.http import HttpResponse,JsonResponse


TMDB_API_KEY="4b4a35c6f0859e3a8713441704bfe252"
# Create your views here.
def search(request):
    query = request.GET.get('q')

    result = []
    if query:
        data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
        # temp = []
        # for a in data.json()["results"]:
        #     if len(temp)<3:
        #         temp.append({"name":a["name"],"poster": a["poster_path"],"overview": a["overview"]})
        #     else:
        #         result.append(temp)
        # result.append(temp) if len(temp)>0 else None

    else:
        return HttpResponse("please enter a search query")
    return render(request,'results.html',{
        'data':data.json(),
        'type':request.GET.get('type')
    })


def index(request):
    data = requests.get(f"https://api.themoviedb.org/3/trending/all/day?api_key={TMDB_API_KEY}&language=en-US")
    data1 = requests.get(f"https://api.themoviedb.org/3/trending/tv/day?api_key={TMDB_API_KEY}&language=en-US")

    
    return render(request, 'index.html',{
        'data':data.json(),
        'data1':data1.json(),
    })


def trending_movies(request):
    data = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}&language=en-US")
   
    return render(request, 'Trending_movies.html',{
        'data':data.json(),
    })

def trending_tvshows(request):
    data = requests.get(f"https://api.themoviedb.org/3/trending/tv/day?api_key={TMDB_API_KEY}&language=en-US")
   
    return render(request, 'Trending_tvshows.html',{
        'data':data.json(),
    })

def trending_people(request):
    data = requests.get(f"https://api.themoviedb.org/3/trending/person/day?api_key={TMDB_API_KEY}&language=en-US")
   
    return render(request, 'Trending_people.html',{
        'data':data.json(),
    })

def tv_detail(request,id):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{id}?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false")
    recommendations = requests.get(f"https://api.themoviedb.org/3/tv/{id}/recommendations?api_key={TMDB_API_KEY}&language=en-US")

    return render(request,'tv_details.html',{
        'data':data.json(),
        'recommendations':recommendations.json(),
        'type':"tv"
        
    })

def people_detail(request,id):
    data = requests.get(f"https://api.themoviedb.org/3/person/{id}?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false")
    recommendations = requests.get(f"https://api.themoviedb.org/3/person/{id}/recommendations?api_key={TMDB_API_KEY}&language=en-US")

    return render(request,'people_details.html',{
        'data':data.json(),
        'recommendations':recommendations.json(),
        'type':"person"
        
    })

def movie_detail(request,id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false")
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{id}/recommendations?api_key={TMDB_API_KEY}&language=en-US")

    return render(request,'movie_details.html',{
        'data':data.json(),
        'recommendations':recommendations.json(),
        'type':"movie"
        
    })

def about(request):
    return render(request,'about.html')
# HttpResponse("This is about page")

def services(request):
    return render(request,'services.html')
# HttpResponse("Bs mara li gaand")

def contact(request):
    return render(request,'contact.html')
# HttpResponse("This is contact page")

def sign_up(request):
    return render(request,'sign_up.html')
