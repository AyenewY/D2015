from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Choice)
admin.site.register(models.Question)
admin.site.register(models.tce_answers)
admin.site.register(models.tce_modules)
admin.site.register(models.tce_questions)
admin.site.register(models.tce_sessions)
admin.site.register(models.tce_sslcerts)
admin.site.register(models.tce_subjects)
admin.site.register(models.tce_test_subject_set)
admin.site.register(models.tce_test_subjects)
admin.site.register(models.tce_testgroups)
admin.site.register(models.tce_tests)
admin.site.register(models.tce_tests_logs)
admin.site.register(models.tce_tests_logs_answers)
admin.site.register(models.tce_users)
admin.site.register(models.tce_testsslcerts)
admin.site.register(models.tce_testuser_stat)
admin.site.register(models.tce_tests_users)
admin.site.register(models.tce_user_groups)
admin.site.register(models.tce_usrgroups)
admin.site.register(models.course)
admin.site.register(models.taken)
admin.site.register(models.student)
admin.site.register(models.permanent_employee)
admin.site.register(models.Contract_employee)
admin.site.register(models.retired_employee)
admin.site.register(models.emp_collection)
'''
class TCEE_Users (admin.ModelAdmin):
    fields = ['user_name','user_firstname']

admin.site.register(tce_users, TCEE_Users)
'''

