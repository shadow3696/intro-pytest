from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_updated")
    pagination_class = PageNumberPagination


@api_view(http_method_names=['POST'])
def send_company_email(request: Request) -> Response:
    """
    Send email with request payload
    sender: swistechlayoffs@gmail.com
    receiver: swistechlayoffs@gmail.com
    """
    subject = request.data.get("subject", "Default Subject")
    message = request.data.get("message", "Default Message")

    if not subject or not message:
        return Response({"status": "error", "info": "Subject and message are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["swistechlayoffs@gmail.com"],
        )
        return Response({"status": "success", "info": "email sent successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"status": "error", "info": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)