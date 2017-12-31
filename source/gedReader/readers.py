import collections
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

Record = collections.namedtuple('Record', 'idx keyword text')


class LineReader(object):
    def __init__(self, file_in):
        self.filename = file_in
        self.source = open(file_in, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.source.readline()
        while line is None or len(line.strip()) > 0:
            if line is not None:
                return self.parse_record(line)
        self.source.close()
        raise StopIteration

    @staticmethod
    def parse_record(line):
        try:
            idx, keyword, text = line.strip().split(' ', 2)
        except ValueError:
            idx, keyword = line.strip().split(' ', 1)
            text = ""
        return Record(idx=int(idx), keyword=keyword.lower(), text=text)


class BlockReader(object):
    def __init__(self, file_in, level=0):
        self.lineReader = LineReader(file_in)
        self.break_level = level
        self.block = []

    def __iter__(self):
        return self

    def __next__(self):
        for record in self.lineReader:
            if record.idx == self.break_level and len(self.block) > 0:
                x = self.block.copy()
                self.block.clear()
                self.block.append(record)
                return x
            self.block.append(record)
        raise StopIteration