from django.shortcuts import render
from .models import Tenant, Task
import random

string = "Please press shuffle"

def shuffle(request):
    global string
    high_tenants = []
    for item in Tenant.objects.filter(high_tenant=True):
        high_tenants.append(item.first_name)


    ground_tenants = []
    for item in Tenant.objects.filter(high_tenant=False):
        ground_tenants.append(item.first_name)

    random.shuffle(ground_tenants)

    tasks = []
    for item in Task.objects.all():
        tasks.append(item.task_name)

    string="Hello this is your automatic cleaning reminder, %s is assigned to %s & %s & %s, %s is assigned to %s and the %s is assigned to %s while %s goes to %s & %s, due date is the upcoming sunday evening. \n Toilet paper is bought by %s Have fun and Cheers! Python"%(tasks[0],ground_tenants[0],ground_tenants[1],ground_tenants[2],tasks[1],ground_tenants[3],tasks[3],ground_tenants[4],tasks[2],high_tenants[0], high_tenants[1], ground_tenants[0])

    context = {
        'string': string,
    }
    return render(request, 'app/index.html', context)

def index(request):
    global string

    context = {
        'string': string,
    }
    return render(request, 'app/index.html', context)
