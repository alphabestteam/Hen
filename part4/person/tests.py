from django.test import TestCase
from django.urls import reverse
from .models import Parent,Person
from django.test import Client
import json



class PersonTestCase(TestCase):
    def setUp(self):
        self.kid2 = Person.objects.create(name ="Alice",  id =12345,  birth_data ='1999-3-9' ,city ="Raanana" )
        self.kid1 = Person.objects.create(name ="Bob",  id =54321,  birth_data ='2009-07-09' ,city ="Tel aviv")
        self.parent1 = Parent.objects.create(name="Parent 1",id=67890,birth_data='1990-01-01',city="Raanana",work_place="intel",salary=50000)
        self.parent2 = Parent.objects.create(name="Parent 2",id=98765,birth_data='1980-01-01',city="Raanana",work_place="Google",salary=40000)
        self.parent1.kids.add(54321)
        self.parent1.kids.add(12345)
        self.parent2.kids.add(67890)
        self.client = Client()

    def test_is_adult(self):
        Alice = Person.objects.get(id=12345)
        Bob = Person.objects.get(id=54321)
        self.assertEqual(Alice.is_adult(),True)
        self.assertEqual(Bob.is_adult(),False)

    def test_get_all_parent(self):
        response = self.client.get('/api/getAllParents/')
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content.decode('utf-8'))
        data_length = len(json_data)
        self.assertEqual(data_length, 2)

    def test_get_parent_and_kid(self):
        response = self.client.get(reverse('get_parent_and_kid', args=[self.parent1.id]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['parent ']['id'], self.parent1.id)

    def test_get_parent_and_kid_nonexistent_parent(self):
        response = self.client.get(reverse('get_parent_and_kid', args=[999]))
        self.assertEqual(response.status_code, 400)

    def test_find_parents(self):
        response = self.client.get(reverse('find_parents', args=[self.kid1.id]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        for parent_data in data:
            self.assertIn('id', parent_data)

    def test_find_parents_not_found(self):
        response = self.client.get(reverse('find_parents', args=[999]))
        self.assertEqual(response.status_code, 400)
        
    def test_find_kids(self):
        response = self.client.get(reverse('find_kids', args=[self.parent1.id]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertIn('kids ', data)
        kids_data = data['kids ']
        self.assertIsInstance(kids_data, list)
        self.assertEqual(len(kids_data), 2)

    def test_find_kids_not_found(self):
        response = self.client.get(reverse('find_kids', args=[999]))
        self.assertEqual(response.status_code, 400)

    def test_find_grand(self):
        response = self.client.get(reverse('find_grand', args=[self.kid1.id]))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertIsInstance(data, list)
        self.assertTrue(data)
        self.assertEqual(len(data), 1)
        for grand_parent_data in data:
            self.assertIn('id', grand_parent_data)
            self.assertIn('name', grand_parent_data)
    
    def test_find_grand_not_found(self):
        response = self.client.get(reverse('find_grand', args=[999]))
        self.assertEqual(response.status_code, 400)

    def test_find_brothers(self):
        response = self.client.get(reverse('find_brothers', args=[self.kid1.id]))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertIsInstance(data, list)
        self.assertTrue(data)
        self.assertEqual(len(data), 1)
        for brother_data in data:
            self.assertIn('id', brother_data)
            self.assertIn('name', brother_data)

    def test_find_brother_not_found(self):
        response = self.client.get(reverse('find_brothers', args=[999]))
        self.assertEqual(response.status_code, 400)

    def test_rich_kid(self):
        response = self.client.get(reverse('rich_kid'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertIsInstance(data, list)

    def test_remove_parent(self):
        response = self.client.delete(reverse('remove_parent', args=[self.parent2.id]))
        self.assertEqual(response.status_code, 200)

    def test_remove_nonexistent_parent(self):
        response = self.client.delete(reverse('remove_parent', args=[99999]))
        self.assertEqual(response.status_code, 400)

    def test_add_parent(self):
        parent_data = {
            "name": "Test Parent",
            "id": 4567,
            "birth_data": "1990-01-01",
            "city": "Test City",
            "work_place": "Test Company",
            "salary": 50000,
        }

        response = self.client.post(reverse('add_parent'), data=parent_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        new_parent = Parent.objects.filter(name="Test Parent").first()
        self.assertIsNotNone(new_parent)
    
    def test_add_parent_failure(self):
        parent_data = {
            "name": "Test Parent",
            "salary": 50000,
        }

        response = self.client.post(reverse('add_parent'), data=parent_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

        new_parent = Parent.objects.filter(name="Test Parent").first()
        self.assertIsNone(new_parent)
    
    def test_add_kid_success(self):
        response = self.client.post(reverse('add_kid', args=[self.parent2.id, self.kid2.id]))
        self.assertEqual(response.status_code, 200)
        self.parent2.refresh_from_db()
        self.assertIn(self.kid2, self.parent2.kids.all())

    def test_add_kid_already_exists(self):

        response = self.client.post(reverse('add_kid', args=[self.parent1.id, self.kid1.id]))
        self.assertEqual(response.status_code, 400) 

        self.parent1.refresh_from_db()
        count = self.parent1.kids.filter(id=self.kid1.id).count()
        self.assertEqual(count, 1)

    def test_update_parent_success(self):
        updated_data = {
            "id": self.parent2.id,
            "name": "Updated Parent Name",
            "birth_data": "2000-02-02",
            "city": "New City",
            "work_place": "New Workplace",
            "salary": 60000,
        }
        response = self.client.put(
            reverse("update_parent"),
            data=json.dumps(updated_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.parent2.refresh_from_db()
        self.assertEqual(self.parent2.name, updated_data["name"])

    def test_update_parent_invalid_data(self):
        invalid_data = {
            "name": "Updated Parent Name",
            "birth_data": "2000-02-02",
            "city": "New City",
            "work_place": "New Workplace",
            "salary": 60000,
        }

        response = self.client.put(
            reverse("update_parent"),
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_update_nonexistent_parent(self):

        nonexistent_data = {
            "id": 99999, 
            "name": "Updated Parent Name",
            "birth_data": "2000-02-02",
            "city": "New City",
            "work_place": "New Workplace",
            "salary": 60000,
        }
        response = self.client.put(
            reverse("update_parent"),
            data=json.dumps(nonexistent_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

        






