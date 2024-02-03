from rest_framework import serializers

from procurement.models import *
from stock.serializers import ProductInventorySerializer

class ProcurementChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcurementChoice
        fields = '__all__'

class RFQSerializer(serializers.ModelSerializer):

    product = ProductInventorySerializer()

    class Meta:
        model = RFQ
        fields = '__all__'

class RFQbidSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFQbid
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
