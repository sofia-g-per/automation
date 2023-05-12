from django.db import models
from django.contrib.auth.models import User

class HostGroup(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Host(models.Model):
    name =  models.CharField(max_length=200, null=False, blank=False)
    ip = models.CharField(max_length=15, null=False)
    group = models.ForeignKey(HostGroup, on_delete = models.SET_NULL, blank=True, null=True)
    network_name = models.CharField(max_length=200, null=False, blank=False)
    hardware = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Script(models.Model):
    name  = models.CharField(max_length=100)
    creation_date = models.DateField(auto_now_add=True)
    version = models.CharField(max_length=50)
    size= models.IntegerField()
    file_type=models.CharField(max_length=100)
    path=models.CharField(max_length=225)
    description= models.CharField(max_length=200)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class ScriptResult(models.Model):
    script = models.ForeignKey(Script, on_delete = models.SET_NULL, blank=True, null=True)
    run_date = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=200)
    run_for = models.ForeignKey(Host, on_delete = models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.script.name} {self.run_date} {self.result}'

class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, blank=True, null=True)
    action_date = models.DateTimeField(auto_now_add=True)
    action_description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.username} {self.action_date} {self.action_description}'


