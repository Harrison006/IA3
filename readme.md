# Digital Solutions IA3 2023

this is an IA3 for QCAA digital solutions.

### Modules needed
- Requests
- Black
```python
# Test code boilerplate 1

db = Datastore()
api_test = db.function('var1')

print(api_test)
```

### Boilerplate API call
```python
    def get_password(self, username):
        # url for Api Calls
        base_url = "https://api.nottelling.github/api/get_password?username={}"
        # format url to add var's
        url = base_url.format(username)
        # outputting the whole API call in JSON
        response = requests.get(url)
        json_respnose = response.json()
        return json_respnose
```