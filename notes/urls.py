from django.conf.urls import url
from . import views

app_name= "notes"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^note/add/$', views.NoteCreate.as_view(), name='note-add'),

    url(r'^note/(?P<pk>[0-9]+)/$', views.NoteUpdate.as_view(), name='note-update'),

    url(r'^note/(?P<pk>[0-9]+)/delete/$', views.NoteDelete.as_view(), name='note-delete'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^logout/$', views.logout_user, name='logout'),

    url(r'^login/$', views.login_user, name='login_user'),


]