from django.urls import path

from .views import SendMoneyView


urlpatterns = [path("", SendMoneyView.as_view(), name="send_money")]
