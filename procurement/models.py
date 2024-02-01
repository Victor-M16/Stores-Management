from django.db import models
from stock.models import Product

class ProcurementChoice(models.Model):
    OPEN_TENDERING = 'open_tendering'
    RESTRICTED_TENDERING = 'restricted_tendering'
    #two stage tendering
    INTERNATIONAL_TENDERING = 'international_tendering'
    RFQ = 'rfq'
    SINGLE_SOURCE = 'single_source'

    PROCUREMENT_CHOICES = [
        (OPEN_TENDERING, 'Open Tendering'),
        (RESTRICTED_TENDERING, 'Restricted Tendering'),
        #(INTERNATIONAL_TENDERING, 'International Tendering'),
        (RFQ, 'Request For Quotation (RFQ)'),
        (SINGLE_SOURCE , 'Single Source'),
    ]

    name = models.CharField(max_length=255, choices=PROCUREMENT_CHOICES)

    def __str__(self):
        return self.get_name_display()

#pblic
class TenderNotice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    procurement_choice = models.ForeignKey(ProcurementChoice, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)
    closing_date = models.DateField()

    def __str__(self):
        return self.title


class Bid(models.Model):
    tender_notice = models.ForeignKey(TenderNotice, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255)
    proposal = models.TextField()
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.supplier_name} - {self.tender_notice}"

#procuring entity
class Contract(models.Model):
    tender_notice = models.OneToOneField(TenderNotice, on_delete=models.CASCADE)
    winning_bid = models.OneToOneField(Bid, on_delete=models.CASCADE)
    contract_text = models.TextField()

    def __str__(self):
        return f"Contract for {self.tender_notice} - {self.winning_bid.supplier_name}"

#status
class ProcurementProcess(models.Model):
    tender_notice = models.ForeignKey(TenderNotice, on_delete=models.CASCADE)
    selected_bid = models.OneToOneField(Bid, on_delete=models.SET_NULL, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Procurement Process for {self.tender_notice}"

#not important rn
class PublicProcurementAct(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

