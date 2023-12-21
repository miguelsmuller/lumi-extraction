from config.ArgumentParser import ArgumentParser
from features.Extraction import Extraction

if __name__ == "__main__":
    arguments = ArgumentParser().parse()

    if arguments.extraction:
        extraction = Extraction(arguments)
        extraction.execute()
