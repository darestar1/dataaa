

# Register your models here.
from django.contrib import admin
from .models import Observation, Rock, Stream, Soil, OreMicroscopy, Petrograph, XRD, FluidInclusion

admin.site.register(Observation)
admin.site.register(Rock)
admin.site.register(Stream)
admin.site.register(Soil)
admin.site.register(OreMicroscopy)
admin.site.register(Petrograph)
admin.site.register(XRD)
admin.site.register(FluidInclusion)
