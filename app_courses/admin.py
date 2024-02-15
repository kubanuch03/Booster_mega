from django.contrib import admin

from .models import *


class CourseTeacherAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','description','image',]
    list_filter = ['id',]
    search_fields = ['id','first_name']


class CourseDirectionAdmin(admin.ModelAdmin):
    list_display = ['id','name',]
    list_filter = ['id',]
    search_fields = ['id','name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','direction','duration','start_date','teacher']
    list_filter = ['id','direction','teacher','lesson_duration']
    search_fields = ['id','name',]


class MajorBenefitAdmin(admin.ModelAdmin):
    list_display = ['id','name','course',]
    list_filter = ['id','course',]
    search_fields = ['id','course']


class EducationBenefitAdmin(admin.ModelAdmin):
    list_display = ['id','name','course',]
    list_filter = ['id','course',]
    search_fields = ['id','course']


class CourseBlockAdmin(admin.ModelAdmin):
    list_display = ['id','name','course_direction',]
    list_filter = ['id','course_direction',]
    search_fields = ['id','course_direction']



class BlockSubheadingAdmin(admin.ModelAdmin):
    list_display = ['id','name','block',]
    list_filter = ['id','block',]
    search_fields = ['id','block']


class TeacherTechnologyAdmin(admin.ModelAdmin):
    list_display = ['id','name',]
    list_filter = ['id',]
    search_fields = ['id',]


admin.site.register(CourseTeacher,CourseTeacherAdmin)
admin.site.register(CourseDirection,CourseDirectionAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(MajorBenefit,MajorBenefitAdmin)
admin.site.register(EducationBenefit,EducationBenefitAdmin)
admin.site.register(CourseBlock,CourseBlockAdmin)
admin.site.register(BlockSubheading,BlockSubheadingAdmin)
admin.site.register(TeacherTechnology,TeacherTechnologyAdmin)

