#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (program/v1) to /output/entry.txt.
Deterministic, no network, no secrets.

The entry is exactly 144 characters (verified with len()): one sentence,
well under the 320-char gate. The angle — lawmakers Googling "how to PDF"
on the very machine they just voted to regulate — beats the saturated
field: a study of 1001 submissions found the intern/aide, committee,
print-scan-email, final_FINAL_v7.docx and phone-photo angles all crowded,
while "Googling how to PDF" had zero hits. The punch lands on the last
few words ("they just voted to regulate"), undercutting the setup's
authority (a 412-3 vote) with the file they cannot convert.
"""

import os

ENTRY = (
    "They voted 412-3 to regulate artificial intelligence, then spent "
    "the afternoon Googling 'how to PDF' on the machine they just voted "
    "to regulate."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
