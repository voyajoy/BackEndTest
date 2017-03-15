from django.shortcuts import render_to_response, redirect
from django.http.response import Http404
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from .models import Commits

# Create your views here.

def commits(request, page_number=1):

    all_commits = Commits.objects.order_by('-pub_date')
    current_page = Paginator(all_commits, 5)
    print(timezone.now().minute)
    return render_to_response('commits.html', {'commits': current_page.page(page_number)})

def readed(request, commit_id, page_number):
    try:
        commits = Commits.objects.get(id=commit_id)
        if commits.read_status:
            commits.read_status = False
        else:
            commits.read_status = True
        commits.save()
        response = redirect('/page/'+page_number+"/")
        return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/page/'+page_number+'/')
