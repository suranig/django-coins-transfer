from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transfer
from .serializers import TransferSerializer, TransferPostSerializer


class TransferListCreateAPIView(APIView):
    """
    GET
    Returns a history of all transfers in the system for current user.
    Current user must be sender or reveiver of transfer.

    POST
    Current user send coins to other user.
    parameters:
        - in: query
          name: amount
          schema:
            type: integer
            required: true
            description: Coins amount to send.
        - in: query
          name: receiver
          schema:
            type: integer
            required: true
            description: User ID who will get your coins.
    """

    def get(self, request):
        """
        GET
        Returns a history of all transfers in the system for current user.
        Current user must be sender or reveiver of transfer.
        """
        transfer = Transfer.objects.filter(sender=request.user).union(
            Transfer.objects.filter(receiver=request.user))

        serializer = TransferSerializer(transfer, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        POST
        Current user send coins to other user.
        :amount -- Coins amount to send.
        :receiver -- User ID who will get your coins.
        """
        serializer = TransferPostSerializer(data=request.data)
        if serializer.is_valid():
            sender = request.user
            if sender == request.user:
                serializer.save(sender=sender)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
