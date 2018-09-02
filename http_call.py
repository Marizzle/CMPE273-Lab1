
import requests

web_hook_url = 'https://webhook.site/00ad0d5b-4adb-4206-b94c-94e1e14ef5db'

for i in range (0,3):
    r = requests.get(web_hook_url)
    print(r.headers['Date'])
