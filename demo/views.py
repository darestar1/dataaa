from django.shortcuts import render, redirect, get_object_or_404
from .models import Observation, Rock, Stream, Soil, OreMicroscopy, Petrograph, XRD, FluidInclusion
from .forms import ObservationForm, RockForm, StreamForm, SoilForm, OreMicroscopyForm, PetrographForm, XRDForm, FluidInclusionForm
from django.urls import reverse

# Tüm gözlemleri listeleme
from django.db.models import Q
# Yeni bir gözlem oluşturma


from django.shortcuts import render, redirect
from .models import Observation
from .forms import ObservationForm

def observation_create(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('observation_list')  # Gözlem listesine yönlendirme
    else:
        form = ObservationForm()
    
    return render(request, 'observation_create.html', {'form': form})

from django.shortcuts import render
from .models import Observation  # Import the Observation model

from django.db.models import Q

from django.db.models import Q

def observation_list(request):
    search_query = request.GET.get('search')
    observations = Observation.objects.all()

    if search_query:
        observations = observations.filter(
            Q(Phase__icontains=search_query) |
            Q(ClientName__icontains=search_query) |
            Q(City__icontains=search_query) |
            Q(Village__icontains=search_query) |
            Q(ER_No__icontains=search_query) |
            Q(Licence_No__icontains=search_query) |
            Q(ObservationID__icontains=search_query) |
            Q(SackNo__icontains=search_query) |
            Q(SampleNo__icontains=search_query) |
            Q(Date__icontains=search_query) |
            Q(SampleType__icontains=search_query) |
            Q(AnalysisType1__icontains=search_query) |
            Q(AnalysisType2__icontains=search_query) |
            Q(Projection__icontains=search_query) |
            Q(UTMZone__icontains=search_query) |
            Q(EastingM__icontains=search_query) |
            Q(NorthingM__icontains=search_query) |
            Q(ElevationM__icontains=search_query) |
            Q(Geologist1__icontains=search_query) |
            Q(Geologist2__icontains=search_query) |
            Q(RockType__icontains=search_query) |
            Q(RockTypeCode__icontains=search_query) |
            Q(Description__icontains=search_query)
        )

    return render(request, 'observation_list.html', {'observations': observations})







def observation_update(request, observation_id):
    observation = get_object_or_404(Observation, id=observation_id)
    search_query = request.GET.get('search')
    

    if search_query:
        observations = observations.filter(
            Q(Phase__icontains=search_query) |
            Q(ClientName__icontains=search_query) |
            Q(City__icontains=search_query) |
            Q(Village__icontains=search_query) |
            Q(ER_No__icontains=search_query) |
            Q(Licence_No__icontains=search_query) |
            Q(ObservationID__icontains=search_query) |
            Q(SackNo__icontains=search_query) |
            Q(SampleNo__icontains=search_query) |
            Q(Date__icontains=search_query) |
            Q(SampleType__icontains=search_query) |
            Q(AnalysisType1__icontains=search_query) |
            Q(AnalysisType2__icontains=search_query) |
            Q(Projection__icontains=search_query) |
            Q(UTMZone__icontains=search_query) |
            Q(EastingM__icontains=search_query) |
            Q(NorthingM__icontains=search_query) |
            Q(ElevationM__icontains=search_query) |
            Q(Geologist1__icontains=search_query) |
            Q(Geologist2__icontains=search_query) |
            Q(RockType__icontains=search_query) |
            Q(RockTypeCode__icontains=search_query) |
            Q(Description__icontains=search_query)
        )
    if request.method == 'POST':
        form = ObservationForm(request.POST, instance=observation)
        if form.is_valid():
            form.save()
            return redirect('observation_list')  # Redirect to the observation list after updating
    else:
        form = ObservationForm(instance=observation)

    return render(request, 'observation_update.html', {'form': form, 'observation': observation})


    

def observation_list_readonly(request):
    observations = Observation.objects.all()
    search_query = request.GET.get('search')
    

    if search_query:
        observations = observations.filter(
            Q(Phase__icontains=search_query) |
            Q(ClientName__icontains=search_query) |
            Q(City__icontains=search_query) |
            Q(Village__icontains=search_query) |
            Q(ER_No__icontains=search_query) |
            Q(Licence_No__icontains=search_query) |
            Q(ObservationID__icontains=search_query) |
            Q(SackNo__icontains=search_query) |
            Q(SampleNo__icontains=search_query) |
            Q(Date__icontains=search_query) |
            Q(SampleType__icontains=search_query) |
            Q(AnalysisType1__icontains=search_query) |
            Q(AnalysisType2__icontains=search_query) |
            Q(Projection__icontains=search_query) |
            Q(UTMZone__icontains=search_query) |
            Q(EastingM__icontains=search_query) |
            Q(NorthingM__icontains=search_query) |
            Q(ElevationM__icontains=search_query) |
            Q(Geologist1__icontains=search_query) |
            Q(Geologist2__icontains=search_query) |
            Q(RockType__icontains=search_query) |
            Q(RockTypeCode__icontains=search_query) |
            Q(Description__icontains=search_query)
        )
    return render(request, 'observation_list_readonly.html', {'observations': observations})



# Belirli bir gözlemi silme

def home(request):
    return render(request, 'home.html')
def delete_observation(request):
    if request.method == 'POST':
        observation_id = request.POST.get('observation')
        observation = Observation.objects.get(id=observation_id)
        observation.delete()
        return redirect('observation_list')
    
    observations = Observation.objects.all()
    return render(request, 'observation_delete.html', {'observations': observations})







# Rock modeli için işlevler
def rock_list_read(request):
    rocks = Rock.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        rocks = rocks.filter(
        Q(ClientName__icontains=search_query) |
        Q(City__icontains=search_query) |
        Q(Village__icontains=search_query) |
        Q(ER_No__icontains=search_query) |
        Q(Licence_No__icontains=search_query) |
        Q(ObservationID__icontains=search_query) |
        Q(SampleNo__icontains=search_query) |  # Update field name to 'SampleNo'
        Q(Date__icontains=search_query) |
        Q(SampleType__icontains=search_query) |
        Q(AnalysisType1__icontains=search_query) |
        Q(AnalysisType2__icontains=search_query) |
        Q(Projection__icontains=search_query) |
        Q(UTMZone__icontains=search_query) |
        Q(EastingM__icontains=search_query) |
        Q(NorthingM__icontains=search_query) |
        Q(ElevationM__icontains=search_query) |
        Q(Geologist1__icontains=search_query) |
        Q(Geologist2__icontains=search_query) |
        Q(RockType__icontains=search_query) |
        Q(RockTypeCode__icontains=search_query) |
        Q(Description__icontains=search_query)
    )
    return render(request, 'rock_list_read.html', {'rocks': rocks})
def rock_list(request):
    search_query = request.GET.get('search')
    rocks = Rock.objects.all()
    if search_query:
        rocks = rocks.filter(
            Q(ClientName__icontains=search_query) |
            Q(City__icontains=search_query) |
            Q(Village__icontains=search_query) |
            Q(ER_No__icontains=search_query) |
            Q(Licence_No__icontains=search_query) |
            Q(ObservationID__icontains=search_query) |
            Q(SackNo__icontains=search_query) |
            Q(SampleNo__icontains=search_query) |
            Q(Date__icontains=search_query) |
            Q(SampleType__icontains=search_query) |
            Q(AnalysisType1__icontains=search_query) |
            Q(AnalysisType2__icontains=search_query) |
            Q(Projection__icontains=search_query) |
            Q(UTMZone__icontains=search_query) |
            Q(EastingM__icontains=search_query) |
            Q(NorthingM__icontains=search_query) |
            Q(ElevationM__icontains=search_query) |
            Q(Geologist1__icontains=search_query) |
            Q(Geologist2__icontains=search_query) |
            Q(RockType__icontains=search_query) |
            Q(RockTypeCode__icontains=search_query) |
            Q(Description__icontains=search_query)
        )


    return render(request, 'rock_list.html', {'rocks': rocks})
    

def rock_create(request):
    if request.method == 'POST':
        form = RockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rock_list')
    else:
        form = RockForm()
    return render(request, 'rock_form.html', {'form': form})



# Existing views for list and create are kept as is




def rock_update(request, rock_id):
    rock = get_object_or_404(Rock, id=rock_id)

    if request.method == 'POST':
        form = RockForm(request.POST, instance=rock)
        if form.is_valid():
            form.save()
            return redirect('rock_list')  # Rock güncellendikten sonra rock listesine yönlendir
    else:
        form = RockForm(instance=rock)

    return render(request, 'rock_update.html', {'form': form, 'rock': rock})





def delete_rock(request):
    if request.method == 'POST':
        rock_id = request.POST.get('rock')
        rock = Rock.objects.get(id=rock_id)
        rock.delete()
        return redirect('rock_list')

    rocks = Rock.objects.all()
    return render(request, 'rock_delete.html', {'rocks': rocks})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Stream
from .forms import StreamForm

def stream_list_read(request):
    streams = Stream.objects.all()
    return render(request, 'stream_list_read.html', {'streams': streams})

def stream_list(request):
    streams = Stream.objects.all()
    return render(request, 'stream_list.html', {'streams': streams})

def stream_create(request):
    if request.method == 'POST':
        form = StreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stream_list')
    else:
        form = StreamForm()
    return render(request, 'stream_form.html', {'form': form})

def stream_update(request, stream_id):
    stream = get_object_or_404(Stream, id=stream_id)

    if request.method == 'POST':
        form = StreamForm(request.POST, instance=stream)
        if form.is_valid():
            form.save()
            return redirect('stream_list')
    else:
        form = StreamForm(instance=stream)

    return render(request, 'stream_update.html', {'form': form, 'stream': stream})

def delete_stream(request):
    if request.method == 'POST':
        stream_id = request.POST.get('stream')
        stream = Stream.objects.get(id=stream_id)
        stream.delete()
        return redirect('stream_list')

    streams = Stream.objects.all()
    return render(request, 'stream_delete.html', {'streams': streams})


# Soil modeli için görünümler
def soil_list_read(request):
    soils = Soil.objects.all()
    return render(request, 'soil_list_read.html', {'soils': soils})
def soil_list(request):
    soils = Soil.objects.all()
    return render(request, 'soil_list.html', {'soils': soils})

def soil_create(request):
    if request.method == 'POST':
        form = SoilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('soil_list')
    else:
        form = SoilForm()
    return render(request, 'soil_form.html', {'form': form})



def soil_update(request, soil_id):
    soil = get_object_or_404(Soil, id=soil_id)

    if request.method == 'POST':
        form = SoilForm(request.POST, instance=soil)
        if form.is_valid():
            form.save()
            return redirect('soil_list')
    else:
        form = SoilForm(instance=soil)

    return render(request, 'soil_update.html', {'form': form, 'soil': soil})


def soil_delete(request, pk):
    soil = get_object_or_404(Soil, pk=pk)
    if request.method == 'POST':
        soil.delete()
        return redirect('soil_list')
    return render(request, 'soil_confirm_delete.html', {'soil': soil})
def ore_microscopy_list_read(request):
    ore_microscopy_data = OreMicroscopy.objects.all()
    return render(request, 'ore_microscopy_list_read.html', {'ore_microscopy_data': ore_microscopy_data})

def ore_microscopy_list(request):
    ore_microscopy_data = OreMicroscopy.objects.all()
    return render(request, 'ore_microscopy_list.html', {'ore_microscopy_data': ore_microscopy_data})

def ore_microscopy_create(request):
    if request.method == 'POST':
        form = OreMicroscopyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ore_microscopy_list')
    else:
        form = OreMicroscopyForm()
    return render(request, 'ore_microscopy_form.html', {'form': form})

def ore_microscopy_update(request, ore_microscopy_id):
    ore_microscopy = get_object_or_404(OreMicroscopy, id=ore_microscopy_id)

    if request.method == 'POST':
        form = OreMicroscopyForm(request.POST, instance=ore_microscopy)
        if form.is_valid():
            form.save()
            return redirect('ore_microscopy_list')
    else:
        form = OreMicroscopyForm(instance=ore_microscopy)

    return render(request, 'ore_microscopy_update.html', {'form': form, 'ore_microscopy': ore_microscopy})


def ore_microscopy_delete(request, pk):
    ore_microscopy = get_object_or_404(OreMicroscopy, pk=pk)
    
    if request.method == 'POST':
        ore_microscopy.delete()
        return redirect('ore_microscopy_list')  # Silme işlemi tamamlandığında liste sayfasına yönlendirme
    
    return render(request, 'ore_microscopy_confirm_delete.html', {'ore_microscopy': ore_microscopy})

# Petrograph modeli için görünümler
def petrograph_list(request):
    petrographs = Petrograph.objects.all()
    return render(request, 'petrograph_list.html', {'petrographs': petrographs})

def petrograph_create(request):
    if request.method == 'POST':
        form = PetrographForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('petrograph_list')
    else:
        form = PetrographForm()
    return render(request, 'petrograph_form.html', {'form': form})

def petrograph_update(request, pk):
    petrograph = get_object_or_404(Petrograph, pk=pk)
    if request.method == 'POST':
        form = PetrographForm(request.POST, instance=petrograph)
        if form.is_valid():
            form.save()
            return redirect('petrograph_list')
    else:
        form = PetrographForm(instance=petrograph)
    return render(request, 'petrograph_form.html', {'form': form})

def petrograph_delete(request, pk):
    petrograph = get_object_or_404(Petrograph, pk=pk)
    if request.method == 'POST':
        petrograph.delete()
        return redirect('petrograph_list')
    return render(request, 'petrograph_confirm_delete.html', {'petrograph': petrograph})

# XRD modeli için görünümler
def xrd_list(request):
    xrds = XRD.objects.all()
    return render(request, 'xrd_list.html', {'xrds': xrds})

def xrd_create(request):
    if request.method == 'POST':
        form = XRDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('xrd_list')
    else:
        form = XRDForm()
    return render(request, 'xrd_form.html', {'form': form})

def xrd_update(request, pk):
    xrd = get_object_or_404(XRD, pk=pk)
    if request.method == 'POST':
        form = XRDForm(request.POST, instance=xrd)
        if form.is_valid():
            form.save()
            return redirect('xrd_list')
    else:
        form = XRDForm(instance=xrd)
    return render(request, 'xrd_form.html', {'form': form})

def xrd_delete(request, pk):
    xrd = get_object_or_404(XRD, pk=pk)
    if request.method == 'POST':
        xrd.delete()
        return redirect('xrd_list')
    return render(request, 'xrd_confirm_delete.html', {'xrd': xrd})

# FluidInclusion modeli için görünümler
def fluidinclusion_list(request):
    fluidinclusions = FluidInclusion.objects.all()
    return render(request, 'fluidinclusion_list.html', {'fluidinclusions': fluidinclusions})

def fluidinclusion_create(request):
    if request.method == 'POST':
        form = FluidInclusionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fluidinclusion_list')
    else:
        form = FluidInclusionForm()
    return render(request, 'fluidinclusion_form.html', {'form': form})

def fluidinclusion_update(request, pk):
    fluidinclusion = get_object_or_404(FluidInclusion, pk=pk)
    if request.method == 'POST':
        form = FluidInclusionForm(request.POST, instance=fluidinclusion)
        if form.is_valid():
            form.save()
            return redirect('fluidinclusion_list')
    else:
        form = FluidInclusionForm(instance=fluidinclusion)
    return render(request, 'fluidinclusion_form.html', {'form': form})

def fluidinclusion_delete(request, pk):
    fluidinclusion = get_object_or_404(FluidInclusion, pk=pk)
    if request.method == 'POST':
        fluidinclusion.delete()
        return redirect('fluidinclusion_list')
    return render(request, 'fluidinclusion_confirm_delete.html', {'fluidinclusion': fluidinclusion})