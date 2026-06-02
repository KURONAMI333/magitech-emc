package com.kuronami.magitechemc;

import com.mojang.logging.LogUtils;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import org.slf4j.Logger;

/**
 * Magitech ProjectE EMC — a data-only integration. All EMC values and recipe
 * conversions live in {@code data/magitech/pe_custom_conversions/magitech.json}
 * and are loaded by ProjectE via the datapack reload; this class only provides
 * the {@code @Mod} entry point so the project fits the standard NeoForge build
 * and runClient pipeline (smoke-test logging on load).
 */
@Mod(MagitechEMC.MODID)
public final class MagitechEMC {
    public static final String MODID = "magitech_emc";
    public static final String VERSION = "0.1.0";
    private static final Logger LOGGER = LogUtils.getLogger();

    public MagitechEMC(IEventBus modBus) {
        LOGGER.info("Magitech ProjectE EMC v{} loading — EMC supplied via data/magitech/pe_custom_conversions", VERSION);
    }
}
