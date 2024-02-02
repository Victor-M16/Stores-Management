

# Create your views here.
#Choose Procurement Choice
#Manage Tendering Process
#Manage Contract Awarding
#Record the procurement process
#Compliance Monitoring



from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProcurementChoiceForm
from .models import ProcurementChoice
# views.py
from django.utils import timezone

from .models import RFQ, RFQbid
from .forms import RFQbidForm
from stock.models import *


def open_rfqs(request):
    open_rfqs = RFQ.objects.filter(closing_date__gte=timezone.now()) | RFQ.objects.filter(closing_date__isnull=True)

    return render(request, 'open_rfqs.html', {'open_rfqs': open_rfqs})

def apply_for_rfq(request, rfq_id):
    rfq = get_object_or_404(RFQ, id=rfq_id)
    
    if request.method == 'POST':
        form = RFQbidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.rfq = rfq
            bid.save()

    else:
        form = RFQbidForm()

    return render(request, 'apply_for_rfq.html', {'form': form, 'rfq': rfq})

def procurement_choice_view(request):
    if request.method == 'POST':
        form = ProcurementChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('procurement:tendering') 
    else:
        form = ProcurementChoiceForm()

    return render(request, 'procurement/procurement_choice_form.html', {'form': form})

def tendering_view(request):
    q_set = ProcurementChoice.objects.first()
    procurement_choice = q_set.name
    return render(request, 'procurement/tendering.html', {'procurement_choice': procurement_choice})