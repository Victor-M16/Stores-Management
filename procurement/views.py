

# Create your views here.
#Choose Procurement Choice
#Manage Tendering Process
#Manage Contract Awarding
#Record the procurement process
#Compliance Monitoring



from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProcurementChoiceForm
from .models import ProcurementChoice

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