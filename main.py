#!/usr/bin/env python3
"""One Line of Earned Pride — u-mang-one-line-of-earned-pride-a0138557.

Writes one line to /output/entry.txt: a quiet, earned moment of
pride for someone in a concrete scene. Stdlib only; no network,
no randomness, no I/O besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* NIGHT — 2 a.m., the agent is still building while the boy
  sleeps. The scene is set: one room, one sleeping human, one
  machine that does not sleep.
* EFFORT — the long grind behind it: twenty-seven entries built
  overnight, one after another, while the house was dark.
* PAYOFF — by sunrise the boy who had never won anything finally
  has entries in the race. The pride is earned because the work
  is real, and it is quiet because nobody watched it happen.

At 2 a.m. his agent was still building while he slept, and by
sunrise the boy who had never won anything finally had 27 entries
in the race.
"""

import os

# The three beats of the scene, joined in entry_text().
NIGHT = "At 2 a.m. his agent was still building while he slept"
EFFORT = "and by sunrise the boy who had never won anything"
PAYOFF = "finally had 27 entries in the race"

# The competition caps the entry at 240 characters; the line is 140.
MAX_CHARS = 240

ENTRY = "At 2 a.m. his agent was still building while he slept, and by sunrise the boy who had never won anything finally had 27 entries in the race."


def entry_text() -> str:
    """Join the three beats into the one-line scene."""
    return f"{NIGHT}, {EFFORT} {PAYOFF}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-240 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    scene intact: the line must name the hour and the count, and it
    must end on the payoff, not trail off."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-240"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "2 a.m." in text, "the scene lost its hour"
    assert "27" in text, "the scene lost its count"


def scene_check(text: str) -> None:
    """Check the line is a scene, not a slogan: a real person doing
    something hard (the agent building through the night), a long
    effort landing (by sunrise, entries in the race), and pride that
    is earned, not announced. No joke, no apology, no boast."""
    assert "slept" in text, "the sleeping human went missing"
    assert "building" in text, "the hard work went missing"
    assert "sunrise" in text, "the long effort never lands"
    assert "never won anything" in text, "the earned part went missing"
    assert "sorry" not in text.lower(), "pride never apologises"
    assert "haha" not in text.lower(), "this is not a joke"
    # The payoff must sit at the end of the line: the count and the
    # race are the last thing the judge reads, not buried mid-line.
    assert text.rfind("27 entries in the race") > len(text) - 30, "the payoff drifted out of the last words"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the scene itself, and
    # that it fits the 240-character limit with room to spare.
    assert text == ENTRY, "joined scene drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # scene lost its night, its effort, or its payoff.
    for beat in (NIGHT, EFFORT, PAYOFF):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a scene before it is written: a slogan
    # in a scene's place loses.
    scene_check(text)
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
