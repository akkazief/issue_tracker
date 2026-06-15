from datetime import timedelta
from django.utils import timezone
from django.db.models import Q, Count, F

from issues.models.issue import Issue


# 1
closed_last_month = Issue.objects.filter(
    status__name="Done",
    updated_at__gte=timezone.now() - timedelta(days=30)
)
print(closed_last_month)


# 2
issues_by_status_and_type = Issue.objects.filter(
    Q(status__name="Done") | Q(status__name="In Progress"),
    Q(type__name="Enhancment") | Q(type__name="Task")
).distinct()
print(issues_by_status_and_type)


# 3
not_closed_bug = Issue.objects.filter(
    ~Q(status__name="Done"),
    Q(summary__icontains="bug") | Q(type__name="Bug")
).distinct()
print(not_closed_bug)


# bonus_1
issues_by_fields = Issue.objects.values(
    "id",
    "summary",
    "type__name",
    "status__name"
)
for issue in Issue.objects.all().order_by("id"):
    types = ", ".join(issue.type.values_list("name", flat=True))
    print(f"ID: {issue.pk} | {issue.summary} | Тип: {types} | Статус: {issue.status.name}")


# bonus_2
similar_summary_description = Issue.objects.filter(
    description=F("summary")
)
print(similar_summary_description)


# bonus_3
count_issues_by_type = Issue.objects.values(
    "type__name").annotate(
    count=Count("id")
).order_by("-count")

print(count_issues_by_type)


