from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *
from django.views import generic
from django.urls import reverse
def index(user_id):
    list_user =tce_users.objects.all()
    context = {"UserName":list_user}
    return render(user_id, "test.html", context)

def display(user_id):
    list_user_member =tce_usrgroups.objects.order_by("usrgrp_group_id")
    result = {"userMember":list_user_member}
    return render (user_id, "test.html",result)

def display_group (user_id):
    list_group = tce_user_groups.objects.order_by("group_id")
    result = {"userGroup":list_group}
    return render (user_id,'test.html',result)

def display_join(user_id):
    user =tce_user_groups.objects.filter(tce_usrgroups__usrgrp_group_id__group_name__contains ="",
                                         tce_usrgroups__usrgrp_user_id__user_name__contains ="").order_by("group_id")                                      
    result = {"user":user}
    return render(user_id,"test.html",result)

def user_reg(request, user_id):
    try:
        user = tce_users.objects.filter(user_name=user_id)
        result={"user":user}
        return render (request,"user_reg.html",result)
    except Exception as e:
        print (e)

