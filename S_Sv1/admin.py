from django.contrib import admin
from S_Sv1.models import Person


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
