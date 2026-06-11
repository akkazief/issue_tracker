from django.db import models

# Create your models here.

STATUS_CHOICES = [('new', 'Новое'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Описание")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Детальное описание")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    deadline = models.DateField(max_length=100, null=True, blank=True, verbose_name="Срок выполнения")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Задания"
        verbose_name = "Задания"
