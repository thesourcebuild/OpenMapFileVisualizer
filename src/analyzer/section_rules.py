SECTION_RULES = {
    "keywords": {
        "code": {"code", "text", "thumb", "arm", "function"},
        "rodata": {"rodata", "readonly", "const", "ro", "ro-data"},
        "data": {"rwdata", "data", "rw", "rw-data"},
        "bss": {"zidata", "bss", "zi", "zero", "zero-initialized"},
        "debug": {"debug", "debugdata"},
    },
    "prefixes": [
        ("code", (".text", ".init", ".fini", ".isr_vector", ".vectors", ".itcm")),
        ("rodata", (".rodata", ".const", ".ARM.extab", ".ARM.exidx", ".eh_frame", ".gcc_except_table")),
        ("data", (".data", ".ramfunc", ".fastcode", ".dtcm")),
        ("bss", (".bss", "COMMON", ".noinit", ".heap", ".stack", ".dma_buffer")),
        ("debug", (".debug", ".stab", ".line", ".group", ".comment", ".note", ".symtab", ".strtab", ".ARM.attributes", ".xtensa.info", ".gnu.attributes", ".gnu.hash", ".dynsym", ".dynstr", ".rel", ".rela")),
    ],
    "suffixes": [
        ("code", (".text", ".text_end", ".vectors", ".force_slow")),
        ("rodata", (".rodata", ".literal", ".appdesc")),
        ("data", (".data", "_reserved", ".force_fast")),
        ("bss", (".bss", ".noload")),
    ],
}

REGION_KIND_RULES = {
    "flash": {
        "keywords": ("flash", "rom", "qspi", "nor", "nand", "emmc", "spi", "boot", "linear", "program"),
        "attributes": ("x", "r"),
    },
    "ram": {
        "keywords": ("ram", "sram", "ddr", "ocm", "tcm", "dram", "bram", "ps7_ram", "ps7_ddr", "noncache"),
        "attributes": ("w",),
    },
}

MODULE_CLASS_RULES = {
    "Networking": ("lwip", "tcp", "udp", "ip4", "eth", "mqtt", "dhcp", "dns", "sntp", "smtp", "tftp", "socket", "arp", "netbios"),
    "Drivers / BSP": (
        # Xilinx
        "xil", "xemac", "xadc", "qspi", "sdps", "ttc", "scugic",
        # Generic/Common
        "uart", "iic", "gpio", "bsp", "driver", "phy",
        # STMicroelectronics HAL
        "stm32", "hal",
        # NXP/Freescale
        "fsl_", "lpc_", "kinetis", "mcux",
        # Microchip/Atmel
        "atmel_", "sam_", "pic_", "avr_",
        # Silicon Labs
        "em_", "sl_",
        # Renesas
        "r_", "rz_",
        # Infineon
        "cy_", "xmc_",
    ),
    "File system": ("fatfs", "ff.", "ff_", "xilffs", "diskio", "filesystem", "file"),
    "RTOS / DSP": ("freertos", "rtos", "task", "queue", "semphr", "cmsis", "arm_"),
    "Runtime / C library": (
        # Standard C libraries
        "libc", "glibc", "musl", "newlib", "uclibc", "ulibc",
        # Embedded/Lightweight C libraries
        "picolibc", "avr-libc", "klibc", "dietlibc", "bionic",
        # ARM embedded
        "arm_none_eabi",
        # Math library
        "libm",
        # C++ standard library
        "libstdc", "libcxx",
        # Compiler runtime support
        "libgcc", "compiler-rt",
        # C runtime initialization
        "crt", "crtbegin", "crtend",
        # Memory management and utilities
        "malloc", "printf", "memcpy", "strlen", "strcpy",
    ),
    "Application": ("app", "cli", "table", "control", "handler", "manager", "database", "ota", "fdr"),
    "Libraries / middleware": (".a(", ".lib("),
}
