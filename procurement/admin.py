from django.contrib import admin
from .models import ProcurementChoice, TenderNotice, Bid, Contract, ProcurementProcess, PublicProcurementAct

admin.site.register(ProcurementChoice)
admin.site.register(TenderNotice)
admin.site.register(Bid)
admin.site.register(Contract)
admin.site.register(ProcurementProcess)
admin.site.register(PublicProcurementAct)
