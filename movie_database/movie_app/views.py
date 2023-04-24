from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .forms import *



# def read_movies(request):


#     # if request.method == 'POST':
#     #     # handle genre_movie_view functionality
#     #     genre_movies = GenreMovie.objects.all()
#     #     return render(request, 'read.html', {'genre_movies': genre_movies})
#     # else:
#     #     # handle read_movies functionality
#     #     movies = Movie.objects.all()
#     #     return render(request, 'read.html', {'movies': movies})




    # sort_by = request.GET.get('sort', 'title')  # default to sorting by title
    # order = request.GET.get('order', 'asc')
    # if order == 'asc':
    #     movies = Movie.objects.order_by(sort_by)
    #     order_qs = 'desc'
    # else:
    #     movies = Movie.objects.order_by(f'{-sort_by}')
    #     order_qs = 'asc'

    # context = {
    #     'movies': movies,
    #     'order_qs': order_qs,
    #     'sort_by': sort_by,
    # }

#     return render(request, 'read.html', context)


# def genre_movie_view(request):
#     genre_movies = GenreMovie.objects.all()
#     for g in genre_movies:
#         print(g.genre_name)
#     context={'genre_movies': genre_movies}
#     return render(request, 'read.html',context )


def read_data(request):
    movie_data = Movie.objects.all()
    genre_data = GenreMovie.objects.all()
    # keyword_data = KeywordMovie.objects.all()
    # production_companies_data = ProductionCompaniesMovie.objects.all()
    # production_countries_data = ProductionCountriesMovie.objects.all()

    # sort_by = request.GET.get('sort', 'title')  # default to sorting by title
    # order = request.GET.get('order', 'asc')
    # if order == 'asc':
    #     movies = Movie.objects.order_by(sort_by)
    #     order_qs = 'desc'
    # else:
    #     movies = Movie.objects.order_by(f'{-sort_by}')
    #     order_qs = 'asc'

    # context = {
    #     'movies': movies,
    #     'order_qs': order_qs,
    #     'sort_by': sort_by,
    # }

    return render(request, 'read.html', {
        'movie_data': movie_data,
        'genre_data': genre_data,
        # 'keyword_data': keyword_data,
        # 'production_companies_data': production_companies_data,
        # 'production_countries_data': production_countries_data,
    })

# def read_data(request):
#     movie_data = Movie.objects.all()
#     genre_data = GenreMovie.objects.all()

#     sort_by = request.GET.get('sort', 'title')  # default to sorting by title
#     order = request.GET.get('order', 'asc')
#     if order == 'asc':
#         movies = Movie.objects.order_by(sort_by)
#         order_qs = 'desc'
#     else:
#         movies = Movie.objects.order_by(f'-{sort_by}')
#         order_qs = 'asc'

#     context = {
#         'movies': movies,
#         'order_qs': order_qs,
#         'sort_by': sort_by,
#         'movie_data': movie_data,
#         'genre_data': genre_data,
#     }

#     return render(request, 'read.html', context)



def update_movie(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)

    if request.method == 'POST':
        movie.title = request.POST['title']
        movie.budget = request.POST['budget']
        movie.revenue = request.POST['revenue']
        movie.release_date = request.POST['release_date']
        movie.runtime = request.POST['runtime']
        movie.popularity = request.POST['popularity']
        movie.save()
        return redirect('read_movies')

    context = {'movie': movie}
    return render(request, 'update.html', context)


def update_movie_record(request):
    if request.method == 'POST':
        # get the data from the form
        movie_id = request.POST['movie_id']
        title = request.POST['title']
        budget = request.POST['budget']
        revenue = request.POST['revenue']
        release_date = request.POST['release_date']
        runtime = request.POST['runtime']
        popularity = request.POST['popularity']

        # update the movie record in the database
        movie = Movie.objects.get(movie_id=movie_id)
        movie.title = title
        movie.budget = budget
        movie.revenue = revenue
        movie.release_date = release_date
        movie.runtime = runtime
        movie.popularity = popularity
        movie.save()

        # redirect to the read view to display the updated record
        return redirect('read_movies')
        
    # handle the case where the request method is not POST
    return HttpResponse('Invalid request method')

def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_movies')
    else:
        form = MovieForm()
    return render(request, 'create.html', {'form': form})


def delete_movie(request):
    if request.method == 'POST':
        movie_id = request.POST['movie_id']
        movie = Movie.objects.get(pk=movie_id)
        movie.delete()
        return redirect('read_movies')
    else:
        return render(request, 'delete.html')

# def delete_movie_from_read(request):
#     if request.method == 'POST':

#         movie_id = request.POST['movie_id']


    




# def login_view(request):
#     next_url = request.GET.get('next')
#     form = AuthenticationForm()
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 if next_url:
#                     return redirect(next_url)
#                 return redirect('read_movies')
#     return render(request, 'login_signup.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = userRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = userRegistration()
    return render(request, 'signup.html', {'form': form})
