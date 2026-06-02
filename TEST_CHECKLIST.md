# Magitech ProjectE EMC — Runtime Test Checklist

Run `./gradlew runClient` from `mod-041-magitech-emc/`. The dev runtime loads
ProjectE + Magitech (+ deps) via `localRuntime` (build.gradle), plus this mod.

## 1. Mod load (title screen)
- [ ] Mods list shows `Magitech ProjectE EMC 0.1.0`, `ProjectE`, `Magitech`
- [ ] No red-banner load errors
- [ ] `run/logs/latest.log` contains: `Magitech ProjectE EMC v0.1.0 loading`
- [ ] No ProjectE custom-conversion parse errors in the log
      (search the log for `pe_custom_conversions`, `CustomConversion`, `EMC` warnings)

## 2. Create world
- [ ] Singleplayer → New World → Creative, **Allow Cheats: ON**

## 3. EMC values (Transmutation Table)
Craft/`/give` a Transmutation Table; drop items in to read their EMC.
Expected (per MAGITECH_EMC_SPEC.md):
- [ ] `magitech:fluorite` ≈ 256, `magitech:tourmaline` ≈ 384
- [ ] `magitech:ember_crystal` and the other 7 element crystals have EMC (derived, > their fluorite cost)
- [ ] `magitech:radiant_steel_ingot` / `ender_metal_ingot` have EMC (derived from their zardius recipes)
- [ ] **Tier ordering holds**: T0 plants/zinc < T1 gems < crystals < T4 polished ores
- [ ] **T4 wall**: `polished_frigidite/translucium/resonite` ≈ 65,536, `polished_abyssite` ≈ 98,304
- [ ] **Tools/parts have NO EMC**: `magitech:dagger`, `magitech:wand`, `magitech:light_blade`,
      `magitech:catalyst` etc. show no EMC value (cannot be learned/transmuted)

## 4. Exploit / sanity check
- [ ] Spot-check: for each hand-set primitive, the cheapest in-game way to obtain it
      costs **≥** its EMC (no "craft cheap → transmute for profit" loop)
- [ ] Tag-based conversions resolved: `magitech:aspect_crystal_base` (tourmaline/quartz) and
      `c:gems/fluorite` produced sensible crystal EMC (if a crystal has NO EMC, the tag didn't resolve)

## 5. Result
- Pass → tune any values that feel off, then publish (icon + store page).
- Fail → capture the log line / wrong EMC and report back for a value/conversion fix.

## Notes
- If runClient errors on a missing dependency (a transitive of Magitech/ProjectE not in
  build.gradle's `localRuntime`), add that jar from the instance mods folder and re-run.
- This is a data-only mod; the `@Mod` class only logs on load.
