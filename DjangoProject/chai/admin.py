from django.contrib import admin
from .models import ChaiVarity,chaiCertificate,ChaiReviews,Store

# Register your models here.


class ChaiReviewInline(admin.TabularInline):
    model=ChaiReviews
    extra=2

class ChaiVarityadmin(admin.ModelAdmin):
    list_display=['name','type','date_added']
    inlines=[ChaiReviewInline]

class Storeadmin(admin.ModelAdmin):
    list_display=['name','location']
    filter_horizontal=('chai_varities',)

class chaiCertificateAdmin(admin.ModelAdmin):
    list_display=['chai','certificate_number']

admin.site.register(ChaiVarity,ChaiVarityadmin)
admin.site.register(Store,Storeadmin)
admin.site.register(chaiCertificate,chaiCertificateAdmin)
# already buidl
