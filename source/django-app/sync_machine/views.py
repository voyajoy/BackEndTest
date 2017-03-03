from django.http import JsonResponse

from sync_machine.models import Commit, Contributor


def authors_list(request):
    authors = Contributor.objects.all()
    results = []
    for author in authors:
        results.append({
            'id': author.id,
            'name': author.name
        })
    response = dict(result=results)
    return JsonResponse(response, status=200)


def commits_list(request, author_id=None):
    commits = Commit.objects.all().filter(author_id=author_id)
    results = []
    for commit in commits:
        results.append({
            'id': commit.id,
            'sha': commit.sha,
            'status': commit.get_status_display()
        })
    response = dict(result=results)
    return JsonResponse(response, status=200)


def commit_update_status(request, commit_id=None, status=None):
    try:
        commit = Commit.objects.all().get(id=commit_id)
        commit.status = status
        commit.save()
        return JsonResponse({'result': 'Updated'}, status=200)
    except Commit.DoesNotExist:
        return JsonResponse({'error': 'Object not found'}, status=404)
