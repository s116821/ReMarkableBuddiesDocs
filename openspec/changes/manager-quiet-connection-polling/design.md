## Existing behavior and selected repair

ConnectionController.connect explicitly publishes checking and clears current details. Its private read also publishes checking before every adapter call, so the four-second automatic poll repeatedly removes the successful observation. Only connect and the successful-read timer invoke read.

Preserve explicit connect's pending transition; automatic read must not publish a pending replacement. The last completed observation remains a historical verified sample while a new read is in flight; checkedAt advances only after a successful result. Existing result validation, identity comparison, cancellation generation and failure-stops-polling behavior remain unchanged. A returned failure or device change clears current details exactly as before. No new spinner, animation, live-region update or notification starts for the automatic attempt.

The current UI displays the verification timestamp. Retaining it must not imply a newly successful verification or install/update eligibility. No hiding an actual error, silent target switching or automatic reconnect is authorized.

## Delivery and evidence

Publish this central precode before source changes. Prepare a narrow successor topic from the current PR8 CI-propagated source, preserving its Windows qualification limits. Focused deferred-adapter controls must observe the in-flight interval, successful refresh, explicit pending, failure and disconnect/late-result races; existing identity-change controls remain. Verify source lint/type/build where applicable, with supported runtime versus supplemental runtime distinguished. Paired exact-head review and required CI precede canonical sync/archive or merge; original physical observations are not repeated for this shared-controller presentation change.
