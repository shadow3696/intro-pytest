from django.contrib import admin
from django.urls import path, include

from companies.views import send_company_email
from companies.urls import companies_router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(companies_router.urls)),
    path("send-email/", send_company_email, name="send-email"),
]
