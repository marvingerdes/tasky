from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Ticket

def tickets_detail(request, id):
	ticket = get_object_or_404(Ticket, id=int(id))
	return render(request, "details.html", {"ticket": ticket})

