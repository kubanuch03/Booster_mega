from django.db import models
from django.utils.translation import gettext_lazy as _


class CourseTeacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='teacher_images/')

    class Meta:
        verbose_name = _("course_teacher")
        verbose_name_plural = _("course_teachers")

    def __str__(self):
        return f'{self.first_name}'


class CourseDirection(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("course_direction")
        verbose_name_plural = _("course_directions")

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course_images/')
    extended_image = models.ImageField(upload_to='extended_course_images/')
    duration = models.CharField(max_length=255)
    monthly_price = models.FloatField()
    installment_price = models.FloatField()
    lesson_duration = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    timetable = models.CharField(max_length=255)
    free_spots = models.IntegerField()
    description_title = models.CharField(max_length=255)
    major_description = models.TextField()
    major_image = models.ImageField(upload_to='major_images/')
    direction = models.ForeignKey(CourseDirection, on_delete=models.CASCADE)
    teacher = models.ForeignKey(CourseTeacher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")

    def __str__(self):
        return f'{self.name}'


class MajorBenefit(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='major_benefit_images/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("major_benefit")
        verbose_name_plural = _("major_benefits")

    def __str__(self):
        return f'{self.name}'


class EducationBenefit(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='education_benefit_images/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("education_benefit")
        verbose_name_plural = _("education_benefits")

    def __str__(self):
        return f'{self.name}'


class CourseBlock(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    course_direction = models.ForeignKey(CourseDirection, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("course_block")
        verbose_name_plural = _("course_blocks")

    def __str__(self):
        return f'{self.name}'


class BlockSubheading(models.Model):
    name = models.CharField(max_length=255)
    block = models.ForeignKey(CourseBlock, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("block_subheading")
        verbose_name_plural = _("block_subheadings")

    def __str__(self):
        return f'{self.name}'


class TeacherTechnology(models.Model):
    name = models.CharField(max_length=255)
    teachers = models.ManyToManyField(CourseTeacher)

    class Meta:
        verbose_name = _("teacher_technology")
        verbose_name_plural = _("teacher_technologies")

    def __str__(self):
        return f'{self.name}'
