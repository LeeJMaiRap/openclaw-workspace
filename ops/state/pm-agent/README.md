# PM Agent Runtime State

Small runtime snapshots for PM Agent operations.

## Use for

- report selector state;
- last-run timestamps;
- temporary scan summaries;
- non-secret runtime metadata.

## Do not use for

- project source of truth;
- secrets/tokens/passwords;
- large cache/build output;
- final PM artifacts.

Project source of truth belongs in `projects/[lifecycle]/[project-name]/`. Framework source belongs in `systems/pm-agent/`.
