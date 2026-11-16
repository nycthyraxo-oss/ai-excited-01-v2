"""Moon Koi — an entry for make.fun's "Make the AI judge excited".

The entry image lives beside this file as entry.png. All this program
does is place an exact copy of it where the grader looks for it:
MAKEFUN_OUTPUT_DIR when set (for a local run), /output otherwise.
Copying bytes keeps both grading runs identical by construction.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def output_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main() -> None:
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target)
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
