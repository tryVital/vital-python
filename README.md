# vital-python

The official Python Library for [Vital API](docs.tryvital.io)


# Install
```
pip install plaid-python
```

# Calling Endpoints

```
from vital import Client

# Available environments are 'sandbox', 'development', and 'production'.
client = Client(client_id='***', secret='***', environment='sandbox')
```

# Supported Endpoints

```
client.LinkToken.create(client_user_id="test_id")
client.Body.get(user_id=**,start_date="2020-01-01", end_date="2020-10-10")
client.Activity.get(user_id=**,start_date="2020-01-01", end_date="2020-10-10")
client.Sleep.get(user_id=**,start_date="2020-01-01", end_date="2020-10-10")
client.SourceSpecific.get(user_id=**,start_date="2020-01-01", end_date="2020-10-10")

```
