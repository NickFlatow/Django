from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)
#add another class to admin.py:
#from django.contrib import admin
#from .models import Question
#admin.site.register(Question)
#add another class to admin.py:


#test comment
#other test comment
