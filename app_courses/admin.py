from django.contrib import admin

from .models import *


class CourseTeacherAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','description','image',]
    list_filter = ['id',]
    search_fields = ['id','first_name']


class TeacherTechnologyAdmin(admin.ModelAdmin):
    list_display = ['id',]
    list_filter = ['id',]
    search_fields = ['id',]




class CourseDirectionAdmin(admin.ModelAdmin):
    list_display = ['id','title',]
    list_filter = ['id',]
    search_fields = ['id','title']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','direction','duration','start_date','teacher']
    list_filter = ['id','direction','teacher','lesson_duration']
    search_fields = ['id','title',]


class AboutProfessionAdmin(admin.ModelAdmin):
    list_display = ['id','title',]
    list_filter = ['id','course',]
    search_fields = ['id']



class MajorBenefitAdmin(admin.ModelAdmin):
    list_display = ['id','title',]
    list_filter = ['id',]
    search_fields = ['id']


class EducationBenefitAdmin(admin.ModelAdmin):
    list_display = ['id','title',]
    list_filter = ['id',]
    search_fields = ['id']


class CourseProgramAdmin(admin.ModelAdmin):
    list_display = ['id','title','course_direction',]
    list_filter = ['id','course_direction',]
    search_fields = ['id','course_direction']



class TopicProgramAdmin(admin.ModelAdmin):
    list_display = ['id','title',]
    list_filter = ['id',]
    search_fields = ['id',]





admin.site.register(CourseTeacher,CourseTeacherAdmin)
admin.site.register(CourseDirection,CourseDirectionAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(MajorBenefit,MajorBenefitAdmin)
admin.site.register(EducationBenefit,EducationBenefitAdmin)
admin.site.register(CourseProgram,CourseProgramAdmin)
admin.site.register(TopicProgram,TopicProgramAdmin)
admin.site.register(TeacherTechnology,TeacherTechnologyAdmin)
admin.site.register(AboutProfession,AboutProfessionAdmin)

