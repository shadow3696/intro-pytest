import json
from unittest.mock import patch
from django.core import mail


def test_send_email_should_succeed(mailoutbox, settings) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    assert len(mailoutbox) == 0

    # Send message
    mail.send_mail(
        subject="Test Subject here",
        message="Test Here is the message",
        from_email="testemail@gmail.com",
        recipient_list=["testemail2@gmail.com"],
        fail_silently=False,
    )

    # Test that one message has been sent.
    assert len(mailoutbox) == 1

    # verify that the subject of the first message is correct
    assert mailoutbox[0].subject == "Test Subject here"


def test_send_email_without_arguments_should_send_empty_email(client) -> None:
    with patch("companies.views.send_mail") as mocked_send_mail_function:
        mocked_send_mail_function.return_value = None

        response = client.post(
            path="/send-email/", data={}, content_type="application/json"
        )

        assert response.status_code == 200
        response_content = response.json()
        assert response_content["status"] == "success"
        assert response_content["info"] == "email sent successfully"

        mocked_send_mail_function.assert_called_with(
            subject="Default Subject",
            message="Default Message",
            from_email="swistechlayoffs@gmail.com",
            recipient_list=["swistechlayoffs@gmail.com"],
        )


def test_send_email_with_get_verb_should_fail(client) -> None:
    response = client.get(path="/send-email/", data={}, content_type="application/json")
    assert response.status_code == 405
    assert json.loads(response.content) == {"detail": 'Method "GET" not allowed.'}
