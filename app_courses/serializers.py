from rest_framework import serializers,generics

from .models import (
    CourseTeacher,
    CourseDirection,
    Course,
    MajorBenefit,
    EducationBenefit,
    CourseProgram,
    TopicProgram,
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
                  'free_spots','direction','teacher','about_profession','course_program',
                  ]
    

class CourseProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseProgram
        fields = ['id','title','topic','course_direction']

class CourseDetailSerializer(serializers.ModelSerializer):
    teacher = CourseTeacherSerializer()
    about_profession = AboutProfessionSerializer()
    direction = CourseDirectionSerializer()
    course_program = CourseProgramSerializer()
    class Meta:
        model = Course
        fields = ['id','title','description','image','extended_image','duration','monthly_price',
                  'installment_price','lesson_duration','start_date','timetable',
                  'free_spots','direction','teacher','about_profession','course_program',
                  ]
    def to_representation(self, instance):
        data_course = super().to_representation(instance)
        if isinstance(self.instance, list):
            return data_course
        
        data_course['direction'] = CourseDirectionSerializer(instance.direction).data
        data_course['teacher'] = CourseTeacherSerializer(instance.teacher).data
        data_course['about_profession'] = AboutProfessionSerializer(instance.about_profession).data
        data_course['course_program']={
            'id': data_course['about_profession']['id'],
            'title': data_course['about_profession']['title'],
            'topic': [{'id': topic.id, 'title': topic.title} for topic in instance.course_program.topic.all()],
            'course_direction': data_course['course_program']['course_direction']
        }
        return data_course




class TopicProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseProgram
        fields = ['id','title',]


class TeacherTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherTechnology
        fields = ['id','title','teachers',]