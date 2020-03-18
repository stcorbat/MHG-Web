from django.shortcuts import redirect
from django.contrib.auth import logout


def logout_req(request):
    logout(request)
    return redirect('/')
