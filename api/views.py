from django.shortcuts import render
from rest_framework import generics

from procurement.models import *
from .serializer import *


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

