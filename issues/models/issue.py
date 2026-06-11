from django.db import models

from .status import Status
from .type import Type


class Issue(models.Model):
    summary = models.CharField(verbose_name="Краткое описание", max_length=100)
    description = models.TextField(
        verbose_name="Полное описание", null=True, blank=True
    )
    status = models.ForeignKey(Status, on_delete=models.RESTRICT, verbose_name="Статус")
    type = models.ForeignKey(Type, on_delete=models.RESTRICT, verbose_name="Тип")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return self.summary

    class Meta:
        db_table = "issues"
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
