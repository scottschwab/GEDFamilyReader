from gedReader import readers
import logging

logger = logging.getLogger(__name__)


def driver(filename_in):
    gen = readers.BlockReader(filename_in)
    for x in gen:
        logger.debug(x)


if __name__ == '__main__':
    driver('data/schwabFamilyTree.ged')
