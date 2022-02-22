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
<!-- Dates have to be url encoded -->
start_date =  (datetime.now()-timedelta(days=1)).isoformat())
end_date = datetime.now().isoformat()

client.Link.create(user_id="user_id")
client.Body.get(user_id=**,start_date, end_date)
client.Activity.get(user_id=**,start_date, end_date)
client.Sleep.get(user_id=**,start_date, end_date)
client.User.create(client_user_id=**)
client.User.providers(user_id=**)
client.User.get(client_user_id=**)


from vital.types import WebhookEventCodes, WebhookType

client.Webhooks.test(WebhookEventCodes.HISTORICAL_DATA_UPDATE,
                     WebhookType.ACTIVITY)
```

# Installing locally

```
poetry build --format sdist
tar -xvf dist/*-`poetry version -s`.tar.gz -O '*/setup.py' > setup.py
```
