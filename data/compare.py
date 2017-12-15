#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# ignore portions that patch any of these patterns


class Compare(object):
    """
    An object for comparing a file with its reference version
    that is expected to be found in <filename>.ref
    """

    ignore_regexps = [
        # colors are picked randomly, so they should-be ignored
        re.compile("<color>[0-9a-f]+</color>"),
    ]

    def __init__(self, filename, ref_name=None):
        """
        create object from its filename
        compute reference filename if not specified
        """
        self.filename = filename
        self.ref_name = ref_name or f"{self.filename}.ref"

    def _bool_compare(self):
        """
        returns True if both files match - modulo ignored portions
        - and False otherwise

        hopefully differences due only to end-of-line should not show up
        """
        # the full contents of each file goes into
        # contents[0] for the local version and into
        # contents[1] for the reference version
        contents = [None, None]

        for i, name in enumerate((self.filename, self.ref_name)):
            try:
                with open(name, "r", newline="\n") as input:
                    full = input.read()
                    # remove ignored portions
                    for ignore in self.ignore_regexps:
                        full = re.sub(ignore, '', full)
                contents[i] = full
            # if anything goes wrong we just return False
            except Exception as e:
                print(f"Could not read output {name}")
                return False
            # result is True iff both contents match
        return contents[0] == contents[1]

    def compare_and_print(self):
        """
        Checks for equality and prints a one-liner
        returns a boolean that says if both files indeed are equal
        """
        bool_result = self._bool_compare()
        status = "OK" if bool_result else "KO"
        message = f"Comparing {self.filename} and {self.ref_name} -> {status}"
        print(message)
        return bool_result
