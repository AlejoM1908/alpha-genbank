from django.test import Client
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class TestSeed(APITestCase):
    seed_data = {
        "name": "cannabis",
        "type": "indica",
        "genetic_purity": 89
    }
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

    def create_seed(self, data = seed_data):
        '''Used to create a new seed in the test db'''
        response = self.client.post(reverse('seed'), data)
        return response

    def test_get_all_items(self):
        """Is a unit test to check if the REST GET call is working to return all stored seeds"""
        # arrange
        self.authenticate()
        self.create_seed()

        # act
        response = self.client.get(reverse("seed"))

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_one_seed_by_id(self):
        """Is a unit test to check if the REST GET call is working to return the provided seed id info"""
        # arrange
        self.authenticate()
        seed_id = self.create_seed().data['id']

        # act
        response = self.client.get(f"/production/seed/?id={seed_id}")

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_seed_info(self):
        """Is a unit test to check if the REST PUT call is working to update the provided seed id info"""
        # arrange
        test_updated_data = {
            "name": "cannabis",
            "type": "ruderalis",
            "genetic_purity": 76
        }
        self.authenticate()
        seed_id = self.create_seed().data['id']

        # act
        response = self.client.put(f"/production/seed/?id={seed_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], test_updated_data["name"])

    def test_update_seed_error_when_updated_with_bad_request_data(self):
        """Is a unit test to check the error status code when given seed data to update don't pass the serializer parameters"""
        # arrange
        test_updated_data = {
            "something": "another something"
        }
        self.authenticate()
        seed_id = self.create_seed().data['id']

        # act
        response = self.client.put(f"/production/seed/?id={seed_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_seed(self):
        """Is a unit test to check if the REST DELETE call is working to delete the given user id info"""
        # Arrange
        self.authenticate()
        seed_id = self.create_seed().data['id']

        # Act
        response = self.client.delete(f"/production/seed/?id={seed_id}")

        # Assert
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_create_seed_error_with_bad_data(self):
        '''Is a unit test to check the REST POST show a correct error when given bad data'''
        # Arrange and Act
        self.authenticate()
        response = self.create_seed(data={"something": "another something"})

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class TestTerrain(APITestCase):
    terrain_data = {
        "area": 150.25,
        "tag": "terrain-1",
        "type": "greenhouse"
    }
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

    def create_terrain(self, data = terrain_data):
        '''Used to create a new seed in the test db'''
        response = self.client.post(reverse('terrain'), data)
        return response

    def test_get_all_items(self):
        """Is a unit test to check if the REST GET call is working to return all stored seeds"""
        # arrange
        self.authenticate()
        self.create_terrain()

        # act
        response = self.client.get(reverse("terrain"))

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_one_terrain_by_id(self):
        """Is a unit test to check if the REST GET call is working to return the provided seed id info"""
        # arrange
        self.authenticate()
        terrain_id = self.create_terrain().data['id']

        # act
        response = self.client.get(f"/production/terrain/?id={terrain_id}")

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_terrain_info(self):
        """Is a unit test to check if the REST PUT call is working to update the provided seed id info"""
        # arrange
        test_updated_data = {
            "area": 89.45,
            "tag": "greenhouse-terrain",
            "type": "greenhouse"
        }
        self.authenticate()
        terrain_id = self.create_terrain().data['id']

        # act
        response = self.client.put(f"/production/terrain/?id={terrain_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["area"], test_updated_data["area"])

    def test_update_terrain_error_when_updated_with_bad_request_data(self):
        """Is a unit test to check the error status code when given seed data to update don't pass the serializer parameters"""
        # arrange
        test_updated_data = {
            "something": "another something"
        }
        self.authenticate()
        terrain_id = self.create_terrain().data['id']

        # act
        response = self.client.put(f"/production/terrain/?id={terrain_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_terrain(self):
        """Is a unit test to check if the REST DELETE call is working to delete the given user id info"""
        # Arrange
        self.authenticate()
        terrain_id = self.create_terrain().data['id']

        # Act
        response = self.client.delete(f"/production/terrain/?id={terrain_id}")

        # Assert
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_create_terrain_error_with_bad_data(self):
        '''Is a unit test to check the REST POST show a correct error when given bad data'''
        # Arrange and Act
        self.authenticate()
        response = self.create_terrain(data={"something": "another something"})

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class TestLot(APITestCase):
    terrain_data = {
        "area": 150.25,
        "tag": "terrain-1",
        "type": "greenhouse"
    }
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

    def create_lot(self, data = None, terrain_id = 0):
        '''Used to create a new seed in the test db'''
        if terrain_id == 0: terrain_id = self.create_terrain().data['id']
        if data == None: data = {
            "tr_id": terrain_id,
            "target_purity": 85
        }
        response = self.client.post(reverse('lot'), data)
        return response

    def create_terrain(self, data = terrain_data):
        '''Used to create a new seed in the test db'''
        response = self.client.post(reverse('terrain'), data)
        return response

    def test_get_all_items(self):
        """Is a unit test to check if the REST GET call is working to return all stored seeds"""
        # arrange
        self.authenticate()
        self.create_lot()

        # act
        response = self.client.get(reverse("lot"))

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_one_lot_by_id(self):
        """Is a unit test to check if the REST GET call is working to return the provided seed id info"""
        # arrange
        self.authenticate()
        lot_id = self.create_lot().data['id']

        # act
        response = self.client.get(f"/production/lot/?id={lot_id}")

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lot_info(self):
        """Is a unit test to check if the REST PUT call is working to update the provided seed id info"""
        # arrange
        self.authenticate()
        terrain_id = self.create_terrain().data['id']
        test_updated_data = {
            "tr_id": terrain_id,
            "target_purity": 90
        }
        lot_id = self.create_lot(terrain_id=terrain_id).data['id']

        # act
        response = self.client.put(f"/production/lot/?id={lot_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["target_purity"], test_updated_data["target_purity"])

    def test_update_lot_error_when_updated_with_bad_request_data(self):
        """Is a unit test to check the error status code when given seed data to update don't pass the serializer parameters"""
        # arrange
        test_updated_data = {
            "something": "another something"
        }
        self.authenticate()
        lot_id = self.create_lot().data['id']

        # act
        response = self.client.put(f"/production/lot/?id={lot_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_lot(self):
        """Is a unit test to check if the REST DELETE call is working to delete the given user id info"""
        # Arrange
        self.authenticate()
        lot_id = self.create_lot().data['id']

        # Act
        response = self.client.delete(f"/production/lot/?id={lot_id}")

        # Assert
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_create_lot_error_with_bad_data(self):
        '''Is a unit test to check the REST POST show a correct error when given bad data'''
        # Arrange and Act
        self.authenticate()
        response = self.create_lot(data = {'something': 'another something'})

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class TestCrop(APITestCase):
    terrain_data = {
        "area": 150.25,
        "tag": "terrain-1",
        "type": "greenhouse"
    }
    seed_data = {
        "name": "cannabis",
        "type": "indica",
        "genetic_purity": 89
    }
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

    def create_lot(self, data = None, terrain_id = 0):
        '''Used to create a new seed in the test db'''
        if terrain_id == 0: terrain_id = self.create_terrain().data['id']
        if data == None: data = {
            "tr_id": terrain_id,
            "target_purity": 85
        }
        response = self.client.post(reverse('lot'), data)
        return response

    def create_terrain(self, data = terrain_data):
        '''Used to create a new seed in the test db'''
        response = self.client.post(reverse('terrain'), data)
        return response

    def create_seed(self, data = seed_data):
        '''Used to create a new seed in the test db'''
        response = self.client.post(reverse('seed'), data)
        return response

    def create_crop(self, data = None, lot_id = 0, seed_id = 0):
        '''Used to create a new seed in the test db'''
        if lot_id == 0: lot_id = self.create_lot().data['id']
        if seed_id == 0: seed_id = self.create_seed().data['id']
        if data == None: data = {
            "lt_id": lot_id,
            "se_id": seed_id,
            "type": "crop-1",
            "projected_date": "2023-08-20"
        }
        response = self.client.post(reverse('crop'), data)
        return response

    def test_get_all_items(self):
        """Is a unit test to check if the REST GET call is working to return all stored seeds"""
        # arrange
        self.authenticate()
        self.create_crop()

        # act
        response = self.client.get(reverse("crop"))

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_one_crop_by_id(self):
        """Is a unit test to check if the REST GET call is working to return the provided seed id info"""
        # arrange
        self.authenticate()
        crop_id = self.create_crop().data['id']

        # act
        response = self.client.get(f"/production/crop/?id={crop_id}")

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_crop_info(self):
        """Is a unit test to check if the REST PUT call is working to update the provided seed id info"""
        # arrange
        self.authenticate()
        lot_id = self.create_lot().data['id']
        seed_id = self.create_seed().data['id']
        test_updated_data = {
            "lt_id": lot_id,
            "se_id": seed_id,
            "type": "crop-2",
            "projected_date": "2024-08-20"
        }
        crop_id = self.create_crop(lot_id=lot_id, seed_id=seed_id).data['id']

        # act
        response = self.client.put(f"/production/crop/?id={crop_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["projected_date"], test_updated_data["projected_date"])

    def test_update_crop_error_when_updated_with_bad_request_data(self):
        """Is a unit test to check the error status code when given seed data to update don't pass the serializer parameters"""
        # arrange
        test_updated_data = {
            "something": "another something"
        }
        self.authenticate()
        crop_id = self.create_crop().data['id']

        # act
        response = self.client.put(f"/production/crop/?id={crop_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_crop(self):
        """Is a unit test to check if the REST DELETE call is working to delete the given user id info"""
        # Arrange
        self.authenticate()
        crop_id = self.create_crop().data['id']

        # Act
        response = self.client.delete(f"/production/crop/?id={crop_id}")

        # Assert
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_create_crop_error_with_bad_data(self):
        '''Is a unit test to check the REST POST show a correct error when given bad data'''
        # Arrange and Act
        self.authenticate()
        response = self.create_crop(data = {'something': 'another something'})

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class TestHarvest(APITestCase):
    terrain_data = {
        "area": 150.25,
        "tag": "terrain-1",
        "type": "greenhouse"
    }
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

    def create_lot(self, data = None, terrain_id = 0):
        '''Used to create a new seed in the test db'''
        if terrain_id == 0: terrain_id = self.create_terrain().data['id']
        if data == None: data = {
            "tr_id": terrain_id,
            "target_purity": 85
        }
        response = self.client.post(reverse('lot'), data)
        return response

    def create_harvest(self, data = None, lot_id = 0):
        '''Ised to create a new harvest in the test db'''
        if lot_id == 0: lot_id = self.create_lot().data['id']
        if data == None: data = {
            "lt_id": lot_id,
            "flower": 402.52,
            "waste": 103.85
        }
        response = self.client.post(reverse('harvest'), data)
        return response

    def create_terrain(self, data = terrain_data):
        '''Used to create a new seed in the test db'''
        response = self.client.post(reverse('terrain'), data)
        return response

    def test_get_all_items(self):
        """Is a unit test to check if the REST GET call is working to return all stored seeds"""
        # arrange
        self.authenticate()
        self.create_harvest()

        # act
        response = self.client.get(reverse("harvest"))

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_one_harvest_by_id(self):
        """Is a unit test to check if the REST GET call is working to return the provided seed id info"""
        # arrange
        self.authenticate()
        harvest_id = self.create_harvest().data['id']

        # act
        response = self.client.get(f"/production/harvest/?id={harvest_id}")

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_harvest_info(self):
        """Is a unit test to check if the REST PUT call is working to update the provided seed id info"""
        # arrange
        self.authenticate()
        lot_id = self.create_lot().data['id']
        test_updated_data = {
            "lt_id": lot_id,
            "flower": 651.52,
            "waste": 76.12
        }
        harvest_id = self.create_harvest(lot_id=lot_id).data['id']

        # act
        response = self.client.put(f"/production/harvest/?id={harvest_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["flower"], test_updated_data["flower"])

    def test_update_harvest_error_when_updated_with_bad_request_data(self):
        """Is a unit test to check the error status code when given seed data to update don't pass the serializer parameters"""
        # arrange
        test_updated_data = {
            "something": "another something"
        }
        self.authenticate()
        harvest_id = self.create_harvest().data['id']

        # act
        response = self.client.put(f"/production/harvest/?id={harvest_id}", test_updated_data)

        # assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_harvest(self):
        """Is a unit test to check if the REST DELETE call is working to delete the given user id info"""
        # Arrange
        self.authenticate()
        harvest_id = self.create_harvest().data['id']

        # Act
        response = self.client.delete(f"/production/harvest/?id={harvest_id}")

        # Assert
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_create_crop_error_with_bad_data(self):
        '''Is a unit test to check the REST POST show a correct error when given bad data'''
        # Arrange and Act
        self.authenticate()
        response = self.create_harvest(data = {'something': 'another something'})

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
