from gedReader import readers
import io


block1 = """0 @P1@ INDI 
1 BIRT 
2 DATE 04 Nov 1964
2 PLAC Cape Girardeau, Cape Girardeau, Missouri, USA
2 SOUR @S663924261@
2 SOUR @S663924264@
1 RESI 
2 PLAC Manchester, MO
2 SOUR @S663924264@
3 _APID 1,1732::61025647
1 NAME Bradley Scott /Schwab/
2 SOUR @S663924261@
2 SOUR @S663924264@
1 SEX M
1 RESI 
2 DATE Dec 1987
2 PLAC St Louis, MO
2 SOUR @S663924261@
0 @P2@ INDI 
1 BIRT 
2 DATE 08 nov 1937
2 PLAC Missouri
2 SOUR @S663802507@
3 PAGE Year: 1940; Census Place: Cape Girardeau, Cape Girardeau, Missouri; Roll: T627_2093; Page: 8A; Enumeration District: 16-11A
3 _APID 1,2442::94736775
2 SOUR @S663922837@
3 PAGE "U.S., School Yearbooks, 1880-2012"; Year: 1954
3 _APID 1,1265::409167193
2 SOUR @S663922837@
3 PAGE "U.S., School Yearbooks, 1880-2012"; Year: 1952
3 _APID 1,1265::415048175
2 SOUR @S663922837@
3 PAGE "U.S., School Yearbooks, 1880-2012"; Year: 1952
3 _APID 1,1265::415048639
1 RESI 
"""


def test_read_next_root_block():
    text = io.StringIO(block1)
    block = readers.read_next_root_block(text)
    assert len(block) == 19, "not a full block was read"
