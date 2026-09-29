from collections import OrderedDict

LABELS = {"SOURCE", "EXPANSION", "UPDATE", "OPERATOR"}

def _items(bundle):
    return bundle.get("items", [])

def deduplicate(items):
    seen = OrderedDict()
    for item in items:
        key = (item.get("title","").strip().lower(), item.get("claim","").strip().lower())
        if key not in seen:
            seen[key] = dict(item)
        else:
            locs = set(seen[key].get("source_locator", [])) if isinstance(seen[key].get("source_locator"), list) else {seen[key].get("source_locator")}
            other = item.get("source_locator")
            if isinstance(other, list):
                locs.update(other)
            elif other:
                locs.add(other)
            seen[key]["source_locator"] = sorted(x for x in locs if x)
    return list(seen.values())

def build_markdown(items):
    lines = ["# Master AI Business Playbook", "", "> Generated from authorised source material.", ""]
    for item in items:
        title = item.get("title", "Untitled")
        labels = ", ".join(x for x in item.get("labels", []) if x in LABELS)
        lines += [f"## {title}", ""]
        if labels:
            lines += [f"**Labels:** {labels}", ""]
        if item.get("claim"):
            lines += [f"**Claim:** {item['claim']}", ""]
        if item.get("action"):
            lines += [f"**Action:** {item['action']}", ""]
        if item.get("tools"):
            lines += [f"**Tools:** {', '.join(item['tools'])}", ""]
        lines += [""]
    return "\n".join(lines)

def build_playbook(bundle):
    original = _items(bundle)
    items = deduplicate(original)
    provenance = {
        "source_bundle": bundle.get("manifest", {}),
        "items": [
            {
                "id": i.get("id"),
                "source": i.get("source"),
                "source_locator": i.get("source_locator"),
                "labels": i.get("labels", [])
            } for i in items
        ]
    }
    report = f"# Change Report\n\nInput items: {len(original)}\n\nDeduplicated items: {len(items)}\n"
    return {"markdown": build_markdown(items), "provenance": provenance, "change_report": report}
