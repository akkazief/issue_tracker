import datetime
from django.db import migrations


def create_project_and_assign(apps, schema_editor):
    Project = apps.get_model("issues", "Project")
    Issue = apps.get_model("issues", "Issue")

    project = Project.objects.create(
        name="Тестовый проект",
        description="Тестовый проект для бонуса",
        start_date=datetime.date(2026, 1, 1),
    )

    for issue in Issue.objects.all():
        issue.project = project
        issue.save()


def rollback(apps, schema_editor):
    Project = apps.get_model("issues", "Project")
    Issue = apps.get_model("issues", "Issue")

    for issue in Issue.objects.all():
        issue.project = None
        issue.save()

    Project.objects.filter(name="Тестовый проект").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("issues", "0003_project_issue_project"),
    ]

    operations = [migrations.RunPython(create_project_and_assign, rollback)]
