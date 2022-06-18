from rest_framework.test import APITestCase
from datetime import datetime, timedelta
from user.jwt import JWTAuthentication
from django.conf import settings
from django.urls import reverse
from rest_framework import status
import jwt

class TestJWT(APITestCase):
    authenticator = JWTAuthentication()
    auth_data = {
            "username": "testuser",
            "email": "test@email.test",
            "password": "testpassword123",
    }

    def authenticate(self, data = auth_data):
        """Used to create a user in the test database and be able to use token protected endpoints"""

        # Save user to test database
        self.client.post(reverse("register"), data)
        response = self.client.post(reverse("auth"), data)
        token = response.data["token"] if response.status_code == 200 else ''

        # Save the token for authorization ussage and returning user id
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        return response

    def test_invalid_token_length(self):
        # Arrange
        login = self.authenticate()
        user_token = f'Bearer {str(login.data["token"])} error'
        self.client.credentials(HTTP_AUTHORIZATION=user_token)

        # Act
        response = self.client.get(reverse("user"))

        # Assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'].split("'")[0], 'Invalid token provided')

    def test_token_expiracy_date(self):
        # Arrange
        user_token = jwt.encode(
            {
                "username": "testuser",
                "email": "test@email.test",
                "exp": datetime.utcnow() - timedelta(hours=16),
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        )
        user_token = f'Bearer {user_token}'
        self.client.credentials(HTTP_AUTHORIZATION=user_token)

        # Act
        response = self.client.get(reverse("user"))

        # Assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'].split("'")[0], 'The provided token is expired')

    def test_invalid_token_structure(self):
        # Arrange
        login = self.authenticate()
        user_token = f'Bearer {str(login.data["token"])}error'
        self.client.credentials(HTTP_AUTHORIZATION=user_token)

        # Act
        response = self.client.get(reverse("user"))

        # Assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'].split("'")[0], 'The provided token has invalid structure')

    def test_token_user_doesnt_exists(self):
        # Arrange
        user_token = jwt.encode(
            {
                "username": "nonexistenttestuser",
                "email": "nonexistenttest@email.test",
                "exp": datetime.utcnow() + timedelta(hours=16),
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        )
        user_token = f'Bearer {user_token}'
        self.client.credentials(HTTP_AUTHORIZATION=user_token)

        # Act
        response = self.client.get(reverse("user"))

        # Assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'].split("'")[0], 'The token owner does not exists')
