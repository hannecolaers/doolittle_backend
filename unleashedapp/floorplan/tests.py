from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from floorplan.models import Room
from floorplan.serializers import RoomSerializer

from floorplan.models import Space
from floorplan.serializers import SpaceSerializer


def create_room_serializer(data, url, many=False):
    request = APIRequestFactory().get(url)
    serializer = RoomSerializer(data, many=many, context={'request': request})
    return serializer


class RoomTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    """
     Tests for RoomSerializer
    """

    def test_room_serializer_expected_fields(self):
        """
        The serializer should only expect and accept the fields that have been set
        """
        self.room = Room.objects.create(name="TestRoom")
        serializer = create_room_serializer(self.room, '')
        self.assertSetEqual(set(serializer.data.keys()), {'id', 'name'})

    def test_room_serializer_id_field_content(self):
        """
        The id field of a room should contain a value
        """
        self.room = Room.objects.create(name="TestRoom")
        serializer = create_room_serializer(self.room, '')
        self.assertEqual(serializer.data['id'], self.room.id)

    def test_room_serializer_name_field_content(self):
        """
        The name field of a room should contain a value
        """
        self.room = Room.objects.create(name="TestRoom")
        serializer = create_room_serializer(self.room, '')
        self.assertEqual(serializer.data['name'], self.room.name)

    def test_room_serializer_returns_empty_when_no_rooms(self):
        """
        The serializer should return [] when no objects are given
        """
        room = Room.objects.none()
        serializer = create_room_serializer(room, '/', many=True)
        self.assertEqual(serializer.data, [])

    """
    Tests for the /rooms/{id} path
    """

    def test_get_room_returns_200_when_found(self):
        """
        A GET request on /rooms/{id} should return a room
        """
        response = self.client.post('/rooms/', {'name': 'ROOM-NAME'}, format='json')

        pk = Room.objects.get(name='ROOM-NAME').pk
        self.assertEqual(response.data, {'id': pk, 'name': 'ROOM-NAME'})

        response = self.client.get('/rooms/' + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

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
        response = self.client.post('/rooms/666/', {'name': 'ROOM-NAME'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_room_returns_200_when_updated(self):
        """
        A PUT request on /rooms/{id} should return an updated room
        """
        response = self.client.post('/rooms/', {'name': 'OLD-ROOM-NAME'}, format='json')

        pk = Room.objects.get(name='OLD-ROOM-NAME').pk
        self.assertEqual(response.data, {'id': pk, 'name': 'OLD-ROOM-NAME'})

        response = self.client.put('/rooms/' + str(pk) + '/', {'name': 'NEW-ROOM-NAME'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': pk, 'name': 'NEW-ROOM-NAME'})

    def test_put_room_returns_400_when_incorrect(self):
        """
        A PUT request on /rooms/{id} should return 400 when sent incorrectly
        """
        response = self.client.post('/rooms/', {'name': 'OLD-ROOM-NAME'}, format='json')

        pk = Room.objects.get(name='OLD-ROOM-NAME').pk
        self.assertEqual(response.data, {'id': pk, 'name': 'OLD-ROOM-NAME'})

        response = self.client.put('/rooms/' + str(pk) + '/', {'incorrectly-typed': 'NEW-ROOM-NAME'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_room_returns_404_when_not_found(self):
        """
        A PUT request on /rooms/{id} should return a 404 when using an invalid id
        """
        response = self.client.put('/rooms/666/', {'name': 'NEW-ROOM-NAME'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_room_returns_200_when_updated(self):
        """
        A PATCH request on /rooms/{id} should return an updated room
        """
        response = self.client.post('/rooms/', {'name': 'OLD-ROOM-NAME'}, format='json')

        pk = Room.objects.get(name='OLD-ROOM-NAME').pk
        self.assertEqual(response.data, {'id': pk, 'name': 'OLD-ROOM-NAME'})

        response = self.client.patch('/rooms/' + str(pk) + '/', {'name': 'NEW-ROOM-NAME'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': pk, 'name': 'NEW-ROOM-NAME'})

    def test_patch_room_returns_400_when_incorrect(self):
        """
        A PATCH request on /rooms/{id} should return 400 when sent incorrectly
        """
        response = self.client.post('/rooms/', {'name': 'OLD-ROOM-NAME'}, format='json')

        pk = Room.objects.get(name='OLD-ROOM-NAME').pk
        self.assertEqual(response.data, {'id': pk, 'name': 'OLD-ROOM-NAME'})

        response = self.client.patch('/rooms/' + str(pk) + '/', {'name': None}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Incorrect patches return 200
        response = self.client.patch('/rooms/' + str(pk) + '/', {'incorrectly-typed': 666}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_room_returns_404_when_not_found(self):
        """
        A PATCH request on /rooms/{id} should return 404 when using an invalid id
        """
        response = self.client.patch('/rooms/666/', {'name': 'NOT-SEND'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_room_returns_204_when_deleting(self):
        """
        A DELETE request on /rooms/{id} should delete a room
        """
        response = self.client.post('/rooms/', {'name': 'TO-BE-DELETED-ROOM'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        pk = Room.objects.get(name='TO-BE-DELETED-ROOM').pk
        self.assertEqual(response.data, {'id': pk, 'name': 'TO-BE-DELETED-ROOM'})

        response = self.client.delete('/rooms/' + str(pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_room_returns_404_when_not_found(self):
        """
        A DELETE request on /rooms/{id} should return 404 when deleting unexisting room
        """
        response = self.client.delete('/rooms/666/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    Tests for the /rooms/ path
    """

    def test_get_all_rooms_returns_200_when_found(self):
        """
        A GET request on /rooms/ should return an array of rooms
        """
        self.client.post('/rooms/', {'name': 'kitchen'}, format='json')
        self.client.post('/rooms/', {'name': 'lobby'}, format='json')
        response = self.client.get('/rooms/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Room.objects.count(), 2)
        self.assertIsNotNone(Room.objects.get(name='kitchen'))
        self.assertIsNotNone(Room.objects.get(name='lobby'))

    def test_get_all_rooms_returns_200_when_non_found(self):
        """
        A GET request on /rooms/ should still work with no results and return an empty array
        """
        response = self.client.get('/rooms/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Room.objects.count(), 0)

    def test_post_all_rooms_returns_201_when_correct_format(self):
        """
        A POST request on /rooms/ should create a new room
        """
        data = {'name': 'NEW-ROOM-NAME'}
        self.assertEqual(Room.objects.count(), 0)

        response = self.client.post('/rooms/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Room.objects.count(), 1)
        self.assertEqual(Room.objects.get().name, 'NEW-ROOM-NAME')

    def test_post_all_rooms_returns_400_when_bad_format(self):
        """
        A POST request on /rooms/ using the wrong format should return a 400 error
        """
        response = self.client.post('/rooms/', {'incorrectly-typed': 'NEW-ROOM-NAME'}, format='json')
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

    """
     Tests for SpaceSerializer
    """

    def test_space_serializer_expected_fields(self):
        """
        The serializer should only expect and accept the fields that have been set
        """
        self.space = Space.objects.create(x=1)
        serializer = create_space_serializer(self.space, '')
        self.assertSetEqual(set(serializer.data.keys()), {'x', 'y', 'employee_id', 'room_id'})

    def test_space_serializer_x_field_content(self):
        """
        The x field of a space should contain a value
        """
        self.space = Space.objects.create(x=1)
        serializer = create_space_serializer(self.space, '')
        self.assertEqual(serializer.data['x'], self.space.x)

    def test_space_serializer_y_field_content(self):
        """
        The y field of a space should contain a value
        """
        self.space = Space.objects.create(y=1)
        serializer = create_space_serializer(self.space, '')
        self.assertEqual(serializer.data['y'], self.space.y)

    def test_space_serializer_employee_id_field_content(self):
        """
        The employee_id field of a space should contain a value
        """
        self.space = Space.objects.create(employee_id=1)
        serializer = create_space_serializer(self.space, '')
        self.assertEqual(serializer.data['employee_id'], self.space.employee_id)

    def test_space_serializer_room_id_field_content(self):
        """
        The room_id field of a space should contain a value
        """
        self.space = Space.objects.create(room_id=1)
        serializer = create_space_serializer(self.space, '')
        self.assertEqual(serializer.data['room_id'], self.space.room_id)

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
        self.client.post('/spaces/', {'x': 100, 'y': 200, 'employee_id': 1, 'room_id': 2}, format='json')

        pk = Space.objects.get(x=100, y=200, employee_id=1, room_id=2).pk
        self.assertEqual(pk, 4)

        response = self.client.get('/spaces/' + str(pk) + '/')
        self.assertEqual(response.data, {'x': 100, 'y': 200, 'employee_id': 1, 'room_id': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_space_returns_404_when_not_found(self):
        """
        A GET request on /spaces/{id} should return a 404 error when the space doesn't exist
        """
        response = self.client.get('/spaces/666/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_space_returns_405(self):
        """
        A POST request on /spaces/{id} should not be possible
        """
        response = self.client.post('/spaces/666/', {'x': 100, 'y': 200, 'employee_id': 1, 'room_id': 2}, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_space_returns_200_when_updated(self):
        """
        A PUT request on /spaces/{id} should return an updated space
        """
        self.client.post('/spaces/', {'x': 100, 'y': 200, 'employee_id': 1, 'room_id': 2}, format='json')

        pk = Space.objects.get(x=100, y=200, employee_id=1, room_id=2).pk
        self.assertEqual(pk, 8)

        response = self.client.put('/spaces/' + str(pk) + '/', {'x': 300, 'y': 400, 'employee_id': 3, 'room_id': 4},
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'x': 300, 'y': 400, 'employee_id': 3, 'room_id': 4})

    def test_put_space_returns_400_when_incorrect(self):
        """
        A PUT request on /spaces/{id} should return 400 when sent incorrectly
        """
        self.client.post('/spaces/', {'x': 100, 'y': 200, 'employee_id': 1, 'room_id': 2}, format='json')

        pk = Space.objects.get(x=100, y=200, employee_id=1, room_id=2).pk
        self.assertEqual(pk, 9)

        response = self.client.put('/spaces/' + str(pk) + '/', {'incorrectly-typed': 666}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_space_returns_404_when_not_found(self):
        """
        A PUT request on /spaces/{id} should return a 404 when using an invalid id
        """
        response = self.client.put('/spaces/666/', {'x': 300, 'y': 400, 'employee_id': 3, 'room_id': 4}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_space_returns_200_when_updated(self):
        """
        A PATCH request on /spaces/{id} should return an updated space
        """
        self.client.post('/spaces/', {'x': 100, 'y': 200, 'employee_id': 1, 'room_id': 2}, format='json')

        pk = Space.objects.get(x=100, y=200, employee_id=1, room_id=2).pk
        self.assertEqual(pk, 5)

        response = self.client.patch('/spaces/' + str(pk) + '/', {'x': 100, 'y': 200, 'employee_id': 3, 'room_id': 4},
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'x': 100, 'y': 200, 'employee_id': 3, 'room_id': 4})

    def test_patch_space_returns_400_when_incorrect(self):
        """
        A PATCH request on /spaces/{id} should return 400 when sent incorrectly
        """
        self.client.post('/spaces/', {'x': 100, 'y': 200, 'employee_id': 1, 'room_id': 2}, format='json')

        pk = Space.objects.get(x=100, y=200, employee_id=1, room_id=2).pk
        self.assertEqual(pk, 6)

        response = self.client.patch('/spaces/' + str(pk) + '/', {'employee_id': 'invalid-text'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Incorrect patches return 200
        response = self.client.patch('/spaces/' + str(pk) + '/', {'incorrectly-typed': 666}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_space_returns_404_when_not_found(self):
        """
        A PATCH request on /spaces/{id} should return 404 when using an invalid id
        """
        response = self.client.patch('/spaces/666/', {'x': 100, 'y': 200, 'employee_id': 1, 'room_id': 2},
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_space_returns_204_when_deleting(self):
        """
        A DELETE request on /spaces/{id} should delete a space
        """
        response = self.client.post('/spaces/', {'x': 100, 'y': 200, 'employee_id': 1, 'room_id': 2}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Space.objects.count(), 1)

        pk = Space.objects.get(x=100, y=200, employee_id=1, room_id=2).pk
        self.assertEqual(pk, 1)

        response = self.client.delete('/spaces/' + str(pk) + '/')
        self.assertEqual(Space.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_space_returns_404_when_not_found(self):
        """
        A DELETE request on /spaces/{id} should return 404 when deleting unexisting space
        """
        response = self.client.delete('/spaces/666/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    Tests for the /spaces/ path
    """

    def test_get_all_spaces_returns_200_when_found(self):
        """
        A GET request on /spaces/ should return an array of spaces
        """
        self.client.post('/spaces/', {'x': 100, 'y': 200, 'employee_id': 1, 'room_id': 2}, format='json')
        self.client.post('/spaces/', {'x': 300, 'y': 400, 'employee_id': 3, 'room_id': 4}, format='json')
        response = self.client.get('/spaces/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Space.objects.count(), 2)
        self.assertIsNotNone(Space.objects.get(x=100, y=200, employee_id=1, room_id=2))
        self.assertIsNotNone(Space.objects.get(x=300, y=400, employee_id=3, room_id=4))

    def test_get_all_spaces_returns_200_when_non_found(self):
        """
        A GET request on /spaces/ should still work with no results and return an empty array
        """
        response = self.client.get('/spaces/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Space.objects.count(), 0)

    def test_post_all_spaces_returns_201_when_correct_format(self):
        """
        A POST request on /spaces/ should create a new space
        """
        data = {'x': 100, 'y': 200, 'employee_id': 1, 'room_id': 2}
        self.assertEqual(Space.objects.count(), 0)
        response = self.client.post('/spaces/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Space.objects.count(), 1)
        self.assertEqual(Space.objects.get().x, 100)
        self.assertEqual(Space.objects.get().y, 200)
        self.assertEqual(Space.objects.get().employee_id, 1)
        self.assertEqual(Space.objects.get().room_id, 2)

    def test_post_all_spaces_returns_400_when_bad_format(self):
        """
        A POST request on /spaces/ using the wrong format should return a 400 error
        """
        self.assertEqual(Space.objects.count(), 0)
        response = self.client.post('/spaces/', {'incorrectly-typed': 666}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Space.objects.count(), 0)

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
