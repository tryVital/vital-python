## 3.0.0 - 2026-04-10
* Several breaking changes have been made in this release:
* The `INSULIN_INJECTION` enum value has been removed from `IntervalTimeseriesExprTimeseries`. Callers using `.visit(insulin_injection=...)` must remove that argument.
* The `LinkBulkExportRequestTeamId`, `LinkBulkImportRequestTeamId`, `LinkBulkPauseRequestTeamId`, `LinkBulkTriggerHistoricalPullRequestTeamId`, and `LinkListBulkOpsRequestTeamId` types have been removed from `vital.link`.
* `AppointmentPscLabs` has changed from a `Literal["quest"]` type alias to a `StrEnum` class — code using it as a plain string type annotation may need updating.
* New in this release: HTTP requests now support structured logging (debug and error) with automatic redaction of sensitive headers; `BaseHttpResponse` exposes a new `status_code` property; and `AppointmentPscLabs` now includes the `SONORA_QUEST` value.
* **Breaking changes:**
* The `file` parameter of `parser_create_job` (on both `LabReportClient` and `AsyncLabReportClient`) has changed from `core.File` to `typing.List[core.File]`. Callers must now wrap a single file in a list: `file=[my_file]`.
* The following types have been removed from the top-level `vital` package: `LinkBulkExportRequestTeamId`, `LinkBulkImportRequestTeamId`, `LinkBulkPauseRequestTeamId`, `LinkBulkTriggerHistoricalPullRequestTeamId`, and `LinkListBulkOpsRequestTeamId`.
**New features:**
* Three new resource submodules are now available: `vital.compendium`, `vital.lab_account`, and `vital.order_transaction`.
* Over 40 new public types have been added, including `CanonicalCandidate`, `ClientFacingLabAccount`, `ClientFacingOrderTransaction`, `InsulinInjectionTimeseriesExpr`, `OrderSummary`, `SearchCompendiumResponse`, `UsState`, `UserAddress`, and more.
* Client wrappers now accept an optional `logging` parameter for structured request/response logging (`LogConfig` or `Logger`).
* The `LabTestsClient` (sync and async) has been expanded with several new parameters and types:
* `get_psc_appointment_availability` now accepts a required `lab` parameter (`AppointmentPscLabs`) and a new optional `allow_stale` flag for cached availability data.
* `book_psc_appointment` now supports optional `idempotency_key` and `idempotency_error` parameters for idempotent PSC appointment booking (currently in closed beta).
* `create_lab_test` accepts new optional `lab_account_id` and `lab_slug` (`Labs`) parameters.
* `get_markers` accepts a new optional `lab_slug` parameter to filter markers by lab slug.
* `get_orders` accepts a new optional `order_transaction_id` parameter for filtering.
* `request_phlebotomy_appointment` accepts a new optional `appointment_notes` parameter.
* `create_order` accepts a new optional `clinical_notes` parameter.
* New types `AppointmentPscLabs` and `Labs` are now available for use with these methods.
* The `get_psc_appointment_availability` method now requires a `lab` parameter (of type `AppointmentPscLabs`) that was previously hardcoded to `"quest"`. Callers must now explicitly pass the desired lab value. Additionally, many lab test and appointment methods have new optional parameters: `lab_account_id`, `lab_slug`, `order_transaction_id`, `appointment_notes`, `allow_stale`, `clinical_notes`, and idempotency support (`idempotency_key`, `idempotency_error`) for PSC appointment booking.
* The `team_id` parameter has been removed from `link.list_bulk_ops()`, `link.bulk_import()`, `link.bulk_trigger_historical_pull()`, `link.bulk_export()`, and `link.bulk_pause()` — callers using this keyword argument must remove it. The associated enum types (`LinkBulkExportRequestTeamId`, `LinkBulkImportRequestTeamId`, `LinkBulkPauseRequestTeamId`, `LinkBulkTriggerHistoricalPullRequestTeamId`, `LinkListBulkOpsRequestTeamId`) have also been removed.
* `link.connect_manual_provider()` now accepts three new optional parameters: `vital_ios_sdk_version`, `vital_android_sdk_version`, and `granted_permissions`, enabling mobile SDK version reporting and explicit permission grants.
* The SDK introduces several breaking changes alongside new features.
**Breaking changes:**
* The `address` parameter type in user creation/update methods (`UserClient`, `RawUserClient`) has changed from `Address` to `UserAddress`. Update all imports and usages accordingly (e.g., replace `from vital import Address` with `from vital import UserAddress`).
* `ParsingJob.job_id` has been removed. Use `ParsingJob.id` to identify parsing jobs.
* `Jpeg.content` and `Png.content` now use `bytes` instead of `str`.
**New features:**
* Three new top-level clients are now available on `Vital` and `AsyncVital`: `compendium`, `lab_account`, and `order_transaction`.
* A new optional `logging` parameter is available on `Vital` and `AsyncVital` constructors, accepting a `LogConfig` dict or a `Logger` instance for configurable SDK-level logging.
* `ClientFacingOrder` now exposes `last_event`, `clinical_notes`, `origin`, and `order_transaction` fields.
* `ClientFacingInsulinInjectionSample` gains optional `delivery_mode`, `delivery_form`, and `bolus_purpose` fields.
* `OrderStatus` includes new enum values for corrected results and lab-processing-blocked states.
* The SDK now includes two new client namespaces: `compendium` (with `search` and `convert` methods for lab test discovery and cross-lab conversion) and `lab_account` (with `get_team_lab_accounts` for managing team lab accounts). A new structured logging module (`ILogger`, `ConsoleLogger`, `LogConfig`, `Logger`, `create_logger`) is also available via `vital.core`.
* The SDK now includes a new `order_transaction` client namespace with three methods: `get_transaction()`, `get_transaction_result()`, and `get_transaction_result_pdf()`. These methods provide access to order transaction details, raw lab results, and streamable PDF lab result reports respectively. Both synchronous and asynchronous variants are available.
* The SDK now exposes many new types and enum values. New types include lab account management (`ClientFacingLabAccount`, `GetTeamLabAccountsResponse`, `LabAccountDelegatedFlow`, `LabAccountStatus`), order transactions (`ClientFacingOrderTransaction`, `ClientFacingOrderInTransaction`, `GetOrderTransactionResponse`, `OrderTransactionStatus`, `OrderOrigin`, `OrderStatusDetail`, `OrderSummary`), compendium search (`SearchCompendiumResponse`, `CompendiumSearchLabs`, `ConvertCompendiumResponse`, `SearchMode`, `CanonicalCandidate`, `PerLabCandidate`, `RelatedCandidate`), insulin injection details (`ClientFacingInsulinInjectionSampleBolusPurpose`, `ClientFacingInsulinInjectionSampleDeliveryForm`, `ClientFacingInsulinInjectionSampleDeliveryMode`), and sleep analytics (`AwakeningsValueMacroExpr`, `DerivedReadinessColumnExpr`). Several existing models have gained new optional fields, and new enum values have been added to `AppointmentProvider` (`SONORA_QUEST`) and source-type enums (`INSULIN_PUMP`).
* The SDK now includes new types and fields to support insulin injection timeseries, lab account management, order transactions, lab report parsing job webhook events, and compendium search/conversion. New optional fields `recovery_readiness_score` (on `ClientFacingSleep`), `status_detail` (on `ClientFacingOrderEvent`), and `order_transaction` (on `LabResultsRaw`) are also available. Several enums have been expanded with new values including `SONORA_QUEST`, `CRL`, `SAMSUNG_HEALTH`, `INSULIN_PUMP`, `CORRECTED`, `LAB_PROCESSING_BLOCKED`, and `DERIVED_READINESS`.
* The SDK now includes several new types and capabilities: `OrderStatusDetail`, `OrderTransactionStatus`, and `OrderSummary` for richer order lifecycle tracking; `SearchCompendiumResponse`, `PerLabCandidate`, `RelatedCandidate`, and `ProviderIdConversionResponse` for compendium search and provider ID conversion; and `UserAddress` with `UsState` enum for US address handling. New providers `TANDEM_SOURCE` and `SAMSUNG_HEALTH` have been added to the `Providers` enum, `TANDEM_SOURCE` to `PasswordProviders`, and `APERO`/`PVERIFY` to `PayorCodeExternalProvider`. Address models (`PatientAddress`, `PatientAddressCompatible`, `PatientAddressWithValidation`, `UsAddress`) now include an optional `access_notes` field, and query expression union types have been expanded with `AwakeningsValueMacroExpr`, `DerivedReadinessColumnExpr`, and `InsulinInjectionTimeseriesExpr`.

