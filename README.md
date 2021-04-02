# vital-python

The official Python Library for [Vital API](https://docs.tryvital.io)


# Install
```
pip install vital
```

# Calling Endpoints

```
from vital import Client

# Available environments are 'sandbox', 'development', and 'production'.
client = Client(client_id='***', secret='***', environment='sandbox')
```

# Supported Endpoints

```
client.LinkToken.create(user_key="user_key")
client.Body.get(user_key=**,start_date="2020-01-01", end_date="2020-10-10")
client.Activity.get(user_key=**,start_date="2020-01-01", end_date="2020-10-10")
client.Sleep.get(user_key=**,start_date="2020-01-01", end_date="2020-10-10")
client.SourceSpecific.get(user_key=**,start_date="2020-01-01", end_date="2020-10-10")
client.User.create(client_user_id=**)
client.User.providers(user_key=**)
```
