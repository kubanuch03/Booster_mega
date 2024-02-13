from django.db import models



class Reviews(models.Model):
    full_name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    review_text = models.TextField()

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
