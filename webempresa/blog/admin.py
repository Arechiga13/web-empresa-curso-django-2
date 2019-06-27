from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    # ordering = ('author',) # Ordenar solo por un campo
    search_fields = ('title', 'content', 'author__username') # categories__name categories es le nombre del modelo y name es el nombre del campo en la tabla origen
    date_hierarchy = 'published' # Agrega una herramienta del filtros por fechas
    list_filter = ('author__username', 'categories__name') # Agrega filtros por listados de campos

    def post_categories(self, obj):
        return [ x.name for x in obj.categories.all().order_by("name") ] # Use '-' to reverse ordering
        # return ", ".join([ x.name for x in obj.categories.all() ])
    
    post_categories.short_description = "Categorias"





admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)