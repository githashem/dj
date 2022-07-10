from django.test import TestCase, override_settings
from django.urls import reverse
from django.conf import settings
from djplus.auth.forms import LoginForm
from djplus.auth.models import User


class LoginViewTest(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(reverse("auth:login"))

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_accessible_by_name(self):
        self.assertEqual(reverse("auth:login"), "/auth/login/")

    def test_use_correct_template(self):
        self.assertTemplateUsed(self.response, "auth/login.html")

    def test_login_form_exists_in_context(self):
        self.assertIn("form", self.response.context)
        self.assertIsInstance(self.response.context["form"], LoginForm)


@override_settings(ROOT_URLCONF="djplus.auth.urls")
class LogoutViewTest(TestCase):
    user_data = {
        "username": "test",
        "password": "123456",
    }

    @classmethod
    def setUpTestData(cls):
        User.objects.create(**cls.user_data)

    def setUp(self) -> None:
        self.client.post("/login/", data=self.user_data)

    @override_settings(AUTH_SESSION_COOKIE_NAME="custom")
    def test_logout_with_custom_session_cookie_name(self):
        response = self.client.post("/logout/")
        self.assertNotIn("custom", response.cookies)

    @override_settings(AUTH_LOGOUT_REDIRECT_URL="/custom/")
    def test_logout_redirect_url_setting(self):
        response = self.client.post("/logout/")
        self.assertRedirects(response, "/custom/", fetch_redirect_response=False)

    @override_settings(AUTH_LOGOUT_REDIRECT_URL=None)
    def test_when_logout_redirect_url_setting_is_none(self):
        response = self.client.post("/logout/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "auth/logout.html")
        self.assertNotIn(settings.AUTH_SESSION_COOKIE_NAME, response.cookies)
