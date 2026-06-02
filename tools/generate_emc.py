"""Regenerate data/magitech/pe_custom_conversions/magitech.json.

Reads the Magitech jar, transcribes its custom alchemy recipes into ProjectE
conversions, and emits hand-set EMC for root primitives. Code-free output.

Usage: python tools/generate_emc.py [path/to/magitech-1.1.3.jar]
ProjectE CustomConversionFile schema (1.21.1): values.before = list of
{type,emc_value,id}; groups.<g>.conversions[] = {count?, ingredients[{type,id,amount?}], output{type,id}}.
"""

import sys, json, os, zipfile, glob, tempfile
from collections import OrderedDict

JAR = (
    sys.argv[1]
    if len(sys.argv) > 1
    else r"C:\Users\naoki\curseforge\minecraft\Instances\2605_nf21_Magi\mods\magitech-1.1.3.jar"
)
OUT = os.path.join(
    os.path.dirname(__file__),
    "..",
    "src",
    "main",
    "resources",
    "data",
    "magitech",
    "pe_custom_conversions",
    "magitech.json",
)

# Hand-set EMC for root primitives (no recipe produces them, or seeded currency gems).
# See MAGITECH_EMC_SPEC.md for rationale (P2 balance, ProjectE anchor scale).
BEFORE = {
    "celifern_log": 32,
    "charcoal_birch_log": 32,
    "celifern_sapling": 32,
    "charcoal_birch_sapling": 32,
    "celifern_leaves": 1,
    "charcoal_birch_leaves": 1,
    "stripped_celifern_log": 32,
    "stripped_charcoal_birch_log": 32,
    "mistalia_petals": 16,
    "scorched_soil": 4,
    "scorched_grass_soil": 4,
    "mana_berries": 16,
    "raw_zinc": 128,
    "chromium_ingot": 512,
    "sulfur": 64,
    "fluorite": 256,
    "tourmaline": 384,
    "redstone_crystal": 256,
    "polished_redstone_crystal": 256,
    "fluorite_crystal_cluster": 768,
    "redstone_crystal_cluster": 768,
    "sulfur_crystal_cluster": 192,
    "aggregated_fluxia": 256,
    "aggregated_luminis": 256,
    "aggregated_noctis": 256,
    "polished_frigidite": 65536,
    "polished_translucium": 65536,
    "polished_resonite": 65536,
    "polished_abyssite": 98304,
}
# Outputs to skip (active gear w/ component state, creative, guidebooks).
EXCLUDE_OUT = {
    "aether_lifter",
    "flamglide_strider",
    "arcane_engineering_compendium",
    "the_fire_that_thinks",
    "glistening_lexicon",
    "weaver_spawn_egg",
}
INCLUDE_TYPES = {
    "magitech:zardius_crucible",
    "magitech:spell_conversion",
    "magitech:athanor_pillar_infusion",
}


def ingredients_of(o):
    acc = OrderedDict()

    def add(item=None, tag=None):
        k = ("item", item) if item else ("tag", tag)
        if k[1]:
            acc[k] = acc.get(k, 0) + 1

    t = o["type"]
    if t == "magitech:spell_conversion":  # spell = free labour
        d = o["ingredient"]
        add(d.get("item"), d.get("tag"))
    elif t == "magitech:zardius_crucible":
        for d in o.get("ingredients", []):
            add(d.get("item"), d.get("tag"))
    elif t == "magitech:athanor_pillar_infusion":
        b = o.get("base", {})
        add(b.get("id") or b.get("item"))
        for slot in o.get(
            "ingredients", []
        ):  # slots are OR-lists -> pick first concrete
            pick = next((x["item"] for x in slot if "item" in x), None)
            if pick:
                add(pick)
            elif slot:
                add(slot[0].get("item"), slot[0].get("tag"))
    return acc


def main():
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(JAR) as z:
            for n in z.namelist():
                if n.startswith("data/magitech/recipe/") and n.endswith(".json"):
                    z.extract(n, tmp)
        recdir = os.path.join(tmp, "data", "magitech", "recipe")
        convs = []
        for f in sorted(glob.glob(os.path.join(recdir, "*.json"))):
            try:
                o = json.load(open(f, encoding="utf-8"))
            except Exception:
                continue
            if o.get("type") not in INCLUDE_TYPES:
                continue
            r = o.get("result") or {}
            out = r.get("id") or r.get("item")
            if not out or not out.startswith(
                "magitech:"
            ):  # don't redefine vanilla outputs
                continue
            if out.replace("magitech:", "") in EXCLUDE_OUT:
                continue
            ings = ingredients_of(o)
            if not ings:
                continue
            ing_json = []
            for (kind, idv), amt in ings.items():
                # ProjectE NSS: tags use type projecte:item with a "tag" key (not a
                # "projecte:tag" type, which does not exist). Plain items use "id".
                if kind == "item":
                    e = {"type": "projecte:item", "id": idv}
                else:
                    e = {"type": "projecte:item", "tag": idv}
                if amt > 1:
                    e["amount"] = amt
                ing_json.append(e)
            c = OrderedDict()
            if r.get("count", 1) > 1:
                c["count"] = r["count"]
            c["ingredients"] = ing_json
            c["output"] = {"type": "projecte:item", "id": out}
            convs.append(c)

    doc = OrderedDict()
    doc["replace"] = False
    doc["comment"] = (
        "Magitech EMC integration for ProjectE (KURONAMI). Hand-set primitives + "
        "transcribed zardius/spell/athanor recipes. Tools/parts/active-gear have no EMC."
    )
    doc["values"] = {
        "before": [
            {"type": "projecte:item", "emc_value": v, "id": f"magitech:{k}"}
            for k, v in BEFORE.items()
        ]
    }
    doc["groups"] = {
        "magitech_recipes": {
            "comment": "Transcribed Magitech custom recipes for EMC derivation.",
            "conversions": convs,
        }
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(doc, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(
        f"primitives={len(BEFORE)} conversions={len(convs)} -> {os.path.normpath(OUT)}"
    )


if __name__ == "__main__":
    main()
