# Magitech ProjectE EMC

A code-free (`lowcodefml`) NeoForge 1.21.1 mod that adds **ProjectE EMC values** to
**Magitech -Arcane Engineering-**. Requires ProjectE and Magitech.

## What it does

- Hand-sets EMC for Magitech's root resources (ores, gems, mana resources, worldgen plants).
- Transcribes Magitech's custom alchemy recipes (Zardius crucible / spell conversion / athanor)
  as ProjectE conversions, so crystals, special ingots and alchemy products derive automatically.
- Endgame tier-4 materials (frigidite / translucium / resonite / abyssite) are priced high so
  **mining stays more practical than transmutation** — preserving Magitech's progression.
- The material-parametric **tool / part system has no EMC by design** (a part's value depends on
  the material it was cut from, which ProjectE can't represent — and it protects the tool-building
  loop from being short-circuited by transmutation).

Balance philosophy and the full value table live in
`~/claude-memory/kuronami-mods/knowledge/MAGITECH_EMC_SPEC.md`.

## Build (no compilation — it's a data-only jar)

```bash
python tools/generate_emc.py   # regenerate data/.../magitech.json from the Magitech jar
./gradlew build                # -> build/libs/magitech_emc-0.1.0.jar
./gradlew runClient            # dev Minecraft with ProjectE + Magitech (localRuntime) for verification
```

`build.gradle` loads ProjectE + Magitech (+ deps) from a local NeoForge 1.21.1 instance via
`localRuntime` so `runClient` can verify EMC end to end. System JAVA_HOME must allow JDK21 — the
build pins `org.gradle.java.home` to JDK21 (JDK25 breaks the toolchain).

## Verify

`./gradlew runClient`, then follow `TEST_CHECKLIST.md` (mod loads, ProjectE parses 0 errors,
Transmutation Table EMC values + tier ordering + tools-have-no-EMC + no exploit).

## Status

v0.1.0 — gradle build green; runClient runtime-verified (loads, ProjectE parses all conversions
with 0 errors). **In-game EMC balance pass (values/ordering) pending.** Icon done (`branding/icon.png`,
64×64 — upscale to ≥256 for store pages). Publishing deferred. First of a planned ProjectE-EMC
compat series (next targets: Iron's Spellbooks, Forbidden Arcanus, Spectrum, Malum).
