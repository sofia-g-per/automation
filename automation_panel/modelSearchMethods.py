from .models import Host, HostGroup, Script, ScriptResult, UserLog
from django.contrib.postgres.search import SearchVector

def searchHosts(query):
    return Host.objects.annotate(searchV=SearchVector("name", "network_name", "ip", "hardware"),).filter(searchV=query)

def searchHostGroups(query):
    # return  HostGroup.objects.annotate(searchV=SearchVector("name", "host__name", "host__network_name", "host__ip", "host__hardware"),).filter(searchV=query)
    return HostGroup.objects.annotate(searchV=SearchVector("name"),).filter(searchV=query)

def searchScripts(query):
    return Script.objects.annotate(searchV=SearchVector("name"),).filter(searchV=query)

def searchScriptResults(query, sortField=''):
    if(sortField):
        return ScriptResult.objects.annotate(searchV=SearchVector("script__name", "result", "run_for__group"),).filter(searchV=query).order_by(sortField)
    else:
        return ScriptResult.objects.annotate(searchV=SearchVector("script__name", "result", "run_for__group"),).filter(searchV=query)
    
def searchUserLogs(query, sortField=''):
    if(sortField):
        return UserLog.objects.annotate(searchV=SearchVector("script__name", "result", "run_for__group"),).filter(searchV=query).order_by(sortField)
    else:
        return UserLog.objects.annotate(searchV=SearchVector("user__name", "action_description"),).filter(searchV=query)
