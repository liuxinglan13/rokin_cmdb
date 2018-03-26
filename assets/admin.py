from django.contrib import admin
from .models import assets
# from django.db import models
# from markdown.widgets import AdminMarkdownWidget


# class TestAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': AdminMarkdownWidget(emoji=False)},
#     }
admin.site.register(assets)

