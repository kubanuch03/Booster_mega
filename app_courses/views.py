from rest_framework import permissions, generics

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

class CourseTeacherDetailApiView(generics.RetrieveAPIView):
    queryset = CourseTeacher.objects.all()
    serializer_class = CourseTeacherSerializer
    permission_classes = [permissions.AllowAny]




#== Course Direction ================================================================

class CourseDirectionListApiView(generics.ListAPIView):
    queryset = CourseDirection.objects.all()
    serializer_class = CourseDirectionSerializer
    permission_classes = [permissions.AllowAny]


class CourseDirectionDetailApiView(generics.RetrieveAPIView):
    queryset = CourseDirection.objects.all()
    serializer_class = CourseDirectionSerializer
    permission_classes = [permissions.AllowAny]

#== Course  ================================================================


class CourseListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]


class CourseDetailApiView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]


#== Major Benefit ================================================================


class MajorBenefitListApiView(generics.ListAPIView):
    queryset = MajorBenefit.objects.all()
    serializer_class = MajorBenefitSerializer
    permission_classes = [permissions.AllowAny]


class MajorBenefitDetailApiView(generics.RetrieveAPIView):
    queryset = MajorBenefit.objects.all()
    serializer_class = MajorBenefitSerializer
    permission_classes = [permissions.AllowAny]


#== Education Benefit ================================================================


class EducationBenefitListApiView(generics.ListAPIView):
    queryset = EducationBenefit.objects.all()
    serializer_class = EducationBenefitSerializer
    permission_classes = [permissions.AllowAny]


class EducationBenefitDetailApiView(generics.RetrieveAPIView):
    queryset = EducationBenefit.objects.all()
    serializer_class = EducationBenefitSerializer
    permission_classes = [permissions.AllowAny]

#== Course Block ================================================================


class CourseBlockListApiView(generics.ListAPIView):
    queryset = CourseBlock.objects.all()
    serializer_class = CourseBlockSerializer
    permission_classes = [permissions.AllowAny]


class CourseBlockDetailApiView(generics.RetrieveAPIView):
    queryset = CourseBlock.objects.all()
    serializer_class = CourseBlockSerializer
    permission_classes = [permissions.AllowAny]

#== Block Subhead ================================================================


class BlockSubheadingListApiView(generics.ListAPIView):
    queryset = BlockSubheading.objects.all()
    serializer_class = BlockSubheadingSerializer
    permission_classes = [permissions.AllowAny]



class BlockSubheadingDetailApiView(generics.RetrieveAPIView):
    queryset = BlockSubheading.objects.all()
    serializer_class = BlockSubheadingSerializer
    permission_classes = [permissions.AllowAny]
#== Teacher Technology ================================================================


class TeacherTechnologyListApiView(generics.ListAPIView):
    queryset = TeacherTechnology.objects.all()
    serializer_class = TeacherTechnologySerializer
    permission_classes = [permissions.AllowAny]

class TeacherTechnologyDetailApiView(generics.RetrieveAPIView):
    queryset = TeacherTechnology.objects.all()
    serializer_class = TeacherTechnologySerializer
    permission_classes = [permissions.AllowAny]