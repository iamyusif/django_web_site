from django.contrib import admin

from porto.views import portfolio

from .models import Home,About,Portfolio,Profile
from . models import Services 



#home
admin.site.register(Home)

#services

admin.site.register(Services)

#portofilo
admin.site.register(Portfolio)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]


    




