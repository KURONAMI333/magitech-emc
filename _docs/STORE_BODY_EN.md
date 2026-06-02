<!-- Modrinth/CurseForge description source of truth. Paste verbatim into Modrinth;
     paste into CurseForge in MARKDOWN mode. Title/summary below are the search-indexed fields. -->

<!-- TITLE (<=64 chars): Magitech ProjectE EMC -->
<!-- SUMMARY (search-indexed, plain text): ProjectE EMC for Magitech -Arcane Engineering-: adds EMC to its ores, gems, crystals and alchemy products so you can transmute Magitech content. -->

# Magitech ProjectE EMC

Play [Magitech -Arcane Engineering-](https://modrinth.com/mod/magitech_mod) with [ProjectE](https://modrinth.com/mod/projecte) and find that none of Magitech's ores, crystals or alchemy products have an EMC value? This add-on fixes that.

## What it does

Magitech builds most of its materials through custom alchemy recipes (the Zardius crucible, spell conversions, the athanor) that ProjectE can't read on its own, and its ores have no EMC seed. So out of the box, ProjectE simply ignores Magitech.

This is a small, **data-only** add-on that teaches ProjectE about Magitech:

- **Hand-tuned EMC** for Magitech's root resources — ores, gems (fluorite, tourmaline), mana resources, worldgen plants and crystals.
- Magitech's **alchemy recipes are transcribed as ProjectE conversions**, so element crystals, special ingots (radiant steel, ender metal) and alchemy products derive their EMC automatically.
- **Endgame tier-4 materials** (frigidite, translucium, resonite, abyssite) are priced high on purpose, so mining them stays more worthwhile than transmuting — Magitech's progression is preserved, not short-circuited.
- The **part-based tool system has no EMC by design**: a Magitech tool's value depends on the material it was cut from, which ProjectE can't represent — and leaving it out keeps the satisfying "build and upgrade your own tool" loop intact instead of letting you transmute finished gear.

It adds **no items, blocks or recipes** — only EMC data.

## Compatibility

| | 1.21.1 |
|---|---|
| NeoForge | ✅ |

Requires **ProjectE** and **Magitech -Arcane Engineering-** (NeoForge 1.21.1).

## Install

Drop the jar into your `mods` folder alongside ProjectE and Magitech. EMC values apply on world load — open a Transmutation Table to see them.

## Dependencies

- **ProjectE** — required
- **Magitech -Arcane Engineering-** — required

## Scope & limitations

- NeoForge 1.21.1 only.
- EMC values are a considered first pass; feedback on balance is welcome via the issue tracker.
- Magitech tools and tool parts intentionally carry no EMC (see above).

## License & credits

MIT. Magitech is by Stln; ProjectE by sinkillerj & contributors. This add-on is an independent integration and is not affiliated with either.
