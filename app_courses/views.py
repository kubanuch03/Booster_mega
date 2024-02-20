from rest_framework import permissions, generics
from drf_spectacular.utils import extend_schema

from django.db.models import Prefetch

from .models import (
    CourseTeacher,
    CourseDirection,
    Course,
    MajorBenefit,
    EducationBenefit,
    CourseBlock,
    BlockSubheading,
    TeacherTechnology
)

from .serializers import (
    CourseTeacherSerializer,
    CourseDirectionSerializer,
    CourseSerializer,
    MajorBenefitSerializer,
    EducationBenefitSerializer,
    CourseBlockSerializer,
    BlockSubheadingSerializer,
    TeacherTechnologySerializer
)


#== Course Teacher ================================================================
class CourseTeacherListApiView(generics.ListAPIView):
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Все Преподователи",
        description=" Запрос на Все Преподователей ",
        responses={200: CourseTeacherSerializer(many=True)},
        operation_id="list_course_teacher",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CourseTeacherDetailApiView(generics.RetrieveAPIView):
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Детальная информация о  Преподователе",
        description="Детальная информация о  Преподователе",
        responses={200: CourseTeacherSerializer()},
        operation_id="detail_course_teacher",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


#== Course Direction ================================================================

class CourseDirectionListApiView(generics.ListAPIView):
    queryset = CourseDirection.objects.all()
    serializer_class = CourseDirectionSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Все Курсы направления",
        description=" Запрос на Все курсы направления ",
        responses={200: CourseDirectionSerializer(many=True)},
        operation_id="list_course_direction",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CourseDirectionDetailApiView(generics.RetrieveAPIView):
    queryset = CourseDirection.objects.all()
    serializer_class = CourseDirectionSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Детальная информация о курс Направления",
        description="Детальная информация о  курс Направления",
        responses={200: CourseDirectionSerializer()},
        operation_id="detail_course_direction",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#== Course  ================================================================


class CourseListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Course.objects.select_related('direction').all()
        queryset = queryset.prefetch_related(Prefetch('teacher',queryset=CourseTeacher.objects.all()))
        return super().get_queryset()

    @extend_schema(
        summary="Все Курсы ",
        description=" Запрос на Все Курсы  ",
        responses={200: CourseSerializer(many=True)},
        operation_id="list_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CourseDetailApiView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Детальная информация о курсе",
        description="Детальная информация о  курсе",
        responses={200: CourseSerializer()},
        operation_id="detail_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


#== Major Benefit ================================================================


class MajorBenefitListApiView(generics.ListAPIView):
    queryset = MajorBenefit.objects.all()
    serializer_class = MajorBenefitSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = MajorBenefit.objects.select_related('course').all()
        return queryset

    @extend_schema(
        summary="Все Плюсы профессии ",
        responses={200: MajorBenefitSerializer(many=True)},
        operation_id="list_major_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class MajorBenefitDetailApiView(generics.RetrieveAPIView):
    queryset = MajorBenefit.objects.all()
    serializer_class = MajorBenefitSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Детальная информация о о плюс профессии",
        description="Детальная информация о плюс профессии",
        responses={200: MajorBenefitSerializer()},
        operation_id="detail_major_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


#== Education Benefit ================================================================


class EducationBenefitListApiView(generics.ListAPIView):
    queryset = EducationBenefit.objects.all()
    serializer_class = EducationBenefitSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = EducationBenefit.objects.select_related('course')
        return queryset

    @extend_schema(
        summary="Все Плюсы курса ",
        description=" Запрос на Все Плюсы Курсы  ",
        responses={200: CourseTeacherSerializer(many=True)},
        operation_id="list_education_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class EducationBenefitDetailApiView(generics.RetrieveAPIView):
    queryset = EducationBenefit.objects.all()
    serializer_class = EducationBenefitSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Детальная информация о о плюс курса",
        description="Детальная информация о плюс курса",
        responses={200: EducationBenefitSerializer()},
        operation_id="detail_education_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#== Course Block ================================================================


class CourseBlockListApiView(generics.ListAPIView):
    queryset = CourseBlock.objects.all()
    serializer_class = CourseBlockSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = CourseBlock.objects.select_related('course_direction')
        return queryset

    @extend_schema(
        summary="Все Блок Курса ",
        description=" Запрос на Все Блок Курса  ",
        responses={200: CourseBlockSerializer(many=True)},
        operation_id="list_block_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CourseBlockDetailApiView(generics.RetrieveAPIView):
    queryset = CourseBlock.objects.all()
    serializer_class = CourseBlockSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Детальная информация Блок Курса",
        description="Детальная информация Блок Курса",
        responses={200: CourseBlockSerializer()},
        operation_id="detail_sub_block_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#== Block Subhead ================================================================


class BlockSubheadingListApiView(generics.ListAPIView):
    queryset = BlockSubheading.objects.all()
    serializer_class = BlockSubheadingSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Все Под Блок Курса ",
        description=" Запрос на Все Под Блок Курса  ",
        responses={200: BlockSubheadingSerializer(many=True)},
        operation_id="list_sub_block_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BlockSubheadingDetailApiView(generics.RetrieveAPIView):
    queryset = BlockSubheading.objects.all()
    serializer_class = BlockSubheadingSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Детальная информация Под Блок Курса",
        description="Детальная информация Под Блок Курса",
        responses={200: BlockSubheadingSerializer()},
        operation_id="detail_sub_block_course_get",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
#== Teacher Technology ================================================================


class TeacherTechnologyListApiView(generics.ListAPIView):
    queryset = TeacherTechnology.objects.all()
    serializer_class = TeacherTechnologySerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Все Технологии Проподователей ",
        description=" Запрос на Все Технологии Проподователей ",
        responses={200: TeacherTechnologySerializer(many=True)},
        operation_id="list_teacher_technology_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class TeacherTechnologyDetailApiView(generics.RetrieveAPIView):
    queryset = TeacherTechnology.objects.all()
    serializer_class = TeacherTechnologySerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Детальная информация Технологии Проподователя",
        description="Детальная информация Технологии Проподователя",
        responses={200: TeacherTechnologySerializer()},
        operation_id="detail_teacher_technology_course",
        
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)