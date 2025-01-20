import json
import pytest
from unittest import TestCase

# import pytest_django
from django.test import Client
from django.urls import reverse

from companies.models import Company

companies_url = reverse("companies-list")

@pytest.mark.django_db
class BasicComponyAPiTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.companies_url = reverse("companies-list")

    def tearDown(self):
        pass

# =====================Test Get Companies=========================

@pytest.mark.django_db
def test_zero_companies_should_return_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []

@pytest.mark.django_db
def test_one_companies_exists_should_succeed(client) -> None:
    test_companies = Company.objects.create(name="Amazon")
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == test_companies.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""
    test_companies.delete()

# ===============End Test Get Companies==========================

# ==============Test Post companies==============================

@pytest.mark.django_db
def test_create_company_without_arguments_should_fail(client) -> None:
    response = client.post(path=companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}


@pytest.mark.django_db
def test_create_existing_company_should_fail(client) -> None:
    client.post(path=companies_url, data={"name": "king"})
    response = client.post(path=companies_url, data={"name": "king"})
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["company with this name already exists."]}


@pytest.mark.django_db
def test_create_company_with_only_name_all_fields_should_be_succeed(client) -> None:
    response = client.post(
        path=companies_url, data={"name": "tests company name"}
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("name") == "tests company name"
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


@pytest.mark.django_db
def test_create_company_with_layoffs_status_should_succeed(client) -> None:
    response = client.post(
        path=companies_url,
        data={"name": "tests company name", "status": "Layoffs"},
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("name") == "tests company name"
    assert response_content.get("status") == "Layoffs"


@pytest.mark.django_db
def test_create_company_with_wrong_status_should_fail(client) -> None:
    response = client.post(
        path=companies_url,
        data={"name": "tests company name", "status": "WrongStatus"},
    )
    assert response.status_code == 400
    assert "WrongStatus" in str(response.content)
    assert "is not a valid choice" in str(response.content)

# ==============End Test Post companies==============================


@pytest.mark.xfail
def test_should_be_ok_if_fails() -> None:
    assert 1 == 2


@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2


def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")


def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)


import logging

logger = logging.getLogger("CORONA_LOGS")


def function_that_logs_somthing() -> None:
    try:
        raise ValueError("CoronaVirus Exception")
    except ValueError as e:
        logger.warning(f"I am logging {str(e)}")


def test_logged_warning_level(caplog) -> None:
    function_that_logs_somthing()
    print(f"\n {caplog.text}")
    assert "I am logging CoronaVirus Exception" in caplog.text


def test_logged_info_level(caplog) -> None:
    with caplog.at_level(logging.INFO):
        logger.info("I am logging info level")
        print(f"\n {caplog.text}")
        assert "I am logging info level" in caplog.text
