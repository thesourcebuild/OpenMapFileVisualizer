#!/bin/bash
set -e
cd "$(dirname "$0")/.."
if [ -z "$1" ]; then
    echo ""
    echo "Usage: $(basename "$0") <map_file> [options...]"
    echo ""
    echo "Example: $(basename "$0") sample/OpenLibCLI_Keil/OpenLibCLI_Keil.map"
    echo ""
    exit 0
fi
cmd=$(command -v python3 || command -v python)
exec "$cmd" src/openmapfileanalyzer.py "$@"