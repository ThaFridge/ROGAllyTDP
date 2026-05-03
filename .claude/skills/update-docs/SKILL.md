---
name: update-docs
description: Use proactively after making any user-visible or behaviour-changing code change in the ROGAllyTDP repo (features, install/build flow, scope, defaults, troubleshooting items, sysfs paths, settings keys, plugin metadata, hardware/OS support). Reviews the diff and updates README.md and CHANGELOG.md so they accurately reflect the current state of the code. All output in English.
---

# update-docs

Keep `README.md` and `CHANGELOG.md` in sync with the code.

## When to invoke

Run this skill whenever a change set includes anything that a user or
contributor would notice from outside the code:

- New, removed, or changed plugin features.
- Changes to install / update / uninstall steps, paths, or `install.sh`.
- Changes to manual-build steps or dependencies.
- Changes to supported hardware or OS scope.
- Changes to defaults, recommended settings, or known-good profiles.
- New troubleshooting items (or invalidated existing ones).
- Renames of plugin name, settings file, or sysfs paths the user might see.
- Changes to `plugin.json`, `package.json` name/version, or licence.
- New external project credits.

Skip for: pure formatting, internal refactors with no behaviour change,
test-only changes, build-system tweaks invisible to the user. Those still
deserve a one-line `Changed` entry in CHANGELOG if non-trivial.

## Procedure

1. **Inventory the change set.** Run `git status` and `git diff` (staged and
   unstaged) to know exactly what changed. Don't skip this — the skill's
   value is grounded in the actual diff, not a memory of intent.

2. **Decide what each change implies for the docs.** For every changed file
   ask: does it alter anything documented in README? Does a user need to
   know about it?

3. **Update `README.md`** in place. Edit the specific sections affected.
   Do not add sections speculatively. If a feature was removed, delete its
   bullet and any references.

4. **Update `CHANGELOG.md`.** Add entries under `## [Unreleased]` in
   [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) style:
   - `### Added` for new capabilities.
   - `### Changed` for changes to existing behaviour.
   - `### Deprecated` for soon-to-be-removed features.
   - `### Removed` for removed features.
   - `### Fixed` for bug fixes.
   - `### Security` for vulnerability fixes.
   - `### Documentation` only when the change is purely docs/repo meta.

   Each entry: one bullet, present tense, English, references the affected
   module/file when it helps the reader. Mention the *why* if non-obvious
   (e.g. linking to a SteamOS / kernel issue).

5. **Cut a release section when the user asks** (not automatically). When
   cutting `[X.Y.Z] — YYYY-MM-DD`, move the contents of `[Unreleased]` into
   the new version block, leave `[Unreleased]` empty (with the standard
   subsection headers ready to be filled), and pick the version per
   [SemVer](https://semver.org/):
   - `MAJOR` — incompatible changes (settings format, plugin ID, removed
     features users rely on).
   - `MINOR` — new features in a backwards-compatible way.
   - `PATCH` — backwards-compatible bug fixes only.

6. **Re-read** `README.md` end-to-end after editing. The whole file should
   describe the project as it stands *now*, not as it was. Stale references
   (old plugin name, old paths, retired features) are bugs.

## Style rules

- English only. Match the existing README tone (concise, technical, no
  marketing language).
- Code, paths, and identifiers in backticks.
- External project names get a link the first time they appear in a section.
- Don't add emojis unless the user has explicitly opted in.
- Don't add comments to code as part of doc updates — code-level commentary
  belongs in the code change itself.

## Output

After running, summarise to the user:

- Which sections of README were touched.
- Which CHANGELOG entries were added (and under which subsection).
- Anything that *seemed* like it needed doc updates but you decided didn't
  (so the user can sanity-check the judgement call).

Do not commit. Leave the staging decision to the user.
