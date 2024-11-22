from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from .models import Transaction
from .serializers import TransactionSerializer
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Welcome to the Transaction Management API!"})

# Create a new transaction
class TransactionCreateView(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# Retrieve and update a transaction
class TransactionDetailView(RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# List all transactions for a user
class TransactionListView(ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return Transaction.objects.filter(user_id=user_id)
# from django.http import JsonResponse

# def welcome_page(request):
#     return JsonResponse({"message": "Welcome to the Transaction Management API!"})

