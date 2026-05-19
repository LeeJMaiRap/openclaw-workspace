# Track 4 — Browser / UI Evidence Recovery Acceptance Criteria

## Track Acceptance

Track 4 is accepted when:

```text
browser readiness matrix exists
browser install approval packet refresh exists
executable discovery dry-run exists
fallback browser-like boundary is documented
real browser proof protocol exists
dry-run rejects browser/a11y/visual overclaims
runbooks preserve explicit install approval requirements
```

## Claim Acceptance Criteria

```text
real browser claim requires executable path + launch output
screenshot claim requires real browser artifact path
a11y claim requires raw scan output and tool provenance
visual claim requires captured artifact and comparison rule
browser-like fallback must be labelled fallback
missing executable keeps status Blocked
```

## Rejection Criteria

Reject claims when:

```text
browser executable missing
install/download not approved
artifact missing
raw command output missing
a11y/visual tooling unapproved or unavailable
browser cloud/deploy path requested without explicit approval
```

## Stop Conditions

Stop and ask before:

```text
running browser install/download
installing browser-related package
using cloud browser provider
using deploy/cloud/DNS/billing/secrets path
calling fallback proof real browser proof
claiming a11y/visual/screenshot evidence without artifacts
```
