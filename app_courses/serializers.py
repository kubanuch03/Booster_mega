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
    name = serializers.CharField(write_only=True)
    class Meta:
        model = Course
        fields = ['id','name','image','extended_image','duration','monthly_price',
                  'installment_price','lesson_duration','start_date','timetable',
                  'free_spots','description_title','major_description','major_image',
                  'direction','teacher'
                  ]


class MajorBenefitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MajorBenefit
        fields = ['id','name','image','course',]


class EducationBenefitSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationBenefit
        fields = ['id','name','image','course',]


class CourseBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseBlock
        fields = ['id','name','description','course_direction',]


class BlockSubheadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockSubheading
        fields = ['id','name','block',]


class TeacherTechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherTechnology
        fields = ['id','name','teachers',]