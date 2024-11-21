# Reference
## Link
<details><summary><code>client.link.<a href="src/vital/link/client.py">token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to generate a user link token, to be used throughout the vital
link process. The vital link token is a one time use token, that
expires after 10 minutes. If you would like vital-link widget to launch
with a specific provider, pass in a provider in the body. If you would
like to redirect to a custom url after successful or error connection,
pass in your own custom redirect_url parameter.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.token(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — User id returned by vital create user request. This id should be stored in your database against the user and used for all interactions with the vital api.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[Providers]` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_on_providers:** `typing.Optional[typing.Sequence[Providers]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">is_token_valid</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.is_token_valid(
    token="token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">code_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a token to invite a user of Vital mobile app to your team
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.code_create(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">start_connect</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

REQUEST_SOURCE: VITAL-LINK
Start link token process
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Providers, Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.start_connect(
    link_token="link_token",
    provider=Providers.OURA,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `Providers` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">token_state</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

REQUEST_SOURCE: VITAL-LINK
Check link token state - can be hit continuously used as heartbeat
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.token_state()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vital_link_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">email_auth</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated. Use `POST /v2/link/provider/email/{provider}` instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import AuthType, Providers, Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.email_auth(
    email="email",
    provider=Providers.OURA,
    auth_type=AuthType.PASSWORD,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `Providers` 
    
</dd>
</dl>

<dl>
<dd>

**auth_type:** `AuthType` 
    
</dd>
</dl>

<dl>
<dd>

**vital_link_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">password_auth</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated. Use `POST /v2/link/provider/password/{provider}` instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import AuthType, Providers, Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.password_auth(
    username="username",
    password="password",
    provider=Providers.OURA,
    auth_type=AuthType.PASSWORD,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `Providers` 
    
</dd>
</dl>

<dl>
<dd>

**auth_type:** `AuthType` 
    
</dd>
</dl>

<dl>
<dd>

**vital_link_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">generate_oauth_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint generates an OAuth link for oauth provider
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import OAuthProviders, Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.generate_oauth_link(
    oauth_provider=OAuthProviders.OURA,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**oauth_provider:** `OAuthProviders` 
    
</dd>
</dl>

<dl>
<dd>

**vital_link_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">connect_password_provider</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This connects auth providers that are password based.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import PasswordProviders, Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.connect_password_provider(
    provider=PasswordProviders.WHOOP,
    username="username",
    password="password",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `PasswordProviders` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — Username for provider
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — Password for provider
    
</dd>
</dl>

<dl>
<dd>

**vital_link_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">complete_password_provider_mfa</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This connects auth providers that are password based.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import PasswordProviders, Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.complete_password_provider_mfa(
    provider=PasswordProviders.WHOOP,
    mfa_code="mfa_code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `PasswordProviders` 
    
</dd>
</dl>

<dl>
<dd>

**mfa_code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**vital_link_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">connect_email_auth_provider</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This connects auth providers that are email based.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.connect_email_auth_provider(
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**vital_link_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_provider_auth_link_provider:** `typing.Optional[Providers]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">get_all_providers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

GET List of all available providers given the generated link token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.get_all_providers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vital_link_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">connect_manual_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import ManualProviders, Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.connect_manual_provider(
    provider=ManualProviders.BEURER_BLE,
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `ManualProviders` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/vital/link/client.py">connect_demo_provider</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

POST Connect the given Vital user to a demo provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import DemoProviders, Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.link.connect_demo_provider(
    user_id="user_id",
    provider=DemoProviders.APPLE_HEALTH_KIT,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Vital user ID
    
</dd>
</dl>

<dl>
<dd>

**provider:** `DemoProviders` — Demo provider. For more information, please check out our docs (https://docs.tryvital.io/wearables/providers/test_data)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SleepCycle
<details><summary><code>client.sleep_cycle.<a href="src/vital/sleep_cycle/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily sleep cycle for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.sleep_cycle.get(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Profile
<details><summary><code>client.profile.<a href="src/vital/profile/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily profile for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.profile.get(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profile.<a href="src/vital/profile/client.py">get_raw</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily profile for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.profile.get_raw(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Devices
<details><summary><code>client.devices.<a href="src/vital/devices/client.py">get_raw</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Devices for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.devices.get_raw(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Activity
<details><summary><code>client.activity.<a href="src/vital/activity/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily Activity for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.activity.get(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activity.<a href="src/vital/activity/client.py">get_raw</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily Activity for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.activity.get_raw(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Workouts
<details><summary><code>client.workouts.<a href="src/vital/workouts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily workout for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.workouts.get(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workouts.<a href="src/vital/workouts/client.py">get_raw</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily workout for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.workouts.get_raw(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workouts.<a href="src/vital/workouts/client.py">get_by_workout_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.workouts.get_by_workout_id(
    workout_id="workout_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workout_id:** `str` — The Vital ID for the workout
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sleep
<details><summary><code>client.sleep.<a href="src/vital/sleep/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily sleep for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.sleep.get(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sleep.<a href="src/vital/sleep/client.py">get_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily sleep stream for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.sleep.get_stream(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sleep.<a href="src/vital/sleep/client.py">get_raw</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily sleep for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.sleep.get_raw(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sleep.<a href="src/vital/sleep/client.py">get_stream_by_sleep_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Sleep stream for a user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.sleep.get_stream_by_sleep_id(
    sleep_id="sleep_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sleep_id:** `str` — The Vital Sleep ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Body
<details><summary><code>client.body.<a href="src/vital/body/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily Body data for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.body.get(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.body.<a href="src/vital/body/client.py">get_raw</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Daily Body data for user_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.body.get_raw(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Meal
<details><summary><code>client.meal.<a href="src/vital/meal/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get user's meals
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.meal.get(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## MenstrualCycle
<details><summary><code>client.menstrual_cycle.<a href="src/vital/menstrual_cycle/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.menstrual_cycle.get(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Vitals
<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">workout_duration_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.workout_duration_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">vo_2_max_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.vo_2_max_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">stress_level_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.stress_level_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">mindfulness_minutes_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.mindfulness_minutes_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">caffeine_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.caffeine_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">water_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.water_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">steps_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.steps_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">floors_climbed_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.floors_climbed_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">distance_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.distance_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">calories_basal_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.calories_basal_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">calories_active_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.calories_active_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">respiratory_rate_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.respiratory_rate_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">note_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.note_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">insulin_injection_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.insulin_injection_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">ige_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.ige_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">igg_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.igg_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">hypnogram_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.hypnogram_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">hrv_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.hrv_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">heartrate_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.heartrate_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">glucose_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.glucose_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">cholesterol_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.cholesterol_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">carbohydrates_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.carbohydrates_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">body_temperature_delta_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.body_temperature_delta_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">body_temperature_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.body_temperature_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">body_weight_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.body_weight_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">body_fat_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.body_fat_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">blood_oxygen_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.blood_oxygen_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">electrocardiogram_voltage_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.electrocardiogram_voltage_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">blood_pressure_grouped</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.blood_pressure_grouped(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**next_cursor:** `typing.Optional[str]` — The cursor for fetching the next page, or `null` to fetch the first page.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">vo_2_max</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.vo_2_max(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">stress_level</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.stress_level(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">mindfulness_minutes</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vital import Vital

client = Vital(
    api_key="YOUR_API_KEY",
)
client.vitals.mindfulness_minutes(
    user_id="user_id",
    start_date="start_date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `str` — Date from in YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 00:00:00
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider oura/strava etc
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Date to YYYY-MM-DD or ISO formatted date time. If a date is provided without a time, the time will be set to 23:59:59
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vitals.<a href="src/vital/vitals/client.py">caffeine</a>(...)</code></summary>
