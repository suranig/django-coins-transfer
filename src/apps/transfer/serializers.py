from rest_framework import serializers
from .models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()

    def get_sender(self, obj):
        return obj.sender.username

    def get_receiver(self, obj):
        return obj.receiver.username

    class Meta:
        model = Transfer
        fields = ('id', 'created', 'amount', 'sender', 'receiver')


class TransferPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('amount', 'receiver')
