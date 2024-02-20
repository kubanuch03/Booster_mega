from rest_framework import serializers

from .models import (
    CourseTeacher,
    CourseDirection,
    Course,
    MajorBenefit,
    EducationBenefit,
    CourseBlock,
    BlockSubheading,
    TeacherTechnology,

)



class CourseTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseTeacher
        fields = ['id','first_name','last_name','description','image']


class CourseDirectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseDirection
        fields = ['id','name']


class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.first_name')
    direction_name = serializers.CharField(source='direction.name')
    name = serializers.CharField(write_only=True)
    class Meta:
        model = Course
        fields = ['id','name','image','extended_image','duration','monthly_price',
                  'installment_price','lesson_duration','start_date','timetable',
                  'free_spots','description_title','major_description','major_image',
                  'direction','direction_name','teacher','teacher_name',
                  ]


class MajorBenefitSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name')
    class Meta:
        model = MajorBenefit
        fields = ['id','name','image','course','course_name']


class EducationBenefitSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name')
    class Meta:
        model = EducationBenefit
        fields = ['id','name','image','course','course_name']


class CourseBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseBlock
        fields = ['id','name','description','course_direction',]


class BlockSubheadingSerializer(serializers.ModelSerializer):
    block_name = serializers.CharField(source='block.name')

    class Meta:
        model = BlockSubheading
        fields = ['id','name','block','block_name',]


class TeacherTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherTechnology
        fields = ['id','name','teachers',]