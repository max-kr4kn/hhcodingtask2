from django.contrib import admin
from .models import GenericModel
from .forms import GenericModelForm


class GenericModelAdmin(admin.ModelAdmin):
    form = GenericModelForm


admin.site.register(GenericModel, GenericModelAdmin)
