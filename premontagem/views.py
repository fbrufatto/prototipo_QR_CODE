from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import AddBicicletaForm
from .models import Bike


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_bikes = Bike.objects.all().count()

    context = {
        'num_bike': num_bikes,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def add_bike(request):
    form = AddBicicletaForm()
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddBicicletaForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            form.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('bike_info', args=[form.cleaned_data['nquadro']]))

    context = {
        "form": form
    }
    return render(request, "add_bike.html", context)


def qr_code_bike(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    context = {"bike": request.build_absolute_uri(reverse('bike_info', args=[bike.nquadro]))}
    return render(request, 'qr_code_bike.html', context)


def bike_info(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    context = {"bike": bike}
    return render(request, 'info_bike.html', context)
