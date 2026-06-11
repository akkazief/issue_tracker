from django.shortcuts import render, redirect,get_object_or_404

from issues.models.issue import Issue
from issues.forms import IssueForm


def issues(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('id_list')
        if id_list:
            issues = Issue.objects.filter(id__in=id_list)
            issues.delete()
            return redirect('main')

    issues = Issue.objects.all()
    context = {'issues': issues}
    return render(request, 'issues/issues.html', context)


def details(request, *args, pk, **kwargs):
    issue = get_object_or_404(Issue, pk=pk)
    context = {'issue': issue}
    return render(request, "issues/details.html", context)


def create_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = IssueForm()
    return render(request, 'issues/create_issue.html', {'form': form})

def update_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'POST':
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('details', pk=issue.pk)
    else:
        form = IssueForm(instance=issue)
    return render(request, 'issues/issue_update.html', {'form': form, 'issue': issue})


def delete_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'POST':
        issue.delete()
        return redirect('main')
    return render(request, 'issues/delete_issue.html', {'issue': issue})

