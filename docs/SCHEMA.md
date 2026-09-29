# Content schema

Each knowledge item should carry:

- id
- title
- source
- source_locator
- source_type
- claim
- action
- prerequisites
- tools
- risks
- confidence
- labels
- created_at
- updated_at

Provenance is mandatory. Deduplication may merge items, but must retain all source locators.

## Bundle

The input bundle contains a manifest plus normalised source records.

## Publication

Published playbooks contain the source/expansion/update/operator distinction so readers can separate course doctrine from later implementation detail.
