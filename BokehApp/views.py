from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from bokeh.plotting import figure
from bokeh.embed import components

# Create your views here.

def home(request):
	#create a plot
	plot = figure(width=400, height=400)
	# add a circle renderer with a size, color, and alpha
	plot.scatter([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="#4C1F7A", alpha=0.5)
	script, div = components(plot)
	return render(request, 'base.html', {'script': script, 'div': div})


