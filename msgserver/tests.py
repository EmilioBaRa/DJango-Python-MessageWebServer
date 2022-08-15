from django.test import TestCase
from msgserver.models import KeyAndMessage
#import msgserver.constants

# Create your tests here.
class MessagesTesting(TestCase):

    def test_create_retrieve_message(self):
        response = self.client.post("/msgserver/create/",{ 'key':'12345678', 'message':'Hello World' })
        createdMessage = KeyAndMessage.objects.filter(key='12345678')
        self.assertEqual(createdMessage[0].key, '12345678')
        self.assertEqual(createdMessage[0].message, 'Hello World')
        response = self.client.post("/msgserver/get/12345678/")
        self.assertIn(b'12345678: Hello World', response._container[0])

    def test_unique_key(self):
        response = self.client.post("/msgserver/create/",{ 'key':'12345678', 'message':'Hello world' })
        response = self.client.post("/msgserver/create/",{ 'key':'12345678', 'message':'Unique?' })
        createdMessage = KeyAndMessage.objects.filter(key='12345678')
        self.assertEqual(createdMessage[0].message, 'Hello world')
        self.assertIn(b'Key is already in use', response._container[0])

    def test_constraints(self):
        key = ''
        for x in range(7):
            key = key + str(x)
            response = self.client.post("/msgserver/create/",{ 'key':key, 'message':'Unique?' })
            self.assertIn(b'Length must be 8', response._container[0])
        #User cannot enter more than 8 length values in key

        response = self.client.post("/msgserver/create/",{ 'key':'999?9999', 'message':'Alphanumeric Key?' })
        self.assertIn(b'Key must be alphanumeric', response._container[0])
        response = self.client.post("/msgserver/create/",{ 'key':'999.9999', 'message':'Alphanumeric Key?' })
        self.assertIn(b'Key must be alphanumeric', response._container[0])
        response = self.client.post("/msgserver/create/",{ 'key':'999_9999', 'message':'Alphanumeric Key?' })
        self.assertIn(b'Key must be alphanumeric', response._container[0])

    def test_update_message(self):
        response = self.client.post("/msgserver/create/",{ 'key':'12345678', 'message':'Hello World' })
        response = self.client.post("/msgserver/update/12345678/",{ 'message':'Updated!' })
        createdMessage = KeyAndMessage.objects.get(key='12345678')
        self.assertEqual(createdMessage.key, '12345678')
        self.assertEqual(createdMessage.message, 'Updated!')


    def test_JSON_retrieved(self):
         response = self.client.post("/msgserver/create/",{ 'key':'12345678', 'message':'Test JSON' })
         response = self.client.post("/msgserver/")
         print(response.content)
         self.assertEqual(b'[{"key": "12345678", "message": "Test JSON"}]', response.content)
