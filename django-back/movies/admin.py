from django.contrib import admin
from .models import Movie, Genre, UserRank, Review
# Register your models here.


admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(UserRank)
admin.site.register(Review)
