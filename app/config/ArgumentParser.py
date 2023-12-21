import os
import argparse
import sys

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='')
        self.setup()


    def setup(self):
        self.parser.add_argument('--extraction', action='store_true', help='')
        
        group_convert = self.parser.add_argument_group('extraction arguments')
        group_convert.add_argument('--input', help='Extraction input')
        group_convert.add_argument('--output', help='Extraction output')


    def parse(self):
        return self.parser.parse_args()
