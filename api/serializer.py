from rest_framework import serializers

from procurement.models import *

class ProcurementChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcurementChoice
        fields = '__all__'



class TenderNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderNotice
        fields = '__all__'



class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'



class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'



class ProcurementProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcurementProcess
        fields = '__all__'



class PublicProcurementActSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicProcurementAct
        fields = '__all__'
