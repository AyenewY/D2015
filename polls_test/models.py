from django.db import models
from django.db.models.functions import Length
import datetime
from django.utils import timezone, timesince
# Create your models here.

models.CharField.register_lookup(Length)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


'''
user session management models. For storing users model information......
'''
class tce_sessions (models.Model):
    cpsession_id=models.CharField(max_length=32, primary_key=True)
    cpsession_expiry = models.DateTimeField(null=False)
    cpsession_data = models.TextField (max_length=200, null=False)


'''
Users table for recording students/users data...... 
'''
class tce_users (models.Model):
    user_id = models.BigAutoField (
        primary_key=True, 
        auto_created=True
        )
    user_name = models.CharField(
        max_length=255,
    unique=True, 
    null=False
    )
    user_password = models.CharField(
        max_length=255,
        null=False,
        
    )
    user_email = models.CharField(
        max_length=255
    )
    user_regdate = models.DateTimeField(
        null=False
        )
    user_ip = models.CharField (
        max_length=40,
        default='',
        blank=True
    )
    user_firstname = models.CharField(
        max_length=255
    )
    user_lastname = models.CharField(
        max_length=255
    )
    user_birthdate = models.DateField()
    user_birthplace = models.CharField(
        max_length=255,
        blank=True
    )
    user_regnumber = models.CharField(
        max_length=255,
        unique=True
    )
    user_ssn = models.CharField(
        max_length=255,
        unique=True,
        blank=True
    )
    user_level = models.SmallIntegerField(
        null=False
    )
    user_verifycode  = models.CharField (
        unique=True,
        default='',
        max_length=255,
        blank= True
    )
    user_otpkey  = models.CharField(
        max_length=255,
        default='',
        blank= True
    )

    def age_verfier(self):
        if self.user_birthdate>=timezone.now()-datetime.timedelta(years=18):
            return self.user_birthdate
    def __str__(self):
        return self.user_name
    
    #models.CharField.register_lookup(Length)

    class Meta:
        constraints = [
            models.CheckConstraint(
            check=models.Q(user_password__length__gte = 8),
            name= "tce_users_length", 
            )
        ]

'''
Module detail information for the exit system.....
'''
class tce_modules(models.Model):
    module_id  = models.BigAutoField(
        primary_key=True,
        null=False
    )
    module_name  = models.CharField(
        max_length=255,
        null=False,
        unique=True,
        default='CSE'
    )
    module_enabled  = models.BooleanField(
        default=False,
        null=False
    )
    module_user_id  = models.ForeignKey(
        tce_users,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.module_name

'''
Table for recording the subjects.......
'''
class tce_subjects (models.Model):
    subject_id  = models.BigAutoField(
        primary_key=True,
        null=False,
    )
    subject_module_id   = models.ForeignKey(
        tce_modules,
        on_delete=models.CASCADE,
        null=False,
        unique=False,
        default=1
    )
    subject_name   =  models.CharField(
        max_length=255,
        null=False,
        unique=True
    )
    subject_description = models.TextField(
        default='',
        blank=True
    )
    subject_enabled   =  models.BooleanField(
        default=False
    )
    subject_user_id   =  models.ForeignKey(
        tce_users, 
        on_delete=models.CASCADE,
        null=False,
        default=1
    )

    def __str__(self):
        return self.subject_name
'''
The questions table to store information related to questions 
in the exam database.
'''
class tce_questions (models.Model):
    question_id = models.BigAutoField(
        primary_key=True,
        null=False
    )
    question_subject_id = models.ForeignKey(
        tce_subjects,
        null=False,
        on_delete=models.CASCADE
    )
    question_description = models.TextField(
        null=False,
        blank=True
    )
    question_explanation = models.TextField(
        null=True,
        default= 'null',
        blank=True
    )
    question_type = models.SmallIntegerField(
        null=False,
        default=1
    )
    question_difficulty = models.SmallIntegerField(
        null=False,
        default=1
    )
    question_enabled = models.BooleanField(
        null=False,
        default=0
    )
    question_position  = models.BigIntegerField(
        default=0
    )
    question_timer  = models.SmallIntegerField(
        default=0
    )
    question_fullscreen  = models.BooleanField(
        default=False
    )
    question_inline_answers  = models.BooleanField(
        default=0
    )
    question_auto_next  = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.question_description

'''
The answers table to store information related to answers 
in the exam database.
'''
class tce_answers (models.Model):
    answer_id = models.BigAutoField(
        primary_key= True
    )
    answer_question_id = models.ForeignKey( 
        tce_questions,
        on_delete=models.CASCADE,
        null=False
    )
    answer_description = models.TextField(
        null=True,
        max_length=500,
        blank=True
    )
    answer_explanation = models.TextField(
        null=True,
        blank=True
    )
    answer_isright = models.BooleanField(
        default= 0
    )
    answer_enabled = models.BooleanField(
        default=0
    )
    answer_position = models.BigIntegerField (
        null=True
    )
    answer_keyboard_key = models.SmallIntegerField(
        null= True
    )

    def __str__(self):
        return self.answer_description
'''
Tests table for recording test related information in the database
'''
class tce_tests (models.Model):
    testRepeatable = models.IntegerChoices (
        'TestRepeat', "1 2 3 4 5 6 7 8 9 10"
        )
    test_id = models.BigAutoField(
        primary_key=True,
        null= False
    )
    test_name = models.CharField(
        "Exit exam Test Name",
        max_length=255,
        null=False,
        unique=True
    )
    test_description = models.TextField(
        null=False,
        blank=True
    )
    test_begin_time = models.DateTimeField(
        default=''
    )
    test_end_time = models.DateTimeField(
        null=False
    )
    test_duration_time = models.SmallIntegerField(
        null=False,
        default=0
    )
    test_ip_range = models.CharField(
        max_length=255,
        null=False,
        default="*.*.*.*",
        blank=True
    )
    test_results_to_users = models.BooleanField(
        default=False,
        null=False
    )
    test_report_to_users = models.BooleanField(
        null=False,
        default=False
    )
    test_score_right = models.SmallIntegerField (
        default=1
    )
    test_score_wrong =models.SmallIntegerField(
        default=0
    )
    test_score_unanswered = models.SmallIntegerField(
        default=0
    )
    test_max_score = models.SmallIntegerField(
        null=False,
        default=0
    )
    test_user_id = models.ForeignKey (
        tce_users,
        on_delete=models.CASCADE,
        null=False,
        default=1
    )
    test_score_threshold = models.SmallIntegerField(
        default=0
    )
    test_random_questions_select = models.BooleanField(
        default=True,
        null=False
    )
    test_random_questions_order = models.BooleanField(
        default= True,
        null=False
    )
    test_questions_order_mode = models.SmallIntegerField(
        null=False,
        default=0
    )
    test_comment_enabled = models.BooleanField(
        null=False,
        default=True
    )
    test_menu_enabled = models.BooleanField(
        null=False,
        default=True
    )
    test_noanswer_enabled = models.BooleanField(
        null=False,
        default=True
    )
    test_mcma_enabled = models.BooleanField(
        null=False,
        default=True
    )
    test_repeatable = models.SmallIntegerField(
        default=0,
        choices=testRepeatable.choices,
        null=False
    )
    test_mcma_partial_score = models.BooleanField(
        null=False,
        default=True
    )
    test_logout_on_timeout = models.BooleanField(
        default=False,
        null=False
    )
    test_password = models.CharField(
        max_length=255,
        null=True,
        default='',
        blank=True
    )

    def __str__(self):
        return self.test_name
    
    #models.CharField.register_lookup(Length)

    class Meta:
        constraints = [
            models.CheckConstraint(
            check=models.Q(test_password__length__gte = 8),
            name= "tce_test_length", 
            )
        ]
'''
A table used to record a test subject relationship information. 
'''
class tce_test_subject_set (models.Model):
    Test_difficulty =[
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    ]
    tsubset_id = models.BigAutoField(
        primary_key=True,
        null=False
    )
    tsubset_test_id = models.ForeignKey(
        tce_tests,
        on_delete=models.CASCADE,
        null=False
    )
    tsubset_type = models.SmallIntegerField(
        null=False,
        default=1
    )
    tsubset_difficulty = models.SmallIntegerField(
        choices=Test_difficulty
    )
    tsubset_quantity = models.SmallIntegerField(
        null=False,
        default=1
    )
    tsubset_answers = models.SmallIntegerField(
        null=False,
        default=0
    )

    def __str__(self):
        return self.tsubset_id

''' 
A table used to record test subject related information
'''
class tce_test_subjects (models.Model):
    subjset_tsubset_id = models.ForeignKey(
        tce_test_subject_set,
        on_delete=models.CASCADE,
        null=False
    )
    subjset_subject_id =models.ForeignKey(
        tce_subjects,
        on_delete=models.CASCADE,
        null=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['subjset_tsubset_id', 'subjset_subject_id'], name ='tests_subjects'
            )
        ]
    

'''
A table used to record test user relationship information. 
'''
class tce_tests_users(models.Model):
    testuser_id = models.BigAutoField(
        primary_key=True,
        null=False
    )
    testuser_test_id = models.OneToOneField(
        tce_tests,
        unique=True,
        null=False,
        on_delete=models.CASCADE
    )
    testuser_user_id = models.OneToOneField(
        tce_users,
        unique=True,
        null=False,
        on_delete=models.CASCADE
    )
    testuser_status = models.SmallIntegerField(
        unique=True,
        null=False,
        default=0
    )
    testuser_creation_time = models.DateTimeField(
        null=False
    )
    testuser_comment = models.TextField(
        default='',
        blank= True
    )

'''
It record test set for users ........

class tce_tests_users (models.Model):
    testuser_id = models.BigAutoField(
        primary_key=True,
        null=False
    )
    testuser_test_id = models.OneToOneField(
        tce_tests,
        on_delete=models.CASCADE,
        unique=True,
        null=False
    )
    testuser_user_id = models.OneToOneField(
        tce_users,
        on_delete=models.CASCADE,
        unique=True,
        null=False
    )
    testuser_status = models.SmallIntegerField(
        unique=True,
        null=False,
        default=0
    )
    testuser_creation_time = models.DateTimeField(
        null=False
    )

    testuser_comment =models.TextField(
        null=True
    )
'''
'''
Test log information table 
'''
class tce_tests_logs (models.Model):
    testlog_id = models.BigIntegerField(
        primary_key=True,
        null=False
    )
    testlog_testuser_id = models.OneToOneField(
        tce_tests_users,
        on_delete=models.CASCADE,
        null=False,
        unique=True
    )
    testlog_user_ip = models.CharField(
        null=True,
        max_length=39
    )
    testlog_question_id = models.OneToOneField  (
        tce_questions,
        on_delete= models.CASCADE,
        unique=True,
        null=False
    )
    testlog_answer_text = models.TextField(
        default=''
    )
    testlog_score = models.IntegerField(
        default=0
    )
    testlog_creation_time =models.DateTimeField(
        default= ''
    )
    testlog_display_time =models.DateTimeField(
        default= ''
    )
    testlog_change_time =models.DateTimeField(
        default= ''
    )
    testlog_reaction_time =models.BigIntegerField(
        default= 0
    )
    testlog_order = models.SmallIntegerField(
        default=1
    )
    testlog_num_answers = models.SmallIntegerField(
        default=0
    )
    testlog_comment = models.TextField(
        null=True
    )

'''
 Recording exam log files for answer
 '''
class tce_tests_logs_answers (models.Model):
    logansw_testlog_id = models.ForeignKey(
        tce_tests_logs,
        null=False,
        on_delete=models.CASCADE
    )
    logansw_answer_id = models.ForeignKey(
        tce_answers,
        null=False,
        on_delete=models.CASCADE
    )
    logansw_selected = models.SmallIntegerField(
        null=False,
        default=-1
    )
    logansw_order = models.SmallIntegerField(
        null=False,
        default=1
    )
    logansw_position = models.BigIntegerField(
        null=True
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['logansw_testlog_id', 'logansw_answer_id'], name ='tests_logs_answers'
            )
        ]

'''
User group infrmation table
'''
class tce_user_groups(models.Model):
    group_id =models.BigAutoField(
        primary_key=True,
        null=False
    )
    group_name = models.CharField(
        max_length=255,
        null=False,
        unique=True
    )

'''
A table records a users assigned group information.
'''
class tce_usrgroups (models.Model):
    usrgrp_user_id = models.ForeignKey(
        tce_users,
        on_delete=  models.CASCADE,
        null=False
    )
    usrgrp_group_id = models.ForeignKey(
        tce_user_groups,
        on_delete=  models.CASCADE,
        null=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['usrgrp_user_id', 'usrgrp_group_id'], name ='usersgroup'
            )
        ]

'''
Test group information table. 
'''
class tce_testgroups (models.Model):
    tstgrp_test_id =models.ForeignKey(
        tce_tests,
        null=False,
        on_delete=models.CASCADE
    )
    tstgrp_group_id =models.ForeignKey(
        tce_user_groups,
        null=False,
        on_delete=models.CASCADE
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['tstgrp_test_id', 'tstgrp_group_id'], name ='testgroups'
            )
        ]
    
'''
User test statistics information recording table.  
'''
class tce_testuser_stat(models.Model):
    tus_id = models.BigAutoField(
        primary_key=True,
        null=False
    )
    tus_date = models.DateTimeField(
        null=False
    )

''' 
SSL certificate information table......
'''

class  tce_sslcerts (models.Model):
    ssl_id = models.BigAutoField(
        primary_key=True,
        null=False
    )
    ssl_name = models.CharField(
        null=False,
        max_length=255, 
    )
    ssl_hash = models.CharField(
        max_length=255,
        null=False
    )
    ssl_end_date = models.DateTimeField(
        null=False
    )
    ssl_user_id = models.BigIntegerField(
        null=False,
        default=1
    )

'''
A table use to record tests ssl certificate infromation 
'''
class tce_testsslcerts(models.Model):
    tstssl_test_id = models.ForeignKey(
        tce_tests,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Test SSl configuration"
    )
    tstssl_ssl_id = models.ForeignKey(
        tce_sslcerts,
        on_delete=models.CASCADE,
        null=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['tstssl_test_id', 'tstssl_ssl_id'], name ='testsslinfo'
            )
        ]


#sample many to many relation

class student (models.Model):
    student_Id = models.CharField(
        max_length=100,
        primary_key=True,
    )
    student_fullname = models.CharField(
        "Student Name",
        max_length=100,
        null=False,
        blank=False,
    )
    student_Department =models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.student_fullname

class course (models.Model):
    course_Id = models.CharField(
        max_length=50,
        primary_key=True
    )
    course_Name = models.CharField(
        null=False,
        blank=False,
        max_length=100
    )
    course_description = models.TextField(
        null=False,
        blank=True
    )
    student_Id = models.ManyToManyField(
        student,
        through="Taken"
    )

    def __str__(self):
        return self.course_Id

class taken (models.Model):
    choice_semester = models.IntegerChoices(
        "choice_semester" , "1 2 3"
    )
    taken_semester = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
        choices=choice_semester.choices
    )
    taken_year = models.PositiveIntegerField(
        "Academic Year",
        null=False,
        blank=False,
        default=2023
    )
    student_Id = models.ForeignKey(
        student,
        on_delete=models.CASCADE
    )
    course_Id = models.ForeignKey(
        course,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['taken_semester', 'taken_year','student_Id','course_Id'], name ='crsstsID'
            )
        ]
    def __str__(self):
        return str(self.taken_semester)