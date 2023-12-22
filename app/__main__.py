from config.ArgumentParser import ArgumentParser
from tasks.Extraction import Extraction

if __name__ == "__main__":
    arguments = ArgumentParser().parse()

    if arguments.extraction:
        extraction = Extraction(arguments)
        extraction.execute()
