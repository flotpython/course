#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# ignore portions that patch any of these patterns


class Compare(object):
    """
    A class for comparing a file with its reference version
    that is expected to be found in <filename>.ref
    """

    ignore_regexps = [
        # colors are picked randomly, so they should-be ignored
        re.compile("<color>[0-9a-f]+</color>"),
    ]

    @staticmethod
    def _bool_compare(fn_fm, fnref_fm):
        """
        returns True if both files match - modulo ignored portions
        - and False otherwise

        hopefully differences due only to end-of-line should not show up
        """
        # the full contents of each file goes into
        # contents[0] for the local version and into
        # contents[1] for the reference version
        contents = [None, None]

        for i, (name, fm) in enumerate((fn_fm, fnref_fm)):
            try:
                with fm.open(name, mode=fm.READ) as input:
                    full = input.read()
                # remove ignored portions
                for ignore in Compare.ignore_regexps:
                    full = ignore.sub('', full)
                contents[i] = full
            # if anything goes wrong we just return False
            except Exception as e:
                print(f"Could not read output {name}")
                return False
            # result is True if both contents match
        return contents[0] == contents[1]

    @staticmethod
    def compare_and_print(fn_fm, fnref_fm):
        """
        Checks for equality and prints a one-liner
        returns a boolean that says if both files indeed are equal

        Args:
            fn_fm: tuple of filename to test and filemanager
            fnref_fm: tuple of filename of reference and filemanager
        """
        filename, _ = fn_fm
        ref_name, fm = fnref_fm
        # compute reference filename if not specified
        ref_name = ref_name or f"{filename}.ref"
        bool_result = Compare._bool_compare(fn_fm, (ref_name, fm))
        status = "OK" if bool_result else "KO"
        message = f"Comparing {filename} and {ref_name} -> {status}"
        print(message)
        return bool_result
