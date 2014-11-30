#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

class Compare(object):
    """
    An object for comparing a file with its reference version
    that is expected to be found in <filename>.ref
    """
    def __init__(self, out_name, ref_name=None):
        "constructor computes reference filename"
        self.out_name = out_name
        self.ref_name = ref_name or "{}.ref".format(self.out_name)
        
    def _bool_compare(self):
        """
        returns True if files match and False otherwise
        hopefully differences due only to end-of-line should not show up
        since we open both files in universal-end-of-line mode
        """
        # the full contents of each file goes into
        # contents[0] for the local version and into
        # contents[1] for the reference version
        contents = [None, None]
        for i, name in enumerate( [self.out_name, self.ref_name] ):
            try:
                with open(name, "ru") as output:
                    contents[i] = output.read()
            # if anything goes wrong we just return False
            except Exception as e:
                print ("Could not read output {}".format(name))
                return False
        # result if True iff both contents match
        return contents[0] == contents[1]

    def compare_and_print(self):
        """
        Checks for equality and prints a one-liner
        returns a boolean that says if both files indeed are equal
        """
        bool_result = self._bool_compare()
        status = "OK" if bool_result else "KO"
        message = "Comparing {self.out_name} and {self.ref_name} -> {status}".\
                  format(**locals())
        print (message)
        return bool_result

