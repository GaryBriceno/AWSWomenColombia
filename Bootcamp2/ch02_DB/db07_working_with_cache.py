'''

key = get_key(parameters)

data = get_from_cache(key)
if data:
   return data
else:
   data = get_data_from_db(parameters)
   put_data_in_cache(key, data)
   return data

'''
