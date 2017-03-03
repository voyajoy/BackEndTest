from django.conf.urls import url, include

from sync_machine.views import authors_list, commits_list, commit_update_status

urlpatterns = (

    url(r'^authors/$', authors_list),
    url(r'^commits/author/(?P<author_id>[0-9]+)/$', commits_list),
    url(r'^commit/(?P<commit_id>[0-9]+)/(?P<status>(R|U)?)/$', commit_update_status)

)
