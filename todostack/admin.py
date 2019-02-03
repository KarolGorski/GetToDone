from django.contrib import admin
from . import models


class TodoStackAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "due_date")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class DifficultyAdmin(admin.ModelAdmin):
    list_display = ("name", "current_multiplier")


class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name", "priority_num")


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Difficulty, DifficultyAdmin)
admin.site.register(models.Priority, PriorityAdmin)
admin.site.register(models.ToDo, TodoStackAdmin)