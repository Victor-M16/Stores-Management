from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from procurement.models import *
from .serializer import *

from rest_framework import generics
from rest_framework.response import Response
from django.utils import timezone


class CreateRFQAPIView(generics.CreateAPIView):
    queryset = RFQ.objects.all()
    serializer_class = RFQSerializer


class OpenRFQsAPIView(generics.ListCreateAPIView):
    queryset = RFQ.objects.filter(is_active=True)  
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


class RFQUpdateAPIView(APIView):
    def patch(self, request, pk):
        try:
            rfq_instance = RFQ.objects.get(pk=pk)
        except rfq_instance.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = RFQSerializer(rfq_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RFQSingleView(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    lookup_field = 'id'
    serializer_class = RFQSerializer
    queryset = RFQ.objects.all()

    