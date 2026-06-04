# ProjectE: EMC for Magitech

Play [Magitech -Arcane Engineering-](https://modrinth.com/mod/magitech_mod) with [ProjectE](https://modrinth.com/mod/projecte) and none of Magitech's ores, crystals, or alchemy products have an EMC value. This data-only add-on fixes that.

Magitech builds most of its materials through custom alchemy recipes (the Zardius crucible, spell conversions, the athanor) that ProjectE can't read, and its ores have no EMC seed — so out of the box ProjectE ignores Magitech entirely. This teaches it:

- **Hand-tuned EMC** for the root resources — ores, gems (fluorite, tourmaline), mana resources, worldgen plants, and crystals.
- Magitech's **alchemy recipes are transcribed as ProjectE conversions**, so element crystals, special ingots (radiant steel, ender metal), and alchemy products derive their EMC automatically.
- **Endgame tier-4 materials** (frigidite, translucium, resonite, abyssite) are priced high on purpose, so mining them stays more worthwhile than transmuting — the progression is preserved, not short-circuited.
- The **part-based tool system carries no EMC by design**: a tool's value depends on the material it was cut from, which ProjectE can't represent, and leaving it out keeps the build-and-upgrade-your-own-tool loop intact.

It adds no items, blocks, or recipes — only EMC data. Values apply on world load; open a Transmutation Table to see them.

**Dependencies**

- [ProjectE](https://modrinth.com/mod/projecte) — required
- [Magitech -Arcane Engineering-](https://modrinth.com/mod/magitech_mod) — required
- NeoForge 1.21.1

EMC values are a considered first pass; balance feedback is welcome on the issue tracker.

MIT. Magitech is by Stln; ProjectE by sinkillerj & contributors. This is an independent integration, not affiliated with either. Source and issues: https://github.com/KURONAMI333/magitech-emc
