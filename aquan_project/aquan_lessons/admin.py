from django.contrib import admin
from .models import Lesson, Module, LessonProgress, UserProgress

# Funkcja do przypisania lekcji do wybranego modułu
def assign_to_module(modeladmin, request, queryset):
    module_id = request.POST.get('module')
    if module_id:
        module = Module.objects.get(pk=module_id)
        queryset.update(module=module)

assign_to_module.short_description = "Przypisz zaznaczone lekcje do wybranego modułu"

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'created_at', 'updated_at')
    actions = [assign_to_module]

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['modules'] = Module.objects.all()
        return super(LessonAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Module)
admin.site.register(LessonProgress)
admin.site.register(UserProgress)
