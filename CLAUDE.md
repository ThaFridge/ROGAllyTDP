# ROGAllyTDP — Project Rules for Claude

## Scope

This project is a Decky Loader plugin scoped exclusively to:

- **Hardware**: ASUS ROG Ally (RC71L) with Ryzen **Z1 Extreme** only.
- **OS**: **SteamOS** only (3.7+).

Multi-device, multi-distro, and Intel branches that exist in the upstream
[SimpleDeckyTDP](https://github.com/aarron-lee/SimpleDeckyTDP) are progressively
being removed. Do not reintroduce them. If a fix is generic, it still belongs
here only if it benefits the Z1E + SteamOS combination.

## Language

- **All commit messages, code comments, identifiers, and documentation
  (README, CHANGELOG, in-repo docs) must be written in English.**
- Conversation with the user may be in Dutch; that does not change the above.

## Documentation discipline

- After any change that affects user-visible behaviour, features, install/build
  flow, configuration, scope, or known-issue lists, update both:
  - `README.md` — the section relevant to the change.
  - `CHANGELOG.md` — under `## [Unreleased]`, in [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) style.
- Pure refactors / formatting / non-user-visible changes do not require
  documentation updates, but should still get a CHANGELOG entry under
  `Changed` if they touch enough code to be worth noting.
- The `update-docs` skill at `.claude/skills/update-docs/SKILL.md` formalises
  this — invoke it when finishing a change set.

## Commits

- One logical change per commit. Don't batch unrelated work.
- Commit message subject in imperative mood, English, ≤ 72 chars.
- Use a Conventional-Commit-ish prefix where it fits: `feat:`, `fix:`,
  `docs:`, `refactor:`, `chore:`. Not strict.
- Body explains *why*, not *what* — the diff already shows what.

## Credits

Upstream SimpleDeckyTDP by Aarron Lee is the foundation of this project and
must remain credited in `README.md` and `LICENSE`. Do not remove attribution.
