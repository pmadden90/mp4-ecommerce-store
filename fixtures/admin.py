from django.contrib import admin
from .models import Post, Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'fixture',
        'competition',
        'time',
        'date',
        'category',
        'result',
        'venue'
    )

    ordering = ('date',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
