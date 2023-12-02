from django.contrib import admin

# Register your models here.
from .models import company
admin.site.register(company)
from .models import jop
admin.site.register(jop)
from .models import Applicant
admin.site.register(Applicant)
from .models import skils
admin.site.register(skils)
from .models import education
admin.site.register(education)
from .models import department
admin.site.register(department)