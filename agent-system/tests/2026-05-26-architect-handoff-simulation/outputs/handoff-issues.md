# Architect Handoff Issues

| Issue | Severity | Owner | Resolution |
|---|---|---|---|
| Persistence decision unresolved | High for implementation | PM Adapter / Doanh | decide local state vs localStorage vs API/DB |
| No implementation task packet | High for implementation | PM Adapter | create Specialist Task Packet before code |
| No Local preflight | High for runtime claim | PM Adapter | run preflight before Local verification |
| Architect role could overreach into implementation | Medium | Architect Agent | keep ADR/boundary only unless assigned implementation |

## Decision

Architect Agent adds value by making boundaries/ADRs explicit and reducing Frontend/Backend ambiguity.
