# Vital Python Library

[![pypi](https://img.shields.io/pypi/v/vital.svg)](https://pypi.python.org/pypi/vital)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

The Vital Python library provides access to the Vital API from applications written in Python.

## Documentation

API reference documentation is available [here](https://docs.tryvital.io/home/welcome).

## Installation

Add this dependency to your project's build file:

```bash
pip install vital
# or
poetry add vital
```

## Usage

```python
from vital.client import Vital

vital_client = Vital(
  api_key="YOUR_API_KEY",
)

lab_test = vital_client.lab_tests.get('order-id')

print(lab_test)
```

## Async Client

The SDK also exports an async client.

```python
from vital.client import AsyncVital

import asyncio

vital_client = AsyncVital(
  api_key="YOUR_API_KEY",
)

async def get_lab_test() -> None:
    lab_test = vital_client.lab_tests.get('order-id')
    print(lab_test)

asyncio.run(get_lab_test())
```

## Handling Errors

All exceptions thrown by the SDK will sublcass [ApiError](./src/vital/core/api_error.py).

```python
from vital.core import ApiError
from vital import BadRequestError

try:
  vital_client.lab_tests.get('order-id')
except BadRequestError as e:
  # handle bad request error
except APIError as e:
  # handle any api related error
```

## Environments

When you sign up to Vital you get access to two environments, Sandbox and Production.

| Environment URLs |                            |
| ---------------- | -------------------------- |
| `production`     | api.tryvital.io            |
| `production-eu`  | api.eu.tryvital.io         |
| `sandbox`        | api.sandbox.tryvital.io    |
| `sandbox-eu`     | api.sandbox.eu.tryvital.io |

By default, the SDK uses the `production` environment. See the snippet below
for an example on how ot change the environment.

```python
from vital.client import Vital
from vital.environment import VitalEnvironment

vital_client = Vital(
  api_key="YOUR_API_KEY",
  environment=VitalEnvironment.Sandbox
)
```

## Timeouts

By default, the client is configured to have a timeout of 60 seconds.
You can customize this value at client instantiation.

```python
from vital.client import Vital
from vital.environment import VitalEnvironment

vital_client = Vital(
  api_key="YOUR_API_KEY",
  environment=VitalEnvironment.Sandbox,
  timeout=15
)
```

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your pyproject.toml file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
