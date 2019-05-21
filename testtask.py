url = 'https://stackoverflow.com/questions/19472616/how-to-populate-a-field-in-a-django-model'
url = 'https://stackoverflow.com'

res = '/'.join(url.split('/')[3:])


print(res)