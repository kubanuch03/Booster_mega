from django.urls import path 

from .views import *

urlpatterns = [

    # Course Teacher
    path('list/course/teacher/',CourseTeacherListApiView.as_view(),name='list-course-teacher'),
    path('detail/course/teacher/<int:pk>/',CourseTeacherDetailApiView.as_view(),name='detail-course-teacher'),

    # Course Direction
    path('list/course/direction/',CourseDirectionListApiView.as_view(),name='list-course-direction'),
    path('detail/course/direction/<int:pk>/',CourseDirectionDetailApiView.as_view(),name='detail-course-direction'),

    # Course 
    path('list/course/',CourseListApiView.as_view(),name='list-course'),
    path('detail/course/<int:pk>/',CourseDetailApiView.as_view(),name='detail-course'),

    # About Profession 
    path('list/about_profession/',AboutProfessionListApiView.as_view(),name='list-about-profession'),

    # Major Benefit
    path('list/major/benefit/',MajorBenefitListApiView.as_view(),name='list-major-benefit'),
    path('detail/major/benefit/<int:pk>/',MajorBenefitDetailApiView.as_view(),name='detail-major-benefit'),

    # Education Benefit
    path('list/education/benefit/',EducationBenefitListApiView.as_view(),name='list-education-benefit'),
    path('detail/education/benefit/<int:pk>/',EducationBenefitDetailApiView.as_view(),name='detail-education-benefit'),

    # Course Block
    path('list/course/block/',CourseBlockListApiView.as_view(),name='list-course-block'),
    path('detail/course/block/<int:pk>/',CourseBlockDetailApiView.as_view(),name='detail-course-block'),

    # Block Subhead
    path('list/block/subhead/',BlockSubheadingListApiView.as_view(),name='list-block-subhead'),
    path('detail/block/subhead/<int:pk>/',BlockSubheadingDetailApiView.as_view(),name='detail-block-subhead'),

    # Teacher Technolog
    path('list/teacher/technology/',TeacherTechnologyListApiView.as_view(),name='list-teacher-technology'),
    path('detail/teacher/technology/<int:pk>/',TeacherTechnologyDetailApiView.as_view(),name='detail-teacher-technology'),

]