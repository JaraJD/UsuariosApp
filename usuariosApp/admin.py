from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.familiar import Familiar
from .models.medico import Medico

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Familiar)
admin.site.register(Medico)

# Register your models here.
