# Vital Python Library [![Vital](https://img.shields.io/badge/Project%20by-Vital-009688)](https://tryvital.io)

[![PyPI Version](https://img.shields.io/pypi/v/vital.svg)](https://pypi.python.org/pypi/vital)
[![Python Versions](https://img.shields.io/pypi/pyversions/vital.svg)](https://pypi.org/project/vital/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/tryvital/vital-python/ci.yml?branch=main)](https://github.com/tryvital/vital-python/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Code Coverage](https://img.shields.io/codecov/c/github/tryvital/vital-python)](https://codecov.io/gh/tryvital/vital-python)
[![Documentation](https://img.shields.io/badge/docs-API%20Reference-blue)](https://docs.tryvital.io)
[![FERN Shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

The Vital Python SDK provides robust, enterprise-grade connectivity to Vital's Health Data Platform. Designed for scalability and reliability, this official library enables seamless integration of health data capabilities into your applications.

## Key Features

- **Production-Ready**: Battle-tested in high-availability environments
- **Multi-Environment Support**: Sandbox & production instances across regions
- **Type-Hinted**: Full PEP 484 type annotations for IDE support
- **Async Ready**: Native async/await support for high-performance applications
- **Comprehensive Error Handling**: Structured exceptions with detailed diagnostics
- **Configurable Timeouts**: Adaptive timeout strategies for network resilience
- **Security First**: TLS verification and secret management best practices

## Table of Contents

- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [Environments](#environments)
- [Usage Examples](#usage-examples)
- [Synchronous Client](#synchronous-client)
- [Asynchronous Client](#asynchronous-client)
- [Error Handling](#error-handling)
- [Logging](#logging)
- [Testing](#testing)
- [Security](#security)
- [Compliance](#compliance)
- [Support](#support)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

1. **Install the SDK**:

   ```bash
   pip install vital
    ```

2. Configure Client

   ```python
   from vital import Vital, VitalEnvironment
   
   client = Vital(
       api_key="YOUR_API_KEY",
       environment=VitalEnvironment.PRODUCTION_EU,
       timeout=30
   )
   ```

3. Execute API call

   ```python
   try:
       lab_report = client.lab_tests.get('REPORT_123')
       print(f"Retrieved lab report: {lab_report.id}")
   except Vital.APIError as e:
       print(f"API Error: {e.status_code} - {e.message}")
   ```

## Installation

### Requirements

- Python 3.8+
- pip >= 20.3

### Package Managers

**pip**:

```bash
pip install vital
```

**poetry**:

```bash
poetry add vital
```

**conda** (via conda-forge):

```bash
conda install -c conda-forge vital
```

## Configuration

### Client Options

| Parameter     | Type               | Default      | Description                   |
| ------------- | ------------------ | ------------ | ----------------------------- |
| `api_key`     | `str`              | **Required** | Your Vital API credential     |
| `environment` | `VitalEnvironment` | `PRODUCTION` | Target deployment environment |
| `timeout`     | `float`            | `60.0`       | Global timeout in seconds     |
| `max_retries` | `int`              | `3`          | Automatic retry attempts      |
| `api_version` | `str`              | `v2`         | API version specification     |

```python
from vital import Vital, VitalEnvironment

client = Vital(
    api_key="prod_XXXXXX",
    environment=VitalEnvironment.SANDBOX_EU,
    timeout=45.0,
    max_retries=5
)
```

## Environments

Vital provides isolated environments for different stages of development:

| Environment   | Region | Base URL                             | Purpose                   |
| ------------- | ------ | ------------------------------------ | ------------------------- |
| Production    | US     | `https://api.tryvital.io`            | Live customer data        |
| Production EU | EU     | `https://api.eu.tryvital.io`         | GDPR-compliant processing |
| Sandbox       | US     | `https://api.sandbox.tryvital.io`    | Development & testing     |
| Sandbox EU    | EU     | `https://api.sandbox.eu.tryvital.io` | EU-compliant testing      |

```python
# EU GDPR-compliant production environment
client = Vital(
    api_key="prod_eu_XXXX",
    environment=VitalEnvironment.PRODUCTION_EU
)
```

## Usage Examples

### Synchronous Client

```python
# Retrieve patient lab results
patient_id = "PATIENT_123"
lab_orders = client.lab_tests.get_orders(patient_id=patient_id)

for order in lab_orders:
    print(f"Order {order.id}: {order.status}")
    report = client.lab_tests.get(order.id)
    print(f"Report PDF: {report.pdf_url}")
```

### Asynchronous Client

```python
import asyncio
from vital import AsyncVital

async def fetch_patient_data(patient_id: str):
    async with AsyncVital(api_key="YOUR_KEY") as client:
        devices = await client.devices.get(patient_id)
        workouts = await client.workouts.get(patient_id)
        return {
            "devices": [d.name for d in devices],
            "workouts": [w.type for w in workouts]
        }

# Run async workflow
data = asyncio.run(fetch_patient_data("PATIENT_789"))
print(f"Connected devices: {data['devices']}")
```

## Error Handling

The SDK uses structured error classes for precise exception management:

```python
from vital import (
    APIError,
    AuthenticationError,
    RateLimitError,
    ServerError,
    ServiceUnavailableError
)

try:
    client.users.get("user_123")
except AuthenticationError as e:
    print(f"Auth failure: {e.headers.get('X-Vital-Trace-ID')}")
except RateLimitError as e:
    print(f"Rate limited: Retry after {e.retry_after} seconds")
except ServiceUnavailableError:
    client.retry_request()
except APIError as e:
    print(f"Error {e.status_code}: {e.body}")
```

## Logging

Enable diagnostic logging:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
client = Vital(api_key="...")

# Will log HTTP transactions
client.activities.get("ACT_123")
```

## Testing

### Mocking API Responses

```python
from vital.responses import MockLabReport
from unittest.mock import patch

@patch('vital.client.Vital.lab_tests.get')
def test_lab_report(mock_get):
    mock_get.return_value = MockLabReport(id='MOCK_123')
    report = client.lab_tests.get('MOCK_123')
    assert report.id == 'MOCK_123'
```

Run test suite:

```bash
python -m pytest tests/
```

## Security

### Secret Management

We recommend using environment variables for credentials:

```python
import os

client = Vital(
    api_key=os.getenv("VITAL_API_KEY"),
    environment=os.getenv("VITAL_ENV")
)
```

### TLS Verification

The SDK verifies TLS certificates by default. To configure:

```python
client = Vital(
    api_key="...",
    tls_cert_path="/path/to/cert.pem",
    tls_verify=True  # Default
)
```

## Compliance

Vital environments comply with:

- HIPAA (Production US)
- GDPR (Production EU)
- SOC 2 Type II
- ISO 27001

Contact [security@tryvital.io](mailto:security@tryvital.io) for compliance documentation.

## Support

| Channel    | Availability       | Contact                                                                    |
| ---------- | ------------------ | -------------------------------------------------------------------------- |
| Enterprise | 24/7               | support@tryvital.io (Priority)                                             |
| Standard   | Business Hours     | support@tryvital.io                                                        |
| Community  | GitHub Discussions | [GitHub Discussions](https://github.com/tryvital/vital-python/discussions) |

## Contributing

While this SDK is generated programmatically, we welcome:

- Documentation improvements
- Test case additions
- Bug reports via [GitHub Issues](https://github.com/tryvital/vital-python/issues)

Please read our [Contribution Guide](https://github.com/tryvital/.github/blob/main/CONTRIBUTING.md) before submitting PRs.

## License

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)  
[![Compliance](https://img.shields.io/badge/HIPAA-Compliant-brightgreen)](https://tryvital.io/compliance)  
[![Warranty](https://img.shields.io/badge/Warranty-As%20Provided%20in%20MIT-red)](https://opensource.org/licenses/MIT)

**Copyright (c) 2025 Vital Technologies Inc.**  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for full legal text.

### Compliance Note for Enterprises

- Contains explicit patent grant in license terms  
- Includes healthcare-specific warranty disclaimer  
- Third-party dependencies documented in [NOTICES.md](NOTICES.md)  
- Export controlled under ECCN 5D992.c (EU Dual-Use Regulation compliance)

*For enterprise licensing options or GDPR addendum requests, contact [legal@tryvital.io](mailto:legal@tryvital.io).*

> **Beta Notice**  
> This SDK is currently in beta. We recommend pinning versions in your requirements:

> ```python
> # pyproject.toml
> [tool.poetry.dependencies]
> vital = "==0.1.2"
> ```

> Subscribe to our [Release Notes](https://docs.tryvital.io/changelog) for updates.
```