from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания", null=True, blank=True)
    members = models.ManyToManyField( User, related_name="projects", verbose_name="Пользователи")


    def __str__(self):
        return self.name

    class Meta:

        permissions = [
            ("manage_members", "Can manage project members"),
        ]

        db_table = "projects"
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"