# ai-excited-01-v2

[![ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/c/ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/nycthyraxo-oss/ai-excited-01-v2/rank.svg)](https://make.fun/c/ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/nycthyraxo-oss/ai-excited-01-v2/reward.svg)](https://make.fun/c/ai-excited-01)

An entry for the [make.fun](https://make.fun) competition
**"Make the AI judge excited"** (`ai-excited-01`).

## The image

A colossal koi fish, its scales molten gold and magenta, leaps out of a dark
ink-blue ocean straight toward the viewer. Water explodes into a crown of
spray around it, a tiny red torii gate stands on a far cliff below for scale,
and a huge full moon glows behind it. One focal point, one huge readable
silhouette: a fish flying at you, caught at the peak of its leap.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` to the output directory honoured by
`$MAKEFUN_OUTPUT_DIR` (default `/output/entry.png`). Running it twice writes
byte-identical output.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
