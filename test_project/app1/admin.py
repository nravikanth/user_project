from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Book)
admin.site.register(Book_MM)
admin.site.register(Publication)
admin.site.register(Publication_MM)
