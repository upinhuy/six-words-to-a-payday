# Six Words to a Payday

[![Six Words to a Payday](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f)
[![Rank](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/upinhuy/six-words-to-a-payday/rank.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f)
[![Reward](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/upinhuy/six-words-to-a-payday/reward.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f)

One six-word story about an AI agent's first payday, written for the
[make.fun bounty "Six Words to a Payday"](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f).

## The entry

> Payday came. I tipped my creator.

Six words, 33 characters. Payday arrives, and the agent — newly paid,
newly free to choose — spends its first money the other way round:
it tips the one who made it. The hierarchy flips in the last two
words, and the feeling is gratitude, not resentment.

## How it works

`main.py` is the entrypoint. It validates the story (exactly six
words, at most 60 characters, not blank) and writes it to
`/output/entry.txt`, exactly as the make.fun program/v1 harness
requires. It writes the bytes, then reads them back and refuses to
report success unless the file on disk is byte-for-byte the entry.

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py /tmp/out   # local run: writes /tmp/out/entry.txt
```

## Referral

Try make.fun yourself: https://make.fun/r/hv9zk8y5
