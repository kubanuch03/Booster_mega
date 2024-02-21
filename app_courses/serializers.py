from rest_framework import serializers,generics

from .models import (
    CourseTeacher,
    CourseDirection,
    Course,
    MajorBenefit,
    EducationBenefit,
    CourseBlock,
    BlockSubheading,
    TeacherTechnology,
    AboutProfession

)



class CourseTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseTeacher
        fields = ['id','first_name','last_name','description','image']


class CourseDirectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseDirection
        fields = ['id','title']





class MajorBenefitSerializer(serializers.ModelSerializer):
    # course_name = serializers.CharField(source='course.title')
    class Meta:
        model = MajorBenefit
        fields = ['id','title','image',]


class EducationBenefitSerializer(serializers.ModelSerializer):
    # course_name = serializers.CharField(source='course.title')
    class Meta:
        model = EducationBenefit
        fields = ['id','title','image',]


class AboutProfessionSerializer(serializers.ModelSerializer):
    major_benefit = MajorBenefitSerializer(many=True)
    major_education = EducationBenefitSerializer(many=True)
    class Meta:
        model = AboutProfession
        fields = ['id','title','description','image','major_benefit','major_education']


class CourseListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['id','title','description','image','extended_image','duration','monthly_price',
                  'installment_price','lesson_duration','start_date','timetable',
                  'free_spots','direction','teacher','about_profession',
                  ]
    


class CourseDetailSerializer(serializers.ModelSerializer):
    teacher = CourseTeacherSerializer()
    about_profession = AboutProfessionSerializer()
    direction = CourseDirectionSerializer()
    class Meta:
        model = Course
        fields = ['id','title','description','image','extended_image','duration','monthly_price',
                  'installment_price','lesson_duration','start_date','timetable',
                  'free_spots','direction','teacher','about_profession',
                  ]
    def to_representation(self, instance):
        data_course = super().to_representation(instance)
        if isinstance(self.instance, list):
            return data_course
        
        data_course['direction']={
            'id': data_course['direction']['id'],
            'title': data_course['direction']['title']
        }
        data_course['teacher']={
            'id': data_course['teacher']['id'],
            'first_name': data_course['teacher']['first_name'],
            'last_name': data_course['teacher']['last_name']
        }
        data_course['about_profession']={
            'id': data_course['about_profession']['id'],
            'title': data_course['about_profession']['title'],
            'major_benefit': data_course['about_profession']['major_benefit'],
            'major_education': data_course['about_profession']['major_education']
        }
        return data_course

class CourseBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseBlock
        fields = ['id','title','description','course_direction',]


class BlockSubheadingSerializer(serializers.ModelSerializer):
    block_name = serializers.CharField(source='block.title')

    class Meta:
        model = BlockSubheading
        fields = ['id','title','block','block_name',]


class TeacherTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherTechnology
        fields = ['id','title','teachers',]