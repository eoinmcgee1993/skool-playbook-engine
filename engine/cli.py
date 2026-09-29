import argparse
import json
from pathlib import Path
from .pipeline import build_playbook
from .render import write_html

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    bundle = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = build_playbook(bundle)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    (out / "master-playbook.md").write_text(result["markdown"], encoding="utf-8")
    (out / "provenance.json").write_text(json.dumps(result["provenance"], indent=2), encoding="utf-8")
    (out / "change-report.md").write_text(result["change_report"], encoding="utf-8")

if __name__ == "__main__":
    main()
