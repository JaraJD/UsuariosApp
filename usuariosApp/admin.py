from django.contrib import admin
from .models.user import User
from .models.familiar import Familiar
from .models.medico import Medico

admin.site.register(User)
admin.site.register(Familiar)
admin.site.register(Medico)

