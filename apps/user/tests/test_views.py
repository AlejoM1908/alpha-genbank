from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestModel(APITestCase):
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
        return response.data["id"] if response.status_code == 200 else response

    def test_error_registrating_user(self):
        """Is a unit test designed to test the fail user creation case"""
        # Arrange
        test_data = {
            "email": "test@email.test",
            "password": "testpassword123",
        }

        # Act
        response = self.authenticate(data= test_data)

        #Assert
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_all_items(self):
        """Is a unit test to check if the REST GET call is working to return all stored users"""
        # arrange
        self.authenticate()

        # act
        response = self.client.get(reverse("user"))

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_one_user_by_id(self):
        """Is a unit test to check if the REST GET call is working to return the provided user id info"""
        # arrange
        user_id = self.authenticate()

        # act
        response = self.client.get(f"/user/?id={user_id}")

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_info(self):
        """Is a unit test to check if the REST PUT call is working to update the provided user id info"""
        # arrange
        test_updated_data = {
            "username": "testupdateduser",
            "email": "test@email.test",
            "first_name": "testnameupdated",
            "last_name": "testlastnameupdated"
        }
        user_id = self.authenticate()

        # act
        response = self.client.put(f"/user/?id={user_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], test_updated_data["username"])

    def test_update_user_error_when_updated_with_bad_request_data(self):
        """Is a unit test to check the error status code when given user data to update don't pass the serializer parameters"""
        # arrange
        test_updated_data = {
            "something": "another something"
        }
        user_id = self.authenticate()

        # act
        response = self.client.put(f"/user/?id={user_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user_password(self):
        """Is a unit test to check if the REST PUT call is working to update the provided user id info"""
        # arrange
        test_updated_data = {
            "old_password": "testpassword123",
            "new_password": "testupdatedpassword123"
        }
        user_id = self.authenticate()

        # act
        response = self.client.put(f"/user/change-password/?id={user_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_error_when_updated_with_bad_request_data(self):
        """Is a unit test to check the error status code when given user data to update don't pass the serializer parameters"""
        # arrange
        test_updated_data = {
            "old_password": "test123",
            "new_password": "testupdatedpassword123"
        }
        user_id = self.authenticate()

        # act
        response = self.client.put(f"/user/change-password/?id={user_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_user(self):
        """Is a unit test to check if the REST DELETE call is working to delete the given user id info"""
        user_id = self.authenticate()
        response = self.client.delete(f"/user/?id={user_id}")

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
