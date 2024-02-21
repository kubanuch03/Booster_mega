from django.db import models



class Reviews(models.Model):
    full_name = models.CharField(max_length=100,verbose_name='Полное имя')
    image = models.ImageField(upload_to='reviews/',verbose_name='Фотография')
    subtitle = models.CharField(max_length=100,verbose_name='Под Заголовок')
    review_text = models.TextField(verbose_name='Отзыв')

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['full_name']), 
        ]
