from django.contrib import admin
from .models import Post 
# Register your models here.

#class PostAdmin(admin.ModelAdmin):

#	list_display= ['title', 'published_date'] #ekrana publishing date ekliyor
#	list_display_links= ['published_date'] #publishin date e link veriyor.
#	list_filter= ['published_date'] #filtreleme alanı
#	search_fields= ['title', 'text'] #arama yapma alanı
#	list_editable= ['title'] #title güncelleme alanı



#	class Meta:
#		model=Post

#admin.site.register(Post, PostAdmin)
admin.site.register(Post)