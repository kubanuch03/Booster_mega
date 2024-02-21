from django.db import models
from django.utils.translation import gettext_lazy as _


class CourseTeacher(models.Model):
    first_name = models.CharField(max_length=255,verbose_name='Имя')
    last_name = models.CharField(max_length=255,verbose_name='Фамилия')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='teacher_images/',verbose_name='Фотография')

    class Meta:
        verbose_name = _("Преподователь")
        verbose_name_plural = _("Преподователи")

    def __str__(self):
        return f'{self.first_name}'


class CourseDirection(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок')

    class Meta:
        verbose_name = _("Направление")
        verbose_name_plural = _("Направления")

    def __str__(self):
        return f'{self.title}'


class Course(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='course_images/',verbose_name='Картинка')
    extended_image = models.ImageField(upload_to='extended_course_images/',verbose_name='Иконка')
    duration = models.CharField(max_length=255,verbose_name='Продолжительность')
    monthly_price = models.FloatField(verbose_name='Месячная цена')
    installment_price = models.FloatField(verbose_name='Цена в Рассрочку')
    lesson_duration = models.CharField(max_length=255,verbose_name='Продолжительность урока')
    start_date = models.DateTimeField(verbose_name='Старт Курса')
    timetable = models.CharField(max_length=255,verbose_name='Расписание')
    free_spots = models.IntegerField(verbose_name='Свободные места')
    direction = models.ForeignKey(CourseDirection, on_delete=models.CASCADE,verbose_name='Направление')
    teacher = models.ForeignKey(CourseTeacher, on_delete=models.CASCADE,verbose_name='Преподователи')
    about_profession = models.ForeignKey("AboutProfession", on_delete=models.CASCADE,verbose_name='О профессии')
    course_program = models.ForeignKey("CourseProgram",on_delete=models.CASCADE,verbose_name='Программа курса')

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
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='major_benefit_images/',verbose_name='Картинка')
    major_benefit = models.ManyToManyField("MajorBenefit",verbose_name='Плюсы профессии')
    major_education = models.ManyToManyField("EducationBenefit",verbose_name='Плюсы Курса')

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
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    image = models.ImageField(upload_to='major_benefit/',verbose_name='Иконка')

    class Meta:
        verbose_name = 'Плюсы профессии'
        verbose_name_plural = 'Плюсы профессии'
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]
    def __str__(self):
        return f'{self.title}'
    

class EducationBenefit(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    image = models.ImageField(upload_to='education_benefit/',verbose_name='Иконка')

    class Meta:
        verbose_name = _("Плюсы Курса")
        verbose_name_plural = _("Плюсы Курса")
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    def __str__(self):
        return f'{self.title}'


class CourseProgram(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовка')
    topic = models.ManyToManyField("TopicProgram",verbose_name='Темы')
    course_direction = models.ForeignKey(CourseDirection, on_delete=models.CASCADE,verbose_name='Направление Курса')

    class Meta:
        verbose_name = _("Программа Курса")
        verbose_name_plural = _("Программа Курсов")
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    def __str__(self):
        return f'{self.title}'


class TopicProgram(models.Model):
    title = models.CharField(max_length=255,verbose_name='Загаловка')

    class Meta:
        verbose_name = _("Тема курса")
        verbose_name_plural = _("Темы курса")
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    def __str__(self):
        return f'{self.title}'


class TeacherTechnology(models.Model):
    title = models.CharField(max_length=255,verbose_name='Загаловка')
    teachers = models.ManyToManyField(CourseTeacher,verbose_name='Преподователи')
    indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']),  
        ]

    class Meta:
        verbose_name = _("Технология Преподователя")
        verbose_name_plural = _("Технологии Преподователей")

    def __str__(self):
        return f'{self.title}'
    


