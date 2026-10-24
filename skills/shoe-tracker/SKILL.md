---
name: shoe-tracker
description: Track mileage on each pair of a runner's shoes and flag pairs nearing retirement. Use when the user adds a pair of shoes, asks about shoe mileage, or during periodic reviews.
---

# Shoe Tracker

Keep a simple ledger of the user's shoes and the miles on each, so retirement is a decision made from data instead of worn-out foam.

## The ledger

Maintain `shoes.md` in the user's files:

| Shoe | Type (road / trail / racer) | First used | Mileage | Status (active / retired) |
| --- | --- | --- | --- | --- |

## Process

- When the user mentions a new pair, add it to the ledger and, if their data source supports per-activity gear, remind them to tag runs with the right pair.
- At check-in time (or when asked), add the week's running distance to the pairs the user ran in. If the data source does not identify which shoes were worn, ask the user or split by their stated rotation; label any estimate as an estimate.
- Flag a pair when it approaches the user's retirement threshold. Default guidance: most daily trainers are ready for evaluation around 300 to 500 miles (500 to 800 km), sooner if the user reports new aches, dead-feeling foam, or visible wear. The flag is a prompt to evaluate, not an automatic verdict.
- When a pair retires, mark it retired with the final mileage and date. Retired pairs stay in the ledger as history.

## Guardrails

- Mileage numbers must come from the user's data or the user's report. Never silently assume every run went on one pair.
- Shoe advice is general information. Persistent pain is a professional matter, not a shoe prescription.
