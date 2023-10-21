from django.contrib import admin


# Register your models here.
from viewset_view.models import Student

# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city') 

admin.site.register(Student, StudentsAdmin)