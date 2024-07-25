from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название заметки'
    )
    description = models.TextField(
        verbose_name='Описание заметки'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    completed = models.BooleanField(
        default=False,
        verbose_name='Выполнено'
    )

    def __str__(self):
        return f'{self.title} была написана {self.created_at} числа'
    
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'