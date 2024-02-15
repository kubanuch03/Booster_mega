from django.db import models



class Reviews(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews/')
    subtitle = models.CharField(max_length=100)
    review_text = models.TextField()

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
