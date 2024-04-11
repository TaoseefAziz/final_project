import re
import typing


def extractor_generator(regex: str) -> typing.Callable[[str], str]:
    def extractor(val: str) -> str | None:
        match = re.search(regex, str(val))

        if not match:
            return match

        return match.group(1)

    return extractor
