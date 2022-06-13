# Polymorphism
# Different behavior happen depending on which
# subclass is being used, without having to explicit
# know what the subclass actually is.
# Liskov Substitution Principle

from pathlib import Path


class AudioFile:

    ext: str

    def __int__(self, filepath: Path) -> None:
        if not filepath.suffix == self.ext:
            raise ValueError("Invalid file format")
        self.filepath = filepath


class MP3File(AudioFile):
    ext = ".mp3"

    def play(self) -> None:
        print(f"playing {self.filepath} as mp3")


class WavFile(AudioFile):
    ext = ".wav"

    def play(self) -> None:
        print(f"playing {self.filepath} as wav")


class OggFile(AudioFile):
    ext = ".ogg"

    def play(self) -> None:
        print(f"playing {self.filepath} as ogg")


# Python allow us to use any object that provides the required behavior
# without forcing it to be a subclass.

class FlacFile:
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == ".flac":
            raise ValueError("Not a .flac file")
        self.filepath = filepath

    def play(self) -> None:
        print(f"playing {self.filepath} as flac")

# Este comportamiento reduce la necesidad de herencia multiple,
# generalmente, cuando se requiere de herencia multiple, se puede usar
# duck typing to mimic una de las clases a heredar.
