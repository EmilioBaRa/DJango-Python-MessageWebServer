from django.db import models
from django.core.exceptions import ValidationError

#
# PURPOSE:
# Given a string analyze for uniqueness on the KeyAndMessages class
#
# PARAMETERS:
# 'key' contains the key entered in the HTML /msgserver/create/
#
# RETURN/SIDE EFFECTS:
# Raises an error if the key is a duplicate
#
# NOTES:
# The key is only analyzed for uniqueness in this function, other validations are on functions
# length_key and valid_characters_key
# This is only step 1 for the key validation
#
def unique_key(key):
    for row in KeyAndMessage.objects.all():
        if row.key == key:
            raise ValidationError('Key is already in use', code='duplicate')

#
# PURPOSE:
# Given a string analyze that is length equals to 8
#
# PARAMETERS:
# 'key' contains the key entered in the HTML /msgserver/create/
#
# RETURN/SIDE EFFECTS:
# Raises an error if the key length is different from 8
#
# NOTES:
# The key is only analyzed for length in this function, other validations are on functions
# unique_key and valid_characters_key
# This the step 2 for the key validation
#
def length_key(key):
    if not len(key) == 8:
        raise ValidationError('Length must be 8', code='length')

#
# PURPOSE:
# Given a string analyze if it is made only of alphanumeric characters
#
# PARAMETERS:
# 'key' contains the key entered in the HTML /msgserver/create/
#
# RETURN/SIDE EFFECTS:
# Raises an error if the key is not formed only by numbers and letters
#
# NOTES:
# The key is only analyzed for being alphanumeric in this function, other validations are on functions
# unique_key and length_key
# This is the step 3 for the key validation
#
def valid_characters_key(key):
    if not key.isalnum():
        raise ValidationError('Key must be alphanumeric', code='alphanumeric')

class KeyAndMessage(models.Model):
    key = models.CharField(max_length=8, validators=[valid_characters_key, length_key, unique_key])
    message = models.CharField(max_length=160)

#
# PURPOSE:
# Given a database row return a string of that row
#
# PARAMETERS:
# 'row' contains one of the KeyAndMessage class object rows
#
# RETURN/SIDE EFFECTS:
# Formats the style of the row fields 'key' and 'message'
#
# NOTES:
# The function expects a valid row sent into the function
#
    def __str__(row):
        return str(row.key) + ':' + row.message + '\n'
