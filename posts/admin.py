from django.contrib import admin
from .models import Posts, Images,Categories

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    model = Posts
    list_display = ("title", "date_publication", "user")
    search_fields = ("title", "user")
    list_filter = ("date_publication", "likes", "dislikes")
    list_per_page = 50

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    model = Images
    list_display = ("post", "image")
    search_fields = ("post",)
    list_per_page = 50

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    model = Categories
    search_fields = ("title",)
    list_per_page = 50