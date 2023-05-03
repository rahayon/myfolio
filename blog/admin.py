from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''Admin View for Post'''
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}
    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)