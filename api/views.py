from django.shortcuts import render
from rest_framework import generics

from procurement.models import *
from .serializer import *

from rest_framework import generics
from rest_framework.response import Response
from django.utils import timezone


class CreateRFQAPIView(generics.CreateAPIView):
    queryset = RFQ.objects.all()
    serializer_class = RFQSerializer


class OpenRFQsAPIView(generics.ListAPIView):
    queryset = RFQ.objects.filter(closing_date__gte=timezone.now()) | RFQ.objects.filter(closing_date__isnull=True)
    serializer_class = RFQSerializer


class ApplyToRFQAPIView(generics.CreateAPIView):
    queryset = RFQbid.objects.all()
    serializer_class = RFQbidSerializer



class ProcurementChoiceView(generics.ListAPIView):
    queryset = ProcurementChoice.objects.all()
    serializer_class = ProcurementChoiceSerializer


class TenderNoticeView(generics.ListAPIView):
    queryset = TenderNotice.objects.all()
    serializer_class = TenderNoticeSerializer


class BidView(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class ContractView(generics.ListAPIView):
    queryset = ProcurementChoice.objects.all()
    serializer_class = ContractSerializer


class ProcurementProcessView(generics.ListAPIView):
    queryset = ProcurementProcess.objects.all()
    serializer_class = ProcurementProcessSerializer


class PublicProcurementActView(generics.ListAPIView):
    queryset = PublicProcurementAct.objects.all()
    serializer_class = PublicProcurementActSerializer

