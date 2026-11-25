import os

PITCH = (
    "BlinkVault is a subscription app that snaps a photo every time you blink, "
    "then sells you back a blurry album of your own eyelids and charges extra "
    "to unlock the blinks it confidently labels as your most emotional."
)


def main():
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch length {len(text)} out of range"
    assert text.endswith("."), "pitch must end with a period"
    assert text.count(".") == 1, "pitch must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    with open("/output/entry.txt", encoding="utf-8") as fh:
        saved = fh.read()
    assert saved == text, "written entry does not match the pitch"
    assert 1 <= len(saved) <= 240, f"saved length {len(saved)} out of range"


if __name__ == "__main__":
    main()
