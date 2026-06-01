#!/usr/bin/env python3
"""Copia logos.js desde carta de conformidad (mismo membrete Gráfica Silvestre)."""
import shutil
from pathlib import Path

DIR = Path(__file__).resolve().parent
ORIGEN = DIR.parent / "carta de conformidad" / "logos.js"
DESTINO = DIR / "logos.js"

if not ORIGEN.is_file():
    raise SystemExit(
        "No existe logos.js en carta de conformidad.\n"
        "Primero ejecute allí: python extraer-assets-acta.py"
    )

shutil.copy2(ORIGEN, DESTINO)
print("OK:", DESTINO, "bytes:", DESTINO.stat().st_size)
