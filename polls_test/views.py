from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *
from django.views import generic
from django.urls import reverse
from django.contrib.postgres import *
from django.db import transaction, IntegrityError, connection
import time

def index(user_id):
    with transaction.atomic():
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
        user = tce_users.objects.filter(user_name=user_id).only(
            'user_password','user_email','user_level'
        )
        result={"user":user}
        return render (request,"user_reg.html",result)
    except Exception as e:
        print ("Error handled here....")

def emp_result(emp_id):
    try:

        with transaction.atomic():
            employee_res = Contract_employee.objects.all().values(
            'employee_name','employee_id','duration_month','allowance',
            'employee_salary', 'employee_age').filter(employee_name__icontains = 'man')
            result = {"employee":employee_res}
            return render(emp_id,"test.html",result)
    except IntegrityError as e:
        #print(e.__str__)
        handle_exception()
    except Exception:
        handle_exception()
    finally:
        transaction.on_commit(handle_exception2)

@transaction.atomic
def per_result(emp_id):
    employee_res = permanent_employee.per.all().values(
    'employee_name','employee_id','employee_salary', 'employee_age')
    result_per = {"emp":employee_res}
    return render(emp_id,"test.html",result_per)

def handle_exception():
    print ('''Error is happen in the program. 
           Please check your codes....''')

def handle_exception2():
    print ('''The transaction committed successfully. 
           Your code is okay....''')

class QueryLogger:
    def __init__(self):
        self.queries = []

    def __call__(self, execute, sql, params, many, context):
        current_query = {"sql": sql, "params": params, "many": many}
        start = time.monotonic()
        try:
            result = execute(sql, params, many, context)
        except Exception as e:
            current_query["status"] = "error"
            current_query["exception"] = e
            raise
        else:
            current_query["status"] = "ok"
            return result
        finally:
            duration = time.monotonic() - start
            current_query["duration"] = duration
            self.queries.append(current_query)

# ql = QueryLogger()
# user_id =10
# with connection.execute_wrapper(ql):
#     index(user_id)
# # Now we can print the log.
# print(ql.queries)