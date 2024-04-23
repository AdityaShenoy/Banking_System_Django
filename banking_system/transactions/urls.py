from django.urls import path

from .views import TransactionsView


urlpatterns = [path("", TransactionsView.as_view(), name="transactions")]
