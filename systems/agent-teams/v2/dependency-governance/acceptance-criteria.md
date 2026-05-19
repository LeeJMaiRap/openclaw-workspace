# Dependency / Toolchain Governance Acceptance Criteria

## Phase 51 Acceptance

Phase 51 is accepted if:

```text
v2 directory exists
v2 roadmap exists
Dependency Governance plan exists
acceptance criteria exists
Phase 51 verification report exists
no install/download occurs
no runtime/app/test changes occur
no PM Agent changes occur
no deploy/cloud/DNS/billing/secrets changes occur
```

## Track 1 Acceptance

Track 1 is complete when Agent-Teams can safely process dependency/toolchain needs using explicit approval and evidence.

Required outputs:

```text
dependency approval request template
dependency risk review template
toolchain preflight matrix
install provenance log template
lockfile policy
starter/runbook wiring
dry-run approval simulation
```

## Dependency Request Must Include

```text
package/tool name
version or version range
install command
reason
owner/task
risk category
lockfile impact
fallback if rejected
verification command
rollback/removal plan
```

## PM Review Must Decide

```text
Approved
Rejected
Needs More Info
Fallback Approved
Blocked
```

## Install Execution Evidence Must Include

```text
exact approved command
command output/log
changed files list
lockfile/package metadata diff
version check
verification result
provenance log entry
```

## Rejection Rules

PM must reject or block if:

```text
install command is vague
reason is unclear
risk is unstated
lockfile impact is unknown
fallback/block behavior is missing
approval is not explicit
worker already installed before approval
```

## Claim Boundaries

```text
Package installed != feature verified
Tool available != tests passed
Browser package installed != browser proof
Fallback proof != real tool proof
Dependency approval != production approval
```
