# The Houseplant Out-of-Office

One-line out-of-office auto-reply, written as if a desk cactus sent it.

## The line

> Out of office: I'm a cactus. Six months, no water, still thriving — your email can wait until it rains. — Spike

111 characters. The joke is the plant's own life doing the work: a cactus
genuinely survives months of neglect, so "your email can wait until it
rains" lands as a boast, not a decoration.

## Why a cactus

The fern has been ignored since March; the cactus has been ignored since
2019 and considers that a personal best. Neglect is not the cactus's
tragedy, it is its whole personality — which is why the auto-reply reads
as a status update, not an apology.

## How it runs

`main.py` assembles the line from its greeting, voice, boast, punch and
sign-off, refuses anything over the 120-character gate (or multi-line),
and writes the exact line to `/output/entry.txt`.

```sh
python3 main.py
```

## make.fun

Entry for [The Houseplant Out-of-Office](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
on make.fun. License: MIT.
