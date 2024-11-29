from django.contrib import admin
from .models import Course, Mounth, ClassAndHomeWork


class MounthInline(admin.TabularInline):
    model = Mounth
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [MounthInline] 

admin.site.register(Mounth)

@admin.register(ClassAndHomeWork)
class ClassAndHomeWorkAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'video', 'homework', 'course', 'mounth')


