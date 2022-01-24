from email.mime import image
from django.contrib import admin
from .models import power,cpu,hard,MOTHERBOARD,fan,ram,etc,keybordandmouse,gpu


admin.site.register(gpu)
admin.site.register(cpu)
admin.site.register(power)
admin.site.register(hard)
admin.site.register(MOTHERBOARD)
admin.site.register(fan)
admin.site.register(ram)
admin.site.register(keybordandmouse)
admin.site.register(etc)
# Register your models here.
