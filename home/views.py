from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
            # django does not allow models to be committed without all fields filled in, so don't commit it yet
            changelog = form.save(commit=False)
            changelog.userid = request.user.id
            changelog.save()
    else:
        form = ChangelogForm()

    context = {
        'changelogs': Changelog.objects.filter(userid=request.user.id),
        'form': form
    }
    return render(request, 'view_changelogs.html', context=context)


@login_required
def view_sounddefs(request):
    if request.method == 'POST':
        form = SoundDefForm(request.POST, request.FILES)

        if form.is_valid():
            soundDef = form.save(commit=False)
            soundDef.userid = request.user.id
            soundDef.save()

    else:
        form = SoundDefForm()

    context = {
        'sounddefs': SoundDef.objects.filter(userid=request.user.id),
        'form': form
    }
    return render(request, 'view_sounddefs.html', context=context)
