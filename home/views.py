import os

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse, Http404

from .models import Changelog, SoundDef
from .forms import ChangelogForm, SoundDefForm


def index(request):
    return render(request, 'index.html', context={})


def login(request):
    return render(request, 'login.html', context={})


def about(request):
    return render(request, 'about.html', context={})


@login_required
def view_changelogs(request):
    if request.method == 'POST':
        form = ChangelogForm(request.POST, request.FILES)

        if form.is_valid():
            changelog = Changelog()
            changelog.file = request.FILES['changelog_file_input']
            changelog.userid = request.user.id
            changelog.save()

    else:
        form = ChangelogForm()

    context = {
        'changelogs': Changelog.objects.filter(userid=request.user.id),
        'form': form,
        'userid': request.user.id
    }
    return render(request, 'view_changelogs.html', context=context)


@login_required
def view_sounddefs(request):
    if request.method == 'POST':
        form = SoundDefForm(request.POST, request.FILES)

        if form.is_valid():
            sounddef = SoundDef()
            sounddef.file = request.FILES['sounddef_file_input']
            sounddef.userid = request.user.id
            sounddef.save()

    else:
        form = SoundDefForm()

    context = {
        'sounddefs': SoundDef.objects.filter(userid=request.user.id),
        'form': form
    }
    return render(request, 'view_sounddefs.html', context=context)


# downloading files method taken from https://stackoverflow.com/questions/36392510/django-download-a-file
# filetype designates if it's a changelog or sound def file
def download(request, filename, filetype):
    path = filetype + '/user_' + str(request.user.id) + '/' + filename
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return Http404
