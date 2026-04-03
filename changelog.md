## 3.0.0 - 2026-04-03
* Several breaking changes are included in this release:
* The `INSULIN_INJECTION` enum member and its corresponding `insulin_injection` visitor argument have been removed from `IntervalTimeseriesExprTimeseries`. Callers using `.visit(insulin_injection=...)` must update their code.
* The `LinkBulkExportRequestTeamId`, `LinkBulkImportRequestTeamId`, `LinkBulkPauseRequestTeamId`, `LinkBulkTriggerHistoricalPullRequestTeamId`, and `LinkListBulkOpsRequestTeamId` types have been removed along with the `vital.link.types` subpackage; any imports of these symbols will fail.
* `AppointmentPscLabs` has been changed from a plain `Literal["quest"]` type alias to a full `StrEnum` class — code that used it as a literal type annotation may need adjustment.
* New in this release: HTTP requests and responses are now optionally logged (with sensitive headers automatically redacted), `BaseHttpResponse` exposes a new `status_code` property, and a `sonora_quest` value has been added to `AppointmentPscLabs`.
* The `parser_create_job` method on `LabReportClient` and `AsyncLabReportClient` now accepts a list of files (`typing.List[core.File]`) instead of a single `core.File` for the `file` parameter — callers must wrap their existing file argument in a list. The symbols `LinkBulkExportRequestTeamId`, `LinkBulkImportRequestTeamId`, `LinkBulkPauseRequestTeamId`, `LinkBulkTriggerHistoricalPullRequestTeamId`, and `LinkListBulkOpsRequestTeamId` have been removed from public exports. New submodules `compendium`, `lab_account`, and `order_transaction` are now available, along with 40+ new types covering order transactions, lab accounts, compendium search, insulin injection detail, and more.
* The `lab_tests` client now supports additional optional parameters across several methods:
* `create_lab_test` accepts new `lab_account_id` and `lab_slug` parameters for specifying the lab account and lab identity.
* `get_markers` accepts a new `lab_slug` parameter to filter markers by lab slug (takes precedence over `lab_id` when both are provided).
* Order listing accepts a new `order_transaction_id` parameter to filter orders by transaction ID.
* `request_phlebotomy_appointment` accepts a new `appointment_notes` parameter.
* `get_psc_appointment_availability` now accepts a required `lab` parameter (`AppointmentPscLabs`) and an optional `allow_stale` flag to allow cached availability data.
* `book_psc_appointment` accepts optional `idempotency_key` and `idempotency_error` parameters for idempotent booking (closed beta).
* `create_order` accepts a new optional `clinical_notes` parameter.
* Two new types — `AppointmentPscLabs` and `Labs` — are now available for import.
* The lab tests and appointment APIs now support several new optional parameters:
* Lab test creation accepts `lab_account_id` and `lab_slug` for specifying the lab account and lab slug.
* `get_markers` accepts a `lab_slug` parameter to filter markers by lab slug.
* Order listing accepts `order_transaction_id` to filter by transaction ID.
* Appointment scheduling accepts `appointment_notes` for additional notes.
* PSC appointment booking supports `idempotency_key` and `idempotency_error` parameters (closed beta) for idempotent requests.
* `get_psc_appointment_availability` now accepts a required `lab` parameter (type `AppointmentPscLabs`) to specify the lab, replacing the previously hardcoded `"quest"` value, and an optional `allow_stale` flag to permit cached results.
* Order creation accepts `clinical_notes` for attaching clinical notes to an order.
* New types `AppointmentPscLabs` and `Labs` are available for use with the updated methods.
* The `team_id` parameter has been removed from the following `link` client methods: `list_bulk_ops`, `bulk_import`, `bulk_export`, `bulk_trigger_historical_pull`, and `bulk_pause`. Callers passing `team_id` (including using the now-removed `LinkBulkExportRequestTeamId`, `LinkBulkImportRequestTeamId`, `LinkBulkPauseRequestTeamId`, `LinkBulkTriggerHistoricalPullRequestTeamId`, and `LinkListBulkOpsRequestTeamId` enum types) must remove those arguments. Additionally, `connect_manual_provider` now accepts new optional parameters `vital_ios_sdk_version`, `vital_android_sdk_version`, and `granted_permissions`.
* Several breaking changes and new features are included in this release.
**Breaking changes:**
* The `Address` type used in `UserClient.create_user_info()` (and the raw client equivalent) has been renamed to `UserAddress`. Update all imports and call sites from `Address` to `UserAddress`.
* `ParsingJob` no longer exposes a `job_id` field — remove any references to `parsing_job.job_id` in consuming code.
* `Jpeg.content` and `Png.content` have changed from `str` to `bytes` — update any code that reads or assigns these fields as strings.
**New features:**
* Three new sub-clients are now available on the `Vital` and `AsyncVital` top-level clients: `compendium` (with `search` and `convert` methods), `lab_account`, and `order_transaction`.
* `ClientFacingOrder` gains `last_event`, `clinical_notes`, `origin`, and `order_transaction` optional fields.
* `ClientFacingInsulinInjectionSample` gains optional `delivery_mode`, `delivery_form`, and `bolus_purpose` fields.
* `ResultMetadata` gains an optional `gender` field, and its `patient_first_name`, `patient_last_name`, `dob`, and `lab_name` fields are now optional.
* `ParsingJob` gains an optional `failure_reason` field.
* Both `Vital` and `AsyncVital` constructors now accept an optional `logging` parameter for configuring SDK-level logging.
* The SDK now includes three new client namespaces: `lab_account` (retrieve team lab accounts with optional filtering), `order_transaction` (fetch order transaction details, results, and PDF reports), and an expanded `compendium` raw client (search and convert compendium entries). A new structured logging subsystem (`ILogger`, `ConsoleLogger`, `Logger`, `LogConfig`, `LogLevel`, `create_logger`) is also available via `vital.core`. Additionally, a bug fix in the JSON encoder ensures that `OMIT` sentinel values are correctly excluded from serialized request payloads.
* The SDK now includes a new `OrderTransaction` client with methods to retrieve order transaction details (`get_transaction`), raw lab results (`get_transaction_result`), and streaming PDF results (`get_transaction_result_pdf`). Approximately 40 new public types have been added to `vital.types`, including `ClientFacingOrderTransaction`, `ClientFacingLabAccount`, `GetOrderTransactionResponse`, `OrderTransactionStatus`, `SearchCompendiumResponse`, and more. The `Address` model also gains an optional `access_notes` field.
* The SDK now supports insulin injection timeseries data with new `ClientFacingInsulinInjectionSample*` enums (BolusPurpose, DeliveryForm, DeliveryMode) and a new `InsulinInjectionTimeseriesExpr` expression type. Sonora Quest has been added as a supported lab and appointment provider (`AppointmentProvider.SONORA_QUEST`, `ClientFacingLabs.SONORA_QUEST`). New models are available for order transactions (`ClientFacingOrderTransaction`, `GetOrderTransactionResponse`), lab account management (`ClientFacingLabAccount`, `GetTeamLabAccountsResponse`), lab report parsing job webhook events, and compendium search/conversion (`CompendiumSearchLabs`, `ConvertCompendiumResponse`). Additionally, `ClientFacingSleep` now includes a `recovery_readiness_score` field, and appointment booking/reschedule requests support `appointment_notes` and async confirmation options.
* The SDK now includes several new types and enum values to support expanded lab account management, order lifecycle tracking, and provider integrations. New enums include `InsulinInjectionTimeseriesExprField`, `LabAccountDelegatedFlow`, `LabAccountStatus`, `OrderOrigin`, `OrderStatusDetail`, `OrderTransactionStatus`, and `ParsingJobFailureReason`. New model types `OrderSummary`, `PerLabCandidate`, `ProviderIdConversionResponse`, and `RelatedCandidate` are now available. Existing models `PatientAddress`, `PatientAddressCompatible`, `PatientAddressWithValidation`, and `LabResultsRaw` have new optional fields (`access_notes` and `order_transaction` respectively), and multiple enums have been extended with new values including `SAMSUNG_HEALTH`, `TANDEM_SOURCE`, `SONORA_QUEST`, `CRL`, `APERO`, `PVERIFY`, `CORRECTED`, and `LAB_PROCESSING_BLOCKED`.
* The SDK now includes several new types to support expanded API functionality: `ResultMetadataGender`, `SearchMode`, `SearchCompendiumResponse`, `UsState`, and `UserAddress` are newly available. The existing `UsAddress` model gains an optional `access_notes` field, and `SleepColumnExprSleep` now includes the `RECOVERY_READINESS_SCORE` enum value.

