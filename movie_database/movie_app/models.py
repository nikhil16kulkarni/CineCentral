from django.db import models

class Movie(models.Model):
    movie_id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    budget = models.CharField(max_length=255)
    revenue = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    runtime = models.CharField(max_length=255)
    popularity = models.CharField(max_length=255)


class Genre(models.Model):
    genre_id = models.CharField(max_length=1000, primary_key=True)
    genre_name = models.CharField(max_length=1000)


class GenreMovie(models.Model):
    # genre_id = models.CharField(max_length=1000)
    # gm_id=models.CharField(max_length=1000,)
    genre_name = models.CharField(max_length=1000)
    # movie_id = models.CharField(max_length=1000)
    genre_ref = models.ForeignKey(Genre, on_delete=models.CASCADE)
    movie_ref1 = models.ForeignKey(Movie, on_delete=models.CASCADE)


# class Keyword(models.Model):
#     keyword_id = models.CharField(max_length=1000, primary_key=True)
#     keyword_name = models.CharField(max_length=1000)

# class KeywordMovie(models.Model):
#     keyword_id = models.CharField(max_length=1000)
#     keyword_name = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='keywords')
#     movie_ref2 = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='keywords_ref2')

# class ProductionCompanies(models.Model):
#     production_companies_id = models.CharField(max_length=1000, primary_key=True)
#     production_companies_name = models.CharField(max_length=1000)

# class ProductionCompaniesMovie(models.Model):
#     production_companies_id = models.CharField(max_length=1000)
#     production_company = models.ForeignKey(ProductionCompanies, on_delete=models.CASCADE, related_name='production_companies')
#     movie_ref3 = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='production_companies_ref3')

# class ProductionCountries(models.Model):
#     production_countries_id = models.CharField(max_length=1000, primary_key=True)
#     production_countries_name = models.CharField(max_length=1000)

# class ProductionCountriesMovie(models.Model):
#     production_countries_id = models.CharField(max_length=1000)
#     production_countries = models.ForeignKey(ProductionCountries, on_delete=models.CASCADE, related_name='production_countries')
#     movie_ref4 = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='production_countries_ref4')
