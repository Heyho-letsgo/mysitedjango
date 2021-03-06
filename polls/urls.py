__author__ = 'andrew'
from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
        # ex: /polls/5/zo/
    url(r'^(?P<question_id>\d+)/zo/$', views.zo, name='zo'),
        # ex: /polls/5/za/3
    url(r'^(?P<a_id>\d+)/za/$', views.za, name='za')
)