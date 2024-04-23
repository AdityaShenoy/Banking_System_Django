from django.urls import path

from .views import WithdrawView


urlpatterns = [path("", WithdrawView.as_view(), name="withdraw")]
