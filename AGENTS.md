# AGENTS.md

Building: FitNova Sales-Call Intelligence prototype. Spec: assignment PDF. Plan: `PLAN.md`.
`PLAN.md` is authoritative for stack/structure/endpoints/sequencing — don't contradict it without
updating it first, in its own commit.

## Step 0 — once, before any component
- [ ] `git init`, `.gitignore`, initial scaffold commit to `main` (folders, `docker-compose.yml`
      with 3 services [db/api/dashboard], `Dockerfile.api`, `Dockerfile.dashboard`,
      `.dockerignore`, `.env.example`, `requirements.txt`, empty `README.md`, `BUILD_LOG.md`).
      Confirm `docker-compose up --build` starts before writing any component logic — every
      component from here on builds and tests against Docker, not a bare local install.
- [ ] System design diagram (Excalidraw/Mermaid) → `docs/00-system-design.md`. The written
      walkthrough in that file MUST explicitly name which pipeline stages automation adds the
      most value to, and justify that prioritisation — this is a graded requirement in the
      assignment's Section A, not satisfied by the diagram alone.

## Per-component checklist — run this exact sequence, every component, no skipping
1. [ ] Re-read `PLAN.md` + the relevant PDF section.
2. [ ] `git checkout -b feature/<component>`.
3. [ ] Build smallest working version. One file = one job.
4. [ ] Write/run its test. Fix until green.
5. [ ] Optimize only after green. Re-run test.
6. [ ] Add one docstring per file (what + why-this-approach) and per non-trivial function.
7. [ ] Write `docs/<NN>-<component>.md` (template below).
8. [ ] Update `README.md` if setup/run changed, or something moved real<->mocked.
9. [ ] Tick the item in `PLAN.md` §7.
10. [ ] Push branch -> open PR -> confirm tests pass -> merge -> tag milestone.
11. [ ] Add one row to `BUILD_LOG.md`.

If stuck >1hr on any step: stop, write the blocker + fallback in the writeup, move to the next
`PLAN.md` item. A working prototype with a documented gap beats a stalled build.

## `docs/<component>.md` template (~20 lines max)
```
# <Component>
What it does:
Why built this way (key decision + alternative not picked):
Inputs / outputs:
Edge cases handled here:
Known gaps:
```

## `BUILD_LOG.md` — one row per merge
```
| Date/Time | Component | Branch | What was built | Test result | PR | Status |
```

## Git rules
- Never commit straight to `main` except scaffold + doc-only fixes.
- Commit messages: `feat(scope): ...`, `fix(scope): ...`, `test(scope): ...`, `docs: ...`, `chore: ...`.
- Commit at each checkpoint (build passes / test passes / optimized), not just at branch end.
- Broke something on `main`? Fix in a `fix/` branch, PR it, merge, log it — before new work.

## Code style
- One docstring per file/non-trivial function. Skip trivial getters.
- Inline comments only for non-obvious *decisions*, never narration of obvious code.
- No commented-out dead code.
- If a function needs 3+ inline comments to follow, split it instead.

## Non-negotiables
- Every tag's `quoted_line` verified against transcript before storage (`verifier.py`).
- `llm_client.py`: Gemini first, auto-fallback to Groq. Rest of codebase calls one function.
- `orchestrator.py` idempotent — check `calls.status` before reprocessing.
- Ingestion adapters implement `base_adapter` — no vendor-specific code outside that layer.
- README's real-vs-mocked section stays accurate the moment anything changes.
- Every service (db/api/dashboard) runs via `docker-compose up --build` — no component is "done"
  if it only works with a bare local Python install.
- The system is deployed (Render) with a working public link before submission — this is required,
  not a stretch item.

## Last hour
- [ ] README accurate (setup — both `docker-compose up --build` locally and the deployed link,
      real-vs-mocked).
- [ ] `BUILD_LOG.md` has an entry per merged component, including the deploy component.
- [ ] Fresh clone + `docker-compose up --build` works.
- [ ] Deployed Render link (API + dashboard) works independently — open it in a fresh incognito
      window, don't just trust that it deployed.
- [ ] Zip repo for submission.
- [ ] Record 2-min video (trade-offs, what's cut and why, where it'd fail).
- [ ] Verify the video link's sharing permission is public/accessible — not restricted to a
      specific account. Open it in a fresh incognito window to confirm before submitting.

## Done = all six
Passing test + docstring + `docs/<component>.md` + PR merged + `BUILD_LOG.md` row +
`PLAN.md` checkbox ticked.
