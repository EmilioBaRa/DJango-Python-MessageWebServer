from django.shortcuts import render
from msgserver.models import KeyAndMessage
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
import json

#
# PURPOSE:
# Search for a row of type KeyAndMessage based on a given key,
# if it exists print it as HTML code
#
# PARAMETERS:
# 'key' contains the value that is going to be searched between the KeyAndMessage objects
# 'request' allows to inspect the type of the key parameter, in this casse expects a KeyAndMessage type
#
# RETURN/SIDE EFFECTS:
# Prints on a HTML file the key and message of the object found, if the object is not found
# prints in HTML 'No such element'
#
# NOTES:
# This function is expected to be called when a user enters to the /msgserver/get/ link.
# This function only returns objects of type KeyAndMessage
#
def get_message(request, key):
    rows = KeyAndMessage.objects.filter(key=key)
    if (len(rows) == 1):
        return HttpResponse(str(rows[0].key) + ': ' + rows[0].message)
    else:
        return HttpResponse("No such element")

class Create_Message(CreateView):
    model = KeyAndMessage
    fields = '__all__'
    success_url = reverse_lazy('messages')

class Update_Message(UpdateView):
#
# PURPOSE:
# Take as the primary key value the key column of the KeyAndMessage object
#
# PARAMETERS:
# 'queryset' is a select SQL statement, we are assigning it to no first because it first has to identify the key
# value as the primary key
# 'self' allows to inspect the KeyAndMessage class
#
# RETURN/SIDE EFFECTS:
# Makes DJango take the column key as if it was the primary key
#
# NOTES:
# It is expected that the user gives a correct value, in this case, self has to matc a key in the
# KeyAndMessage objects
#
    def get_object(self, queryset=None):
        return KeyAndMessage.objects.get(key=self.kwargs.get("key"))
    model = KeyAndMessage
    fields = ['message']
    success_url = reverse_lazy('messages')

class MessageEncoderJSON(json.JSONEncoder):
#
# PURPOSE:
# Given an object of type KeyAndMessage, change the format to JSON
#
# PARAMETERS:
# 'obj' contains the KeyAndMessage object
# 'self' alloows to inspect the class of obj parameter
#
# RETURN/SIDE EFFECTS:
# if the object exists in the KeyAndMessage class then return it into a formatted form
# in case the object is not of type KeyAndMessage return a default JSON format of that object
#
# NOTES:
# This method expects to always get an object of type KeyAndMessage, but in case it is not of KeyAndMessage type,
# use the default JSON encoder format
#
    def default(self, obj):
        if isinstance(obj, KeyAndMessage):
            return { 'key' : obj.key, 'message' : obj.message }
        return json.JSONEncoder.default(self, obj)

#
# PURPOSE:
# Get all the KeyAndMessage objects, list them and change the format into JSON
#
# PARAMETERS:
# 'object' contains the link status of /msgserver/
#
# RETURN/SIDE EFFECTS:
# It is expected to return a JSON format of all the KeyAndMessages objects in HTML
#
# NOTES:
# It is expected to be called when the user enters to /msgserver/
#
def get_all_messages(object):
    rows = KeyAndMessage.objects.all()
    objectJSON = json.dumps(list(rows), cls=MessageEncoderJSON)
    return HttpResponse(objectJSON)
