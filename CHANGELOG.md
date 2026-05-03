# Changelog

All notable changes to ROGAllyTDP are documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

ROGAllyTDP is a derivative of [SimpleDeckyTDP](https://github.com/aarron-lee/SimpleDeckyTDP),
narrowed in scope to the ROG Ally Z1 Extreme on SteamOS. History prior to the
fork point is recorded in upstream SimpleDeckyTDP's release notes; this
changelog tracks divergence from the fork.

## [Unreleased]

### Added
- Expose `mcuVersion` and `mcuPowersaveSafe` from `get_power_control_info`
  so the frontend can warn users on MCU firmware below the safe threshold
  (319 for original Ally, 314 for Ally X).
- New `mcu_powersave_safe()` helper in `devices/rog_ally.py` with documented
  minimum-version constants.
- `migrate_from_simpledecky_tdp()` migration: on first run, if a
  `~/homebrew/settings/SimpleDeckyTDP/settings.json` exists and this
  plugin's settings file is empty, the upstream settings (per-game
  profiles, etc.) are copied over so users don't lose configuration when
  switching from upstream SimpleDeckyTDP. Wired into `_migration()` so it
  runs before any code reads the new settings file.

### Changed
- Plugin renamed end-to-end: `plugin.json`, `package.json`, all install
  / OTA / dev-reload scripts, `i18n.py` paths, `plugin_update.py` paths
  and GitHub API URL, `ryzenadj.py` fallback path, `main.py` log strings,
  and the frontend display name in `src/index.tsx` now use `ROGAllyTDP`.
  This also avoids any conflict with an existing SimpleDeckyTDP install
  on the same device (different plugin id, different settings dir).
- `set_platform_profile` now matches `platform_profile_choices` by name
  (`low-power` / `quiet` / `balanced` / `performance`) with a fallback chain,
  instead of indexing positions `[0]/[1]/[2]`. Fixes incorrect profile
  selection on SteamOS kernels that expose 4 entries (with `low-power`).
- `on_resume` now re-applies EPP and power governor for the Ally immediately,
  to work around SteamOS issue #2383 where EPP on CPUs 1..N is reset to
  `performance` after wake on `amd-pstate-epp`. Closes the ~3.5 s gap before
  the JS-side resume action fires.
- `on_suspend` SMT-on workaround is now scoped to the ROG Ally series only,
  rather than running unconditionally on every device.
- `supports_cpu_boost()` returns `False` on the Ally when running
  `amd-pstate-epp` in `active` mode (SteamOS 3.7.5+ default), since
  per-policy boost writes silently revert under that driver. The toggle
  is hidden instead of presenting a non-functional control.
- `package.json` version reset to `0.1.0` to reflect that this is a
  standalone project, not a continuation of upstream's `1.0.x` series.

### Documentation
- Added `CLAUDE.md` with project-scope and language rules.
- Added this `CHANGELOG.md`.
- Added `update-docs` skill under `.claude/skills/` to formalise
  documentation-update workflow.

## [0.1.0] — 2026-05-03

Initial release of ROGAllyTDP as a standalone project, forked from
SimpleDeckyTDP 1.0.2.

### Changed
- Rebranded `README.md` to `ROGAllyTDP`, scoped explicitly to ROG Ally
  Z1 Extreme on SteamOS. Removed sections covering Steam Deck, Legion Go,
  Intel handhelds, ChimeraOS / Bazzite-specific instructions, ryzenadj
  troubleshooting, and the SimpleDeckyTDP Desktop App.
- Repository detached from the GitHub fork relationship; standalone
  project at `ThaFridge/ROGAllyTDP`.

### Credits
- Built on the work of [SimpleDeckyTDP](https://github.com/aarron-lee/SimpleDeckyTDP)
  by Aarron Lee. License (BSD 3-Clause) and attribution preserved.
