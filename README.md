# ProjectE: EMC for Magitech

Give Magitech's ores, crystals, and alchemy products EMC values when playing with ProjectE. This data-only add-on requires both ProjectE and Magitech.

## What it does

- Hand-sets EMC for Magitech's root resources (ores, gems, mana resources, worldgen plants).
- Transcribes Magitech's custom alchemy recipes (Zardius crucible / spell conversion / athanor)
  as ProjectE conversions, so crystals, special ingots and alchemy products derive automatically.
- Endgame tier-4 materials (frigidite / translucium / resonite / abyssite) are priced high so
  **mining stays more practical than transmutation** — preserving Magitech's progression.
- The material-parametric **tool / part system has no EMC by design** (a part's value depends on
  the material it was cut from, which ProjectE can't represent — and it protects the tool-building
  loop from being short-circuited by transmutation).

## Requirements

- Minecraft 1.21.1 with NeoForge.
- [ProjectE](https://www.curseforge.com/minecraft/mc-mods/projecte) and [Magitech](https://modrinth.com/mod/magitech_mod).

Install the matching mods, then place this add-on's JAR in `mods/`. Values become available when the world loads; check them in a Transmutation Table.

## Build from source

The EMC data is included in this repository. Run `./gradlew build` with JDK 21 to package it. To regenerate the data from a Magitech release, provide the JAR explicitly:

```bash
python tools/generate_emc.py <path-to-magitech-jar>
./gradlew build
```

For an in-game development run, ProjectE and Magitech must be installed in a matching Minecraft instance. A local `runclient-hosts.gradle` can add host dependencies to Gradle, but that optional file is not part of this repository.

## License

[All Rights Reserved](LICENSE). Modpack inclusion is allowed without permission or credit.

## Downloads and support

Downloads: [CurseForge](https://www.curseforge.com/minecraft/mc-mods/projecte-emc-for-magitech).

For bugs and questions, comment on the [CurseForge page](https://www.curseforge.com/minecraft/mc-mods/projecte-emc-for-magitech) or DM [@kuronami333 on X](https://x.com/kuronami333).

[Source](https://github.com/KURONAMI333/magitech-emc) · [License](LICENSE)
