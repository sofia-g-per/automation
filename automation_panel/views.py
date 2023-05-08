from django.shortcuts import render
from django.http import HttpResponse
from .models import HostGroup, Host
from .forms import HostForm

# главная страница
def index(request):
    hostGroups = HostGroup.objects.all()
    print(hostGroups[0].host_set)
    # currentGroupIndex = 0
    for group in hostGroups:
        group.hosts = group.host_set.all()
    context = {
        "hosts": hostGroups,
    }

    return render(request, "index.html" , context)

# страница создания хоста
def createHost(request):
    hostGroups = HostGroup.objects.all()
    context = {
        "hostGroups": hostGroups,
        "form": HostForm()
    }

    if(request.method == "POST"):
        print("post")
        form = HostForm(request.POST)

        if(form.is_valid()):
            form.save()
            return index(request)
        else:
            context["form"] = form
        
    print("form")
    print(context)
    return render(request, "create_host.html", context)