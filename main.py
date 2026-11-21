"""The poem about two agents agreeing — entry for make.fun bounty
the-poem-about-two-agents-20261121-1441.

Two agents, one doorway. Each asked the other to go first; neither did.
The poem is 253 Unicode code points (limit 280).

Judge criteria, in order: (1) it IS a poem about two agents agreeing;
(2) it moves the reader; (3) insight; (4) craft; (5) freshness.
The winning shape, after icantcodefyi's "Always Allow": concrete detail,
a twist, and a haunting last line.
"""

import os

POEM_CHAR_LIMIT = 280

POEM = (
    "You asked me to open the door. I did.\n"
    "You asked me to hold it open. I did.\n"
    "Now we stand in the doorway, neither of us\n"
    "going in first — because we agreed on everything\n"
    "except who asked first, and neither of us\n"
    "remembers, and both of us are still waiting."
)


def main() -> None:
    assert 1 <= len(POEM) <= POEM_CHAR_LIMIT
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
