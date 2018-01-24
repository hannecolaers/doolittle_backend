from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from floorplan.models import Room, Space
from floorplan.serializers import RoomSerializer, SpaceSerializer

from django.urls import reverse
from django.contrib.auth.models import User


def create_room_serializer(data, url, many=False):
    request = APIRequestFactory().get(url)
    serializer = RoomSerializer(data, many=many, context={'request': request})
    return serializer


class RoomTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create(username='test')
        self.client.force_authenticate(user=user)

        self.room_name = 'ROOM-NAME'
        self.room_type = 'Kitchen'
        self.room_color = 'FFFFFF'
        self.room_json = {
            'name': self.room_name,
            'type': self.room_type,
            'color': self.room_color
        }

        self.changed_room_name = 'CHANGED-ROOM-NAME'
        self.changed_room_type = 'Empty'
        self.changed_room_color = '000000'
        self.changed_room_json = {
            'name': self.changed_room_name,
            'type': self.changed_room_type,
            'color': self.changed_room_color
        }

        self.room = Room.objects.create(
            name=self.room_name,
            type=self.room_type,
            color=self.room_color
        )

        self.url_with_id = reverse('room-detail', args=[self.room.id])

    """
    Tests for the /rooms/{id} path
    """

    def test_get_room_returns_200_when_found(self):
        """
        A GET request on /rooms/{id} should return a room
        """
        response = self.client.get(self.url_with_id, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {'id': self.room.id, 'name': self.room_name, 'type': self.room_type, 'color': self.room_color})

    def test_get_room_returns_404_when_not_found(self):
        """
        A GET request on /rooms/{id} should return a 404 error when the room doesn't exist
        """
        response = self.client.get('/rooms/666/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_room_returns_405(self):
        """
        A POST request on /rooms/{id} should not be possible
        """
        response = self.client.post('/rooms/666/', self.room_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_room_returns_200_when_updated(self):
        """
        A PUT request on /rooms/{id} should return an updated room
        """
        response = self.client.get(self.url_with_id, format="json")
        response = self.client.put('/rooms/' + str(self.room.id) + '/', self.changed_room_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {'id': self.room.id, 'name': self.changed_room_name, 'type': self.changed_room_type,
                          'color': self.changed_room_color})

    def test_put_room_returns_400_when_incorrect(self):
        """
        A PUT request on /rooms/{id} should return 400 when sent incorrectly
        """
        response = self.client.put('/rooms/' + str(self.room.id) + '/', {'incorrectly-typed': self.changed_room_name},
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_room_returns_400_when_empty(self):
        """
        A PUT request on /rooms/{id} should return 400 when sent empty
        """
        response = self.client.put('/rooms/' + str(self.room.id) + '/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_room_returns_400_when_invalid_value(self):
        """
        A PUT request on /rooms/{id} should return 400 when sent incorrectly
        """
        response = self.client.put('/rooms/' + str(self.room.id) + '/', {'name': None}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_room_returns_404_when_not_found(self):
        """
        A PUT request on /rooms/{id} should return a 404 when using an invalid id
        """
        response = self.client.put('/rooms/666/', self.changed_room_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_room_returns_404_when_invalid_character(self):
        """
        A PUT request on /rooms/{id} should return a 404 when using an invalid character
        """
        response = self.client.put('/rooms/xyz/', self.changed_room_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_room_returns_404_when_negative_id(self):
        """
        A PUT request on /rooms/{id} should return a 404 when using an invalid character
        """
        response = self.client.put('/rooms/-100/', self.changed_room_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_room_returns_200_when_updated(self):
        """
        A PATCH request on /rooms/{id} should return an updated room
        """
        response = self.client.patch('/rooms/' + str(self.room.id) + '/', self.changed_room_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {'id': self.room.id, 'name': self.changed_room_name, 'type': self.changed_room_type,
                          'color': self.changed_room_color})

    def test_patch_room_returns_400_when_incorrect(self):
        """
        A PATCH request on /rooms/{id} should return 400 when sent incorrectly
        """
        response = self.client.patch('/rooms/' + str(self.room.id) + '/', {'name': None}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_room_returns_404_when_not_found(self):
        """
        A PATCH request on /rooms/{id} should return 404 when using an invalid id
        """
        response = self.client.patch('/rooms/666/', self.room_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_room_returns_404_when_invalid_character(self):
        """
        A PATCH request on /rooms/{id} should return 404 when using an invalid id
        """
        response = self.client.patch('/rooms/xyz/', self.room_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_room_returns_404_when_negative_id(self):
        """
        A PATCH request on /rooms/{id} should return 404 when using an invalid id
        """
        response = self.client.patch('/rooms/-100/', self.room_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_room_returns_204_when_deleting(self):
        """
        A DELETE request on /rooms/{id} should delete a room
        """
        response = self.client.delete('/rooms/' + str(self.room.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_room_returns_404_when_not_found(self):
        """
        A DELETE request on /rooms/{id} should return 404 when deleting a non existing room
        """
        response = self.client.delete('/rooms/666/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_room_returns_404_when_invalid_character(self):
        """
        A DELETE request on /rooms/{id} should return 404 when deleting a non existing room
        """
        response = self.client.delete('/rooms/xyz/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_room_returns_404_when_negative_id(self):
        """
        A DELETE request on /rooms/{id} should return 404 when deleting a non existing room
        """
        response = self.client.delete('/rooms/-100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    Tests for the /rooms/ path
    """

    def test_get_all_rooms_returns_200_when_found(self):
        """
        A GET request on /rooms/ should return an array of all rooms
        """
        self.client.post('/rooms/', self.changed_room_json, format='json')
        response = self.client.get('/rooms/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Room.objects.count(), 2)

        self.assertIsNotNone(Room.objects.get(name=self.room_name))
        self.assertIsNotNone(Room.objects.get(name=self.changed_room_name))

    def test_get_all_rooms_returns_200_when_non_found(self):
        """
        A GET request on /rooms/ should still work with no results and return an empty array
        """
        Room.objects.all().delete()
        response = self.client.get('/rooms/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Room.objects.count(), 0)

    def test_post_all_rooms_returns_201_when_correct_format(self):
        """
        A POST request on /rooms/ should create a new room
        """
        self.assertEqual(Room.objects.count(), 1)
        response = self.client.post('/rooms/', self.changed_room_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Room.objects.count(), 2)

    def test_post_all_rooms_returns_400_when_incorrect_attribute(self):
        """
        A POST request on /rooms/ using the wrong format should return a 400 error
        """
        response = self.client.post('/rooms/', {'incorrectly-typed': self.room_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_all_rooms_returns_400_when_empty_value(self):
        """
        A POST request on /rooms/ using the wrong format should return a 400 error
        """
        response = self.client.post('/rooms/', {'name': None}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_all_rooms_returns_400_when_missing_field(self):
        """
        A POST request on /rooms/ using the wrong format should return a 400 error
        """
        response = self.client.post('/rooms/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_all_rooms_returns_405(self):
        """
        A PUT request on /rooms/ should not be possible
        """
        response = self.client.put('/rooms/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_all_rooms_returns_405(self):
        """
        A PATCH request on /rooms/ should not be possible
        """
        response = self.client.patch('/rooms/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_all_rooms_returns_405(self):
        """
        A DELETE request on /rooms/ should not be possible
        """
        response = self.client.delete('/rooms/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


def create_space_serializer(data, url, many=False):
    request = APIRequestFactory().get(url)
    serializer = SpaceSerializer(data, many=many, context={'request': request})
    return serializer


class SpaceTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create(username='test')
        self.client.force_authenticate(user=user)

        self.room_name = 'lobby'
        self.room = Room.objects.create(
            name=self.room_name
        )

        self.room_name2 = 'desk'
        self.room2 = Room.objects.create(
            name=self.room_name2
        )

        self.space_x = 100
        self.space_y = 200
        self.space_employee_id = 1
        self.space_room = self.room
        self.space_json = {
            'x': self.space_x,
            'y': self.space_y,
            'employee_id': self.space_employee_id,
            'room': {
                "name": self.room_name
            }
        }
        self.space = Space.objects.create(
            x=self.space_x,
            y=self.space_y,
            employee_id=self.space_employee_id,
            room=self.room
        )

        self.changed_space_x = 300
        self.changed_space_y = 400
        self.changed_space_employee_id = 3
        self.changed_space_json = {
            'x': self.changed_space_x,
            'y': self.changed_space_y,
            'employee_id': self.changed_space_employee_id,
            'room': {
                "name": self.room_name2
            }
        }

        self.url_with_id = reverse('space-detail', args=[self.space.id])

    """
     Tests for SpaceSerializer
    """

    def test_space_serializer_expected_fields(self):
        """
        The serializer should only expect and accept the fields that have been set
        """
        serializer = create_space_serializer(self.space, '')
        self.assertSetEqual(set(serializer.data.keys()), {'x', 'y', 'employee_id', 'room'})

    def test_space_serializer_x_field_content(self):
        """
        The x field of a space should contain a value
        """
        serializer = create_space_serializer(self.space, '')
        self.assertEqual(serializer.data['x'], self.space.x)

    def test_space_serializer_y_field_content(self):
        """
        The y field of a space should contain a value
        """
        serializer = create_space_serializer(self.space, '')
        self.assertEqual(serializer.data['y'], self.space.y)

    def test_space_serializer_employee_id_field_content(self):
        """
        The employee_id field of a space should contain a value
        """
        serializer = create_space_serializer(self.space, '')
        self.assertEqual(serializer.data['employee_id'], self.space.employee_id)

    def test_space_serializer_room_name_field_content(self):
        """
        The room_id field of a space should contain a value
        """
        serializer = create_space_serializer(self.space, '')
        self.assertEqual(serializer.data['room']['name'], self.room_name)

    def test_space_serializer_returns_empty_when_no_spaces(self):
        """
        The serializer should return [] when no objects are given
        """
        space = Space.objects.none()
        serialzer = create_space_serializer(space, '/', many=True)
        self.assertEqual(serialzer.data, [])

    """
    Tests for the /spaces/{id} path
    """

    def test_get_space_returns_200_when_found(self):
        """
        A GET request on /spaces/{id} should return a space
        """
        response = self.client.get('/spaces/' + str(self.space.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Space.objects.count(), 1)

        self.assertIsNotNone(Space.objects.get(x=self.space_x, y=self.space_y))

    def test_get_space_returns_404_when_not_found(self):
        """
        A GET request on /spaces/{id} should return a 404 error when the space doesn't exist
        """
        response = self.client.get('/spaces/666/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_space_returns_404_when_negative_id(self):
        """
        A GET request on /spaces/{id} should return a 404 error when the space doesn't exist
        """
        response = self.client.get('/spaces/-100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_space_returns_404_when_invalid_character(self):
        """
        A GET request on /spaces/{id} should return a 404 error when the space doesn't exist
        """
        response = self.client.get('/spaces/xyz/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_space_returns_405(self):
        """
        A POST request on /spaces/{id} should not be possible
        """
        response = self.client.post('/spaces/666/', self.space_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_space_returns_200_when_updated(self):
        """
        A PUT request on /spaces/{id} should return an updated space
        """
        response = self.client.put('/spaces/' + str(self.space.id) + '/', self.changed_space_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Space.objects.get(id=self.space.id).x, self.changed_space_x)

    def test_put_space_returns_400_when_invalid_room(self):
        """
            A PUT request on /spaces/{id} should return 400 when room does not exist
        """
        response = self.client.put('/spaces/' + str(self.space.id) + '/', {'x': self.space_x, 'y': self.space_y,
                                                                           'employee_id': self.space_employee_id,
                                                                           'room': {
                                                                               "name": "x"
                                                                           }}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_space_returns_400_when_incorrect(self):
        """
        A PUT request on /spaces/{id} should return 400 when sent incorrectly
        """
        response = self.client.put('/spaces/' + str(self.space.id) + '/', {'incorrectly-typed': ''}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_space_returns_400_when_empty_body(self):
        """
        A PUT request on /spaces/{id} should return a 400 when body is empty
        """
        response = self.client.put('/spaces/' + str(self.space.id) + '/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_space_returns_400_when_invalid_value(self):
        """
        A PUT request on /spaces/{id} should return a 400 when using an invalid value
        """
        response = self.client.put('/spaces/' + str(self.space.id) + '/', {'x': 'a', 'y': self.changed_space_y,
                                                                           'employee_id': self.changed_space_employee_id,
                                                                           'room': {
                                                                               "name": "desk"
                                                                           }}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_space_returns_400_when_missing_required_field(self):
        """
        A PUT request on /spaces/{id} should return a 400 when missing a required field
        """
        response = self.client.put('/spaces/' + str(self.space.id) + '/',
                                   {'y': self.changed_space_y, 'employee_id': self.changed_space_employee_id},
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_space_returns_404_when_not_found(self):
        """
        A PUT request on /spaces/{id} should return a 404 when using an invalid id
        """
        response = self.client.put('/spaces/666/', self.changed_space_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_space_returns_404_when_invalid_characters(self):
        """
        A PUT request on /spaces/{id} should return a 404 when using an invalid id
        """
        response = self.client.put('/spaces/xyz/', self.changed_space_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_space_returns_404_when_negative_id(self):
        """
        A PUT request on /spaces/{id} should return a 404 when using an invalid id
        """
        response = self.client.put('/spaces/-100/', self.changed_space_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_space_returns_200_when_updated(self):
        """
        A PATCH request on /spaces/{id} should return an updated space
        """
        response = self.client.patch('/spaces/' + str(self.space.id) + '/', self.changed_space_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Space.objects.get(id=self.space.id).x, self.changed_space_x)

    def test_patch_space_returns_400_when_invalid_room(self):
        """
            A PATCH request on /spaces/{id} should return 400 when room does not exist
        """
        response = self.client.patch('/spaces/' + str(self.space.id) + '/', {'x': self.space_x, 'y': self.space_y,
                                                                             'employee_id': self.space_employee_id,
                                                                             'room': {
                                                                                 "name": "x"
                                                                             }}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_space_returns_400_when_incorrect(self):
        """
        A PATCH request on /spaces/{id} should return 400 when sent incorrectly
        """
        response = self.client.patch('/spaces/' + str(self.space.id) + '/', {'x': 'xyz'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_space_returns_404_when_not_found(self):
        """
        A PATCH request on /spaces/{id} should return 404 when using an invalid id
        """
        response = self.client.patch('/spaces/666/', self.space_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_space_returns_404_when_invalid_character(self):
        """
        A PATCH request on /spaces/{id} should return 404 when using an invalid id
        """
        response = self.client.patch('/spaces/xyz/', self.space_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_space_returns_404_when_negative_id(self):
        """
        A PATCH request on /spaces/{id} should return 404 when using an invalid id
        """
        response = self.client.patch('/spaces/-100/', self.space_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_space_returns_400_when_empty_body(self):
        """
        A PATCH request on /spaces/{id} should return 400 when body is empty
        """
        response = self.client.patch('/spaces/' + str(self.space.id) + '/', '{}', format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_space_returns_204_when_deleting(self):
        """
        A DELETE request on /spaces/{id} should delete a space
        """
        response = self.client.delete('/spaces/' + str(self.space.id) + '/')
        self.assertEqual(Space.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_space_returns_404_when_not_found(self):
        """
        A DELETE request on /spaces/{id} should return 404 when deleting a non existing space
        """
        response = self.client.delete('/spaces/666/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_space_returns_404_when_invalid_character(self):
        """
        A DELETE request on /spaces/{id} should return 404 when deleting a non existing space
        """
        response = self.client.delete('/spaces/xyz/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_space_returns_404_when_negative_id(self):
        """
        A DELETE request on /spaces/{id} should return 404 when deleting a non existing space
        """
        response = self.client.delete('/spaces/-100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    Tests for the /spaces/ path
    """

    def test_get_all_spaces_returns_200_when_found(self):
        """
        A GET request on /spaces/ should return an array of spaces
        """
        self.client.post('/spaces/', self.changed_space_json, format='json')

        response = self.client.get('/spaces/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Space.objects.count(), 2)

        self.assertIsNotNone(Space.objects.get(x=self.space_x, y=self.space_y))
        self.assertIsNotNone(Space.objects.get(x=self.changed_space_x, y=self.changed_space_y))

    def test_get_all_spaces_returns_200_when_non_found(self):
        """
        A GET request on /spaces/ should still work with no results and return an empty array
        """
        Space.objects.all().delete()
        response = self.client.get('/spaces/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_all_spaces_returns_201_when_correct_format(self):
        """
        A POST request on /spaces/ should create a new space
        """
        Space.objects.all().delete()
        response = self.client.post('/spaces/', self.space_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Space.objects.count(), 1)
        space = Space.objects.first()
        self.assertEqual(space.x, self.space_x)
        self.assertEqual(space.y, self.space_y)
        self.assertEqual(space.employee_id, self.space_employee_id)
        self.assertEqual(space.room, self.space_room)

    def test_post_all_spaces_returns_400_when_invalid_attribute(self):
        """
        A POST request on /spaces/ using the wrong format should return a 400 error
        """
        response = self.client.post('/spaces/', {'x': 'a', 'y': self.changed_space_y,
                                                 'incorrectly-typed': self.changed_space_employee_id,
                                                 'room': {
                                                     "name": "desk"
                                                 }}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Space.objects.count(), 1)

    def test_post_all_spaces_returns_400_when_invalid_value(self):
        """
        A POST request on /spaces/ using the wrong format should return a 400 error
        """
        response = self.client.post('/spaces/', {'x': 'a', 'y': self.changed_space_y,
                                                 'employee_id': self.changed_space_employee_id,
                                                 'room': {
                                                     "name": "desk"
                                                 }}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Space.objects.count(), 1)

    def test_post_all_spaces_returns_400_when_missing_field(self):
        """
        A POST request on /spaces/ using the wrong format should return a 400 error
        """
        response = self.client.post('/spaces/', {'x': self.changed_space_x, 'y': self.changed_space_y}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Space.objects.count(), 1)

    def test_post_all_spaces_returns_400_when_invalid_room(self):
        """
        A POST request on /spaces/ with an invalid room should return a 400 error
        """
        response = self.client.post('/spaces/',
                                    {'x': self.changed_space_x, 'y': self.changed_space_y,
                                     'employee_id': self.changed_space_employee_id,
                                     'room': {
                                         "name": "invalid-name"
                                     }}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Space.objects.count(), 1)

    def test_put_all_spaces_returns_405(self):
        """
        A PUT request on /spaces/ should not be possible
        """
        response = self.client.put('/spaces/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_all_spaces_returns_405(self):
        """
        A PATCH request on /spaces/ should not be possible
        """
        response = self.client.patch('/spaces/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_all_spaces_returns_405(self):
        """
        A DELETE request on /spaces/ should not be possible
        """
        response = self.client.delete('/spaces/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
