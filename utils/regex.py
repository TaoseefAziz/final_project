import re
import typing


def extractor_generator(regex: str) -> typing.Callable[[str], str]:
    """
    Given a regex string with ONE GROUP, return a function that extracts that group from an input string

    :param regex: the regex string, which should contain exactly one group
    :return: the extracting function
    """

    def extractor(val: str) -> str | None:
        match = re.search(regex, str(val))

        if not match:
            return match

        return match.group(1)

    return extractor
