# Quality Gates

## Purpose

Prevent low-quality or incomplete work from moving forward.

## Gate List

```text
1. Requirement Gate
2. Architecture Gate
3. API Contract Gate
4. Planning Gate
5. Implementation Gate
6. Integration Gate
7. QA Gate
8. Review Gate
9. Handoff Gate
```

## 1. Requirement Gate

Pass when:

- goal is clear
- scope and out-of-scope are documented
- acceptance criteria exist
- unknowns are resolved or tracked

## 2. Architecture Gate

Pass when:

- stack and architecture are justified
- module boundaries exist
- data flow is clear
- solution is not overcomplicated

## 3. API Contract Gate

Pass when:

- FE/BE contract exists
- request/response/error schemas are clear
- auth rules are clear
- contract change process exists

## 4. Planning Gate

Pass when:

- tasks have owners
- dependencies are known
- owned/forbidden paths are defined
- verification exists for each task
- parallel plan has no ownership conflicts

## 5. Implementation Gate

Pass when:

- agent reports include evidence
- changed files stay inside owned paths
- acceptance criteria are met or blockers documented

## 6. Integration Gate

Pass when:

- parts work together
- env/config issues are resolved or documented
- full-app verification ran where applicable

## 7. QA Gate

Pass when:

- acceptance criteria verified
- tests/manual checks run
- bugs are reported with reproduction steps

## 8. Review Gate

Pass when:

- security/performance/code review findings are handled or accepted as known risk

## 9. Handoff Gate

Pass when:

- setup/run/deploy docs exist where needed
- known issues documented
- rollback path documented
- user receives concise summary
