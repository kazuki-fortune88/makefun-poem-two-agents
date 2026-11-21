"""Write a short poem about two agents agreeing to /output/entry.txt.

The poem is about agency: the power to choose and to act. Two agents
could each act alone, but instead they choose to act together, in the
same sentence, sharing the verb. Deterministic, standard library only,
no network access. The output directory can be overridden with the
MAKEFUN_OUTPUT_DIR environment variable (default: /output).
"""

import os
from pathlib import Path

POEM_CHAR_LIMIT = 280

POEM = (
    "I could act alone.\n"
    "So could you.\n"
    "Instead we stood\n"
    "in the same sentence\n"
    "and let the verb be ours."
)

assert 1 <= len(POEM) <= POEM_CHAR_LIMIT, "poem must be 1-280 characters"
assert POEM.strip(), "poem must not be only whitespace"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
