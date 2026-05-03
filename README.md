# ROGAllyTDP

A Decky Loader plugin for TDP and power management, tailored exclusively for the **ASUS ROG Ally (RC71L) with the AMD Ryzen Z1 Extreme**, running on **SteamOS**.

![plugin screenshot](./img/recent.jpg)

> **Note**: this is a focused derivative of [SimpleDeckyTDP](https://github.com/aarron-lee/SimpleDeckyTDP). If you are not on a ROG Ally Z1 Extreme on SteamOS, please use the upstream project instead.

- [About this project](#about-this-project)
- [Scope](#scope)
- [Features](#features)
- [Requirements](#requirements)
- [Install](#install)
- [Manual build](#manual-build)
- [Uninstall](#uninstall)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)
- [License](#license)

## About this project

ROGAllyTDP is a standalone derivative of the excellent **[SimpleDeckyTDP](https://github.com/aarron-lee/SimpleDeckyTDP)** by **Aarron Lee** and contributors.

SimpleDeckyTDP is a brilliant cross-device, cross-distro TDP plugin and the entire foundation this project is built on. **Huge thanks and full credit to its authors for their outstanding work** — none of this would exist without it. Please consider starring and supporting the upstream project.

ROGAllyTDP does not aim to replace SimpleDeckyTDP. It is a deliberate narrowing of scope: one device, one OS, tuned and tested only for that combination.

## Scope

- **Hardware**: ROG Ally with Ryzen **Z1 Extreme** only (RC71L). No Ally X, no Steam Deck, no Legion Go, no Intel handhelds.
- **OS**: **SteamOS** only (3.7+), with the kernel and `asus-nb-wmi` modules Valve ships.

The reason is simple: this is the hardware and the OS I run, and the only combination I can develop, test, and validate against. By dropping multi-device and multi-distro branching, the codebase can be tuned specifically to the Z1 Extreme on SteamOS — defaults, clamps, workarounds, profiles — without risking regressions on platforms I cannot verify.

**If you are not on a ROG Ally Z1 Extreme running SteamOS, please use the upstream [SimpleDeckyTDP](https://github.com/aarron-lee/SimpleDeckyTDP).** It is broader, better maintained for general use, and supports many more devices and distros.

## Features

Scoped to the Z1 Extreme on SteamOS:

- Per-game TDP profiles, with optional separate AC-power profiles
- TDP control via Asus WMI (works with secure boot, no `ryzenadj` required)
- Platform profile (`low-power` / `quiet` / `balanced` / `performance`) management synced to TDP
- GPU min/max clock controls
- CPU controls: EPP, power governor, SMT
- Battery charge limit
- MCU "extreme powersave" toggle (requires recent MCU firmware)
- Apply TDP on AC plug/unplug events and on resume from suspend
- Background TDP polling — defends against the Z1E's known ~5-minute PPT snap-back at higher wattages

## Requirements

- ROG Ally Z1 Extreme (RC71L)
- SteamOS 3.7 or newer
- [Decky Loader](https://github.com/SteamDeckHomebrew/decky-loader) installed
- MCU firmware **≥ 319** recommended (required for safe MCU powersave; older firmware causes back-button / suspend issues)

## Install

In Desktop mode, run the following in a terminal, then reboot:

```bash
curl -L https://github.com/ThaFridge/ROGAllyTDP/raw/main/install.sh | sh
```

The same command both installs and updates the plugin.

### Manual install

Download the latest release from the [releases page](https://github.com/ThaFridge/ROGAllyTDP/releases), unzip, move the resulting folder to `$HOME/homebrew/plugins/`, then:

```bash
sudo systemctl restart plugin_loader.service
```

## Manual build

Dependencies:

- Node.js v16.14+
- pnpm

```bash
git clone https://github.com/ThaFridge/ROGAllyTDP.git
cd ROGAllyTDP

# if pnpm not already installed
npm install -g pnpm

pnpm install
pnpm update @decky/ui --latest
pnpm run build
```

Place the resulting folder in `~/homebrew/plugins/`, then:

```bash
sudo systemctl restart plugin_loader.service
```

## Uninstall

In Desktop mode:

```bash
sudo rm -rf $HOME/homebrew/plugins/ROGAllyTDP
sudo systemctl restart plugin_loader.service
```

## Troubleshooting

### TDP control isn't working

1. Update the plugin (re-run the install command above) and reboot.
2. If that doesn't help, delete `$HOME/homebrew/settings/ROGAllyTDP/settings.json` and reboot. Note: this resets all per-game profiles — back the file up first if you want to keep them.
3. Still broken? Open an issue on the [issue tracker](https://github.com/ThaFridge/ROGAllyTDP/issues).

### MCU powersave / suspend / back buttons after wake

Ensure your **MCU firmware is ≥ 319**. Older firmware is known to break suspend and the back paddles when MCU powersave is enabled. If you cannot update MCU firmware, leave MCU powersave off.

### CPU boost toggle has no effect

SteamOS 3.7.5+ uses the `amd-pstate-epp` scaling driver in `active` mode. On this driver the per-policy boost write often reverts silently — this is a kernel/driver limitation, not a plugin bug. CPU boost is in any case **not recommended** on the Ally: it draws excessive power for little gain.

### TDP drifts down to ~30 W after several minutes

The Ally Z1E's embedded controller enforces a sustained ~30 W ceiling and will roll back higher PPT values after roughly five minutes. This is hardware behaviour, not a plugin bug. Background polling re-applies your target periodically.

## Credits

This project is built entirely on the foundation laid by others. In particular:

- **[SimpleDeckyTDP](https://github.com/aarron-lee/SimpleDeckyTDP)** by Aarron Lee — the upstream project this is derived from. Truly excellent work, and the reason ROGAllyTDP can exist at all.
- **[Decky Loader](https://github.com/SteamDeckHomebrew/decky-loader)** — the plugin runtime.
- **[PowerControl](https://github.com/mengmeet/PowerControl/)** — reference implementation for many TDP-control patterns.
- **[Handheld Daemon (hhd) — adjustor](https://github.com/hhd-dev/adjustor/)** and **[hwinfo](https://github.com/hhd-dev/hwinfo)** — reference for Asus WMI and Ally-specific quirks.
- **[ryzenadj](https://github.com/FlyGoat/RyzenAdj)** — even though this project favours WMI on the Ally, ryzenadj remains the canonical AMD TDP tool.
- The **[asus-linux](https://asus-linux.org/)** project — the `asus-nb-wmi` and `asus-armoury` kernel work that makes everything on the sysfs side possible.
- Valve and the SteamOS team — for opening SteamOS up to non-Deck handhelds.

If you find this useful, please star and support the upstream **[SimpleDeckyTDP](https://github.com/aarron-lee/SimpleDeckyTDP)** first.

## License

BSD 3-Clause License, inherited from upstream SimpleDeckyTDP. See [LICENSE](./LICENSE) for the full text and copyright notices.
