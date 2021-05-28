from django.contrib import admin
from blog.models import Post,BlogComment



# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title',)

# admin.site.register(Article, ArticleAdmin)

admin.site.register((BlogComment,Post))

