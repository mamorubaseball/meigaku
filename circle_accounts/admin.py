from django.contrib import admin
from .models import CircleContents,Circles,ParentCategory,Category

#
admin.site.register(Circles)
admin.site.register(CircleContents)
admin.site.register(Category)

