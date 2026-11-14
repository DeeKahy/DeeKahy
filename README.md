<div align="center">

<img src="assets/hero.svg" alt="Hi, I'm DeeKahy" width="100%"/>

<br/>

[![Editor: Mitos](https://img.shields.io/badge/editor-Mitos-cba6f7?style=for-the-badge&logo=gnometerminal&logoColor=11111b&labelColor=1e1e2e)](https://mitos.computer)
[![OS: NixOS](https://img.shields.io/badge/os-NixOS-89b4fa?style=for-the-badge&logo=nixos&logoColor=11111b&labelColor=1e1e2e)](https://nixos.org)
[![Homelab: smallapp.cc](https://img.shields.io/badge/homelab-smallapp.cc-a6e3a1?style=for-the-badge&logo=proxmox&logoColor=11111b&labelColor=1e1e2e)](#-the-homelab)
[![Based in Denmark](https://img.shields.io/badge/based_in-Denmark-f38ba8?style=for-the-badge&logo=googlemaps&logoColor=11111b&labelColor=1e1e2e)](#)

</div>

<br/>

## 🚀 &nbsp;Things I've built

<table>
<tr>
<td width="50%" valign="top">

### 🌸 [Chainbloom](https://github.com/DeeKahy/chainbloom)
A chain-reaction idle game. Start with a spark, end up with a galaxy, and then a farm.
<br/>`TypeScript` `Vite` · **[▶ play it](https://chainbloom.smallapp.cc)**

</td>
<td width="50%" valign="top">

### 🔬 [Pollen-Detector](https://github.com/DeeKahy/Pollen-Detector)
A cheap, 3D-printable pollen sampler built around a Raspberry Pi. It takes pictures, sorts them and uploads them.
<br/>`Python` `Raspberry Pi` `3D printing`

</td>
</tr>
<tr>
<td valign="top">

### 🍎 [fluxer-apple](https://github.com/DeeKahy/fluxer-apple)
Native Fluxer chat client for iOS and macOS, written in Swift and SwiftUI.
<br/>`Swift` `SwiftUI`

</td>
<td valign="top">

### 🐱 [CopyCat](https://github.com/DeeKahy/CopyCat)
`ccat` walks a project tree and copies every text file to your clipboard, so you can hand an LLM the whole thing. It's in nixpkgs: `nix-shell -p copycat`.
<br/>`Rust`

</td>
</tr>
<tr>
<td valign="top">

### 🌀 [Portal Link Planner](https://github.com/DeeKahy/portal-link-planner)
Works out where to build Minecraft nether portals so they link the way you meant, and catches link-stealing between nearby portals.
<br/>`JavaScript` · **[▶ try it](https://portals.smallapp.cc)**

</td>
<td valign="top">

### 🔎 [searxng-instant-answers](https://github.com/DeeKahy/searxng-instant-answers)
About 45 instant-answer cards for SearXNG (dice, timers, weather, dates, colours, dev tools) plus per-browser site ranking.
<br/>`Python` `SearXNG`

</td>
</tr>
<tr>
<td valign="top">

### 📸 [toolshot](https://github.com/DeeKahy/toolshot)
Screenshot, annotation and colour-picker tool that lives in the menu bar.
<br/>`JavaScript` · **[▶ site](https://deekahy.github.io/toolshot/)**

</td>
<td valign="top">

### ❄️ [fluxer-nix](https://github.com/DeeKahy/fluxer-nix)
A Nix package for the Fluxer desktop client, laid out for upstreaming to nixpkgs.
<br/>`Nix`

</td>
</tr>
</table>

<details>
<summary><b>…and a pile of smaller things</b></summary>
<br/>

| | |
|---|---|
| 🔁 [**FrontendConverter**](https://github.com/DeeKahy/FrontendConverter) | A file converter that runs entirely in your browser, with no uploads. [convert.smallapp.cc](https://convert.smallapp.cc) |
| ⏳ [**Countdown**](https://github.com/DeeKahy/Countdown) | Countdowns to things, shown in your own timezone. [countdown.smallapp.cc](https://countdown.smallapp.cc) |
| 🌐 [**whatmyip**](https://github.com/DeeKahy/whatmyip) | A tiny axum service: `curl whatmyip.smallapp.cc` |
| 🎨 [**fluxer-theme-library**](https://github.com/DeeKahy/fluxer-theme-library) | Community themes for Fluxer, previewed live from each theme's own tokens |
| 🌿 [**trident**](https://github.com/DeeKahy/trident) | A git client for GitHub and GitLab, built with Tauri and Svelte |
| 🛤️ [**fastcarts**](https://github.com/DeeKahy/fastcarts) | A Fabric mod that speeds up minecarts only while a player rides them |
| 🗳️ [**Project-Choice-Maxxing**](https://github.com/DeeKahy/Project-Choice-Maxxing) | A voting app that ranks options with several voting algorithms |
| ⏱️ [**workhours**](https://github.com/DeeKahy/workhours) | A self-hosted work-hours and pay tracker |

</details>

<br/>

## 🏠 &nbsp;The homelab

```text
  internet ──► cloudflare ──► caddy ──► ~20 self-hosted apps
                                 │
             proxmox ──► nixos ──┘   one flake · declarative · reproducible
```

All of `*.smallapp.cc` runs on a Proxmox box in my home. The VM that serves it is NixOS, declared in a single flake: every app is a flake input and a module, Caddy gets TLS certificates over Cloudflare DNS-01, and Prometheus and Grafana watch it. If the server dies, a rebuild brings everything back as it was.

<br/>

## ❄️ &nbsp;NixOS

Everything I build ends up on [**NixOS**](https://nixos.org). Each app ships with a flake that has a package and a NixOS module, so putting it on the homelab takes one line of config and a rebuild.

<p align="center">
  <a href="https://github.com/DeeKahy/whatmyip"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=17&duration=2200&pause=1300&color=CBA6F7&center=true&vCenter=true&width=440&height=34&lines=%24+cargo+run;%24+nix+build+.%23whatmyip;services.whatmyip.enable+%3D+true;%24+curl+whatmyip.smallapp.cc" alt="$ cargo run · $ nix build .#whatmyip · services.whatmyip.enable = true · $ curl whatmyip.smallapp.cc"/></a>
</p>

<br/>

## 🧰 &nbsp;Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=rust,go,ts,swift,py,java,haskell,svelte&theme=dark" alt="Languages"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=nix,linux,bash,sqlite,vite,tauri,cloudflare,raspberrypi,githubactions&theme=dark" alt="Tools"/>
</p>

<br/>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DeeKahy/DeeKahy/output/snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DeeKahy/DeeKahy/output/snake-light.svg"/>
  <img alt="A snake eating my contribution graph" src="https://raw.githubusercontent.com/DeeKahy/DeeKahy/output/snake-dark.svg" width="100%"/>
</picture>

<sub>✦ written in Mitos · built on NixOS · served from a box in my home ✦</sub>

</div>
