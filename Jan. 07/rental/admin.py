from django.contrib import admin
from .models import Genre, Movie

#create admin templates
class GenreAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name' )

class MovieAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title')
    list_display = ( 'id', 'title', 'release_year', 'price', 'in_stock')
    #exclude = ('in_stock', 'price')



# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)