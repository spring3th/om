from django.contrib import admin
from image.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','slug','image','created']
    list_filter = ['created']

admin.site.register(Image,ImageAdmin)