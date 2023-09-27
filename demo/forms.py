from django import forms
from .models import Observation, Rock, Stream, Soil, OreMicroscopy, Petrograph, XRD, FluidInclusion

class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = '__all__'

class RockForm(forms.ModelForm):
    class Meta:
        model = Rock
        fields = '__all__'

class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = '__all__'

class SoilForm(forms.ModelForm):
    class Meta:
        model = Soil
        fields = '__all__'

class OreMicroscopyForm(forms.ModelForm):
    class Meta:
        model = OreMicroscopy
        fields = '__all__'

class PetrographForm(forms.ModelForm):
    class Meta:
        model = Petrograph
        fields = '__all__'

class XRDForm(forms.ModelForm):
    class Meta:
        model = XRD
        fields = '__all__'

class FluidInclusionForm(forms.ModelForm):
    class Meta:
        model = FluidInclusion
        fields = '__all__'
class ObservationUpdateForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = '__all__'  # Tüm alanları formda kullanmak için