# Project Rules

This is the canonical Conduit message protocol repository: JSON Schema for the message envelope, transport-binding docs, and cross-client conformance fixtures. It intentionally contains no client implementation.

Priorities:

- Keep everything here language-neutral. Nothing in this repo should assume Node.js, Python, or any other specific client.
- Transport-specific behaviour (routing keys, exchange/queue names, ack state, persistence settings) belongs in `transports/`, never in the envelope schema or `meta`.
- `causationId` on a child message is a non-overridable invariant: it is always the parent's `id`. `streamId`/`correlationId` inheritance is default-with-override; their deeper semantics aren't fully settled yet — don't invent stronger rules for them without checking first.
- New or changed conformance fixtures must validate against `schemas/conduit-message.schema.json` before committing. There's no CI for this yet, so check by hand (see `conformance/README.md` for the fixture format).
- `conduit-node-client` is still the reference implementation. This repo is the spec, but the two can silently drift — if a change here affects derivation rules, check it against what `conduit-node-client` actually does.

Before editing:

- Explain the intended change.
- Prefer small diffs.
- Validate any new/changed fixture or schema edit before committing.

Git workflow:

- Branch off `origin/main`, push the branch, and open a PR (`gh pr create`) rather than pushing directly, even though this repo doesn't currently enforce branch protection.
- Use the `gh` CLI for push/PR/merge operations rather than the GitHub web UI.
- Keep unrelated changes on separate branches/PRs rather than bundling them.
- Squash-merge is this org's convention (`gh pr merge --squash --delete-branch`).
