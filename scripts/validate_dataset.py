#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
c = json.loads((root / "metadata/catalog.json").read_text(encoding="utf-8"))
assert c["schema_version"] == "1.0.0"
assets = c["audio_assets"]
assert len({a["id"] for a in assets}) == len(assets)
assert len({a["path"] for a in assets}) == len(assets)
for a in assets:
    p = root / a["path"]
    assert p.is_file() and p.stat().st_size == a["bytes"], a["path"]
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    assert h == a["sha256"], a["path"]
    assert a["duration_seconds"] > 0, a["path"]
for d in c["reference_assets"]:
    assert (root / d["path"]).is_file(), d["path"]
print(f'validated {len(assets)} audio assets and {len(c["reference_assets"])} reference assets')
