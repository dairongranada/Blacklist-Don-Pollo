from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
# from .models import 

@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def home(request):
    context = {}
    return render(request, 'home.html', {'user_data': context})


@login_required(login_url='/login/')
def mass_query(request):
    return render(request, 'mass_query.html')


@login_required(login_url='/login/')
def consult_lists(request):
    return render(request, 'consult_lists.html')

@login_required(login_url='/login/')
def report_CyC(request):
    return render(request, 'report_C&C.html')

@login_required(login_url='/login/')
def addList(request):
    return render(request, 'addList.html')