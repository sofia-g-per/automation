from django.shortcuts import render, redirect
from .models import HostGroup, Host, Script, ScriptResult
from .forms import HostForm
from .viewHelpers import search
from .modelSearchMethods import searchHostGroups, searchHosts, searchScripts, searchScriptResults
# главная страница
def index(request):
    
    hosts = search(request, 's', '', searchHosts, Host)
    hostGroups = search(request, 'sg', '', searchHostGroups, HostGroup)
    for group in hostGroups:
        group.hosts = group.host_set.all()

    scripts = search(request, 'ss', '', searchScripts,  Script)
    scriptResults = search(request, 'ssr', 'sort-s', searchScriptResults,  ScriptResult)
    userLog = search(request, 'su', 'sort-u', searchScriptResults,  ScriptResult)

    context = {
        "hosts": hosts,
        "hostGroups": hostGroups,
        "scripts": scripts,
        "userLog": userLog,
        "scriptResults": scriptResults
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
        form = HostForm(request.POST)

        if(form.is_valid()):
            form.save()
            return redirect(index)

        else:
            context["form"] = form
        
    return render(request, "create_host.html", context)

# удаление хостов
def deleteHosts(request):
    print(request.GET)
    if(request.GET['deleteHosts']):
        ids = [int(id) for id in request.GET['deleteHosts']]
    print(ids)
    Host.objects.filter(id__in=ids).delete()

    return redirect(index)

