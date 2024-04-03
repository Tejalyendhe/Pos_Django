from django.test import TestCase

# Create your tests here.

'''
For Price Update 💶:  added on 27-12-22

For Post i.e. Saving data:

data = {
        'mac_id':'7C-3D-2D-D3-97-22',
        'products':[
         {
        'uniqueNumber':'11AA1197',
        'headline':'Updated SAREE Price',
        'updatedPrice':'3000',
        },
         {
        'uniqueNumber':'11AA1198',
        'headline':'Updated KURTA Price',
        'updatedPrice':'2000',
        },
        ],
    }  
will receive response as ['message']

For Get i.e. Getting data:

  for all data
      data = {
        'mac_id':'7C-3D-2D-D3-97-22',
        'trigger':'0',
        'uniqueNumber':'',

for particular data
      data = {
        'mac_id':'7C-3D-2D-D3-97-22',
        'trigger':'1',
        'uniqueNumber':'11AA1197',

will receive response as ['Product_Data']

'''
