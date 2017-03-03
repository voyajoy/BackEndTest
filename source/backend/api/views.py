import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .tasks import fetch_commits
from .models import Commit


def index(request):
    fetch_commits.delay()
    return HttpResponse('200')


def filter_commits(request):
    query = {}
    for p in ['email', 'name']:
        if p in request.GET:
            query[p] = request.GET[p]
    commits = [c.to_dict() for c in Commit.objects.filter(**query)]
    return JsonResponse({'commits': commits})


def commit(request, sha):
    commit = Commit.objects.filter(sha=sha).first()
    if not commit:
        return JsonResponse({'msg': 'not found'}, status=404)
    if request.method == 'PATCH':
        # TODO check content-type
        data = json.loads(request.body)
        if 'seen' in data:
            commit.seen = data['seen']
            commit.save()
    return JsonResponse(commit.to_dict())
