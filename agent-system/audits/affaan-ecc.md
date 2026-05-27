# Audit: affaan-ecc

## Source

https://github.com/affaan-m/ecc

## Purpose

Large engineering/agent-harness skill collection covering architecture, audits, testing, automation, and agent systems.

## Useful Candidates

- TBD

## Candidate Agents

- TBD

## Keep

- TBD

## Reject or Modify

- Agent-specific install assumptions not valid for OpenClaw.
- Unsafe commands, prompt overrides, or auto-execution steps.
- Unneeded scripts/dependencies.

## Dependencies

- TBD

## License

- TBD

## Risk

- TBD: Low / Medium / High

## Decision

Use selectively. Audit carefully before adapting due broad scope.

## Notes

- Status: draft audit.
- Next step: inspect individual `SKILL.md` files before adaptation.

## Phase 4 Architecture Skill Notes — 2026-05-26

Inspected via GitHub API:

- `.agents/skills/` list includes architecture-adjacent skills:
  - `api-design`
  - `backend-patterns`
  - `frontend-patterns`
  - `coding-standards`
  - `documentation-lookup`
  - `e2e-testing`
- Root repo has many agent/tool directories; treat all as untrusted until individual skill files are audited.

Combined with `awesome-llm-apps/fullstack-developer` architecture sections for first adaptation pass.

Keep:

- frontend/backend file structure patterns;
- API/data/security boundary thinking;
- validation, error contract, N+1/query/performance awareness;
- specialist separation between architecture, frontend, backend, QA.

Modify:

- Do not import ECC runtime/tool config.
- Do not run/install anything from ECC.
- Convert broad patterns into OpenClaw architecture decision workflow.

Decision:

Adapt `software/software-architecture` to `status: reviewed` for Paper-level architecture design tasks. Further deep audit of specific ECC skills can improve it later.

## Phase 4 Affiliate Strategy Notes

Inspected `market-research` and `content-engine`. Keep decision-oriented research, source/fact/inference separation, risks/caveats, source-first content system, platform-native drafts. Adapt for affiliate strategy without auto-posting or outreach.

Decision: adapt `affiliate/affiliate-strategy` to reviewed Paper-level strategy skill for Business PM Agent.
