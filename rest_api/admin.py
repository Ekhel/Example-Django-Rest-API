from django.contrib import admin
from .models import Nelayan

class PageNelayan(admin.ModelAdmin):
    list_display = ('nama','umur','distrik','kampung')
    list_display_links = ('nama','umur','distrik','kampung')
    search_fields = ('nama','umur','distrik','kampung')
    list_per_page = 10

admin.site.register(Nelayan, PageNelayan)

# Register your models here.
