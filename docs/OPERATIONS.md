# Operations

Input is an immutable authorised bundle from `skool-master-playbook`.

Run:

validate -> extract -> normalise -> deduplicate -> gap analysis -> expansion -> verification -> curation -> publish -> change report

Failed verification must never be silently promoted to verified content.

## Local run

```bash
python -m engine.cli --input ../skool-master-playbook/data/normalised/bundle.json --output dist/
```
