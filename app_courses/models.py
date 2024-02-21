from django.db import models
from django.utils.translation import gettext_lazy as _


class CourseTeacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='teacher_images/')

    class Meta:
        verbose_name = _("Преподователь")
        verbose_name_plural = _("Преподователи")

    def __str__(self):
        return f'{self.first_name}'


class CourseDirection(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Направление")
        verbose_name_plural = _("Направления")

    def __str__(self):
        return f'{self.title}'


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course_images/')
    extended_image = models.ImageField(upload_to='extended_course_images/')
    duration = models.CharField(max_length=255)
    monthly_price = models.FloatField()
    installment_price = models.FloatField()
    lesson_duration = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    timetable = models.CharField(max_length=255)
    free_spots = models.IntegerField()
    direction = models.ForeignKey(CourseDirection, on_delete=models.CASCADE)
    teacher = models.ForeignKey(CourseTeacher, on_delete=models.CASCADE)
    about_profession = models.ForeignKey("AboutProfession", on_delete=models.CASCADE,)

    class Meta:
        verbose_name = _("Курс")
        verbose_name_plural = _("Курсы")
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    def __str__(self):
        return f'{self.title}'


class AboutProfession(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='major_benefit_images/')
    major_benefit = models.ManyToManyField("MajorBenefit")
    major_education = models.ManyToManyField("EducationBenefit")

    class Meta:
        verbose_name = _("О Профессии")
        verbose_name_plural = _("О Профессии")
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    def __str__(self):
        return f'{self.title}'


class MajorBenefit(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='major_benefit/')

    class Meta:
        verbose_name = 'Плюсы профессии'
        verbose_name_plural = 'Плюсы профессии'
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

class EducationBenefit(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='education_benefit/')

    class Meta:
        verbose_name = _("Плюсы Курса")
        verbose_name_plural = _("Плюсы Курса")
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    def __str__(self):
        return f'{self.title}'


class CourseBlock(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course_direction = models.ForeignKey(CourseDirection, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Блок Стеков")
        verbose_name_plural = _("Блок Стеков")
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    def __str__(self):
        return f'{self.title}'


class BlockSubheading(models.Model):
    title = models.CharField(max_length=255)
    block = models.ForeignKey(CourseBlock, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Стеки")
        verbose_name_plural = _("Стеки")
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    def __str__(self):
        return f'{self.title}'


class TeacherTechnology(models.Model):
    title = models.CharField(max_length=255)
    teachers = models.ManyToManyField(CourseTeacher)
    indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    class Meta:
        verbose_name = _("Технология Преподователя")
        verbose_name_plural = _("Технологии Преподователей")

    def __str__(self):
        return f'{self.title}'
