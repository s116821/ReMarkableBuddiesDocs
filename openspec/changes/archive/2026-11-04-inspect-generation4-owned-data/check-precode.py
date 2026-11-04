"""Check literal precode integrity and arithmetic premises, not product behavior."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
MAX_U64 = (1 << 64) - 1
MAX_MEDIA = 256 * 1024 * 1024
schema = json.loads((ROOT / "schema.json").read_bytes())
vectors = json.loads((ROOT / "vectors.json").read_bytes())["cases"]
assert len(schema["required"]) == 26
assert set(schema["required"]) == set(schema["properties"])
assert len({row["id"] for row in vectors}) == len(vectors)
pattern = schema["$defs"]["counter"]["pattern"]
for value in ["0", "1", str(MAX_U64)]:
    assert re.search(pattern, value)
for value in ["1\n", "1\r\n", "1 ", " 1", "+1", "-1", "1.0", "1e3", "00", ""]:
    assert not re.search(pattern, value), repr(value)
checked_arithmetic = []
for row in vectors:
    raw = row["raw_utf8"].encode("utf-8")
    assert len(raw) == row["raw_bytes"]
    assert hashlib.sha256(raw).hexdigest() == row["raw_sha256"]
    if row["expected_valid"]:
        assert len(raw) <= 32768
        report = json.loads(raw)
        assert set(report) == set(schema["required"])
        if report["status"] == "complete":
            assert not report["issues"]
            for usage in report["observed_domains"].values():
                for field in ["missing_references", "uninspected_references", "size_mismatched_references", "omitted_references"]:
                    assert usage[field] == "0"
    if "arithmetic_inputs" in row:
        report = json.loads(raw)
        values = [int(value) for value in row["arithmetic_inputs"]["cache_file_lengths"]]
        assert all(0 <= value <= MAX_U64 for value in values)
        assert int(report["storage"]["cache"]["files"]) == len(values)
        assert all(int(usage["declared_media_bytes"]) <= 4096 * MAX_MEDIA for usage in report["observed_domains"].values())
        subtotal = sum(values)
        total = subtotal + int(row["arithmetic_inputs"]["noncache_bytes"])
        if subtotal > MAX_U64:
            assert len(values) > 1
            assert report["storage"]["cache"]["apparent_bytes"] is None
            assert report["observed_apparent_bytes"] is None
            assert report["issues"]["byte-count-overflow"] == "1"
        else:
            assert int(report["storage"]["cache"]["apparent_bytes"]) == subtotal
            assert int(report["observed_apparent_bytes"]) == total <= MAX_U64
        checked_arithmetic.append(row["id"])
assert {row["raw_bytes"] for row in vectors if row["id"] in ["exact-32768-wire-bound", "wire-one-byte-over"]} == {32768, 32769}
print(json.dumps({"status": "passed", "literal_cases": len(vectors), "arithmetic_premises": checked_arithmetic,
                  "limits": "Precode integrity/regex/arithmetic only; no successor parser/producer/host/filesystem qualification"}))
