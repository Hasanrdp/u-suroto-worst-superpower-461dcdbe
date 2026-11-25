# Worst Superpower — Closed-Umbrella Rain

[![make.fun](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/Hasanrdp/u-suroto-worst-superpower-461dcdbe/rank.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/Hasanrdp/u-suroto-worst-superpower-461dcdbe/reward.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)

Entry for the [Worst Superpower](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe) bounty on [make.fun](https://make.fun): invent the most useless superpower in one line of at most 140 characters.

## The entry

> I can summon rain, but only inside umbrellas that people have already closed.

Rain summoned into an umbrella that is already closed wets nobody, waters nothing, and helps no one — the power achieves exactly nothing, and a closed umbrella is the one place rain can do no good at all.

## How it works

`main.py` (pure Python 3 standard library, no dependencies, no network) writes the single line above to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before writing, it verifies the text against the competition gate (1–140 characters, one line) and against its pinned byte count (77 bytes) and SHA-256 (`f615828526806afbb2a0e157a851cd9417347aae480330e5f01cc36d572a048c`), so both grader runs produce byte-identical output.

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
