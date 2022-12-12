from django.contrib import admin
from users.models import Tokenstable, User

# Register your models here.
admin.site.register(User)
admin.site.register(Tokenstable)
