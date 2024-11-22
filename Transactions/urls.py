from django.urls import path
from .views import TransactionCreateView, TransactionDetailView, TransactionListView

urlpatterns = [
    path('transactions/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/list/', TransactionListView.as_view(), name='transaction-list'),
]




# from django.contrib import admin
# from django.urls import path, include
# from Transactions.views import welcome_page

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('Transactions.urls')),
#     path('', welcome_page),  # Define the root route
# ]
