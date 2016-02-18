from pyiso import client_factory
from unittest import TestCase
from io import StringIO
from datetime import date, datetime
import pytz


class TestNYISOBase(TestCase):
    def setUp(self):
        self.load_csv = StringIO(u'"Time Stamp","Time Zone","Name","PTID","Load"\n\
"09/10/2014 00:00:00","EDT","CAPITL",61757,1173.2\n\
"09/10/2014 00:00:00","EDT","CENTRL",61754,1591.2\n\
"09/10/2014 00:00:00","EDT","DUNWOD",61760,609.4\n\
"09/10/2014 00:00:00","EDT","GENESE",61753,1003.3\n\
"09/10/2014 00:00:00","EDT","HUD VL",61758,965.4\n\
"09/10/2014 00:00:00","EDT","LONGIL",61762,2099.7\n\
"09/10/2014 00:00:00","EDT","MHK VL",61756,714.7\n\
"09/10/2014 00:00:00","EDT","MILLWD",61759,235.5\n\
"09/10/2014 00:00:00","EDT","N.Y.C.",61761,5546.5\n\
"09/10/2014 00:00:00","EDT","NORTH",61755,436.2\n\
"09/10/2014 00:00:00","EDT","WEST",61752,1707.7\n\
"09/10/2014 00:05:00","EDT","CAPITL",61757,1180\n\
"09/10/2014 00:05:00","EDT","CENTRL",61754,1577.1\n\
"09/10/2014 00:05:00","EDT","DUNWOD",61760,596.2\n\
"09/10/2014 00:05:00","EDT","GENESE",61753,994.1\n\
"09/10/2014 00:05:00","EDT","HUD VL",61758,943.9\n\
"09/10/2014 00:05:00","EDT","LONGIL",61762,2083.9\n\
"09/10/2014 00:05:00","EDT","MHK VL",61756,723\n\
"09/10/2014 00:05:00","EDT","MILLWD",61759,240.1\n\
"09/10/2014 00:05:00","EDT","N.Y.C.",61761,5473.5\n\
"09/10/2014 00:05:00","EDT","NORTH",61755,421.1\n\
"09/10/2014 00:05:00","EDT","WEST",61752,1689.6\n\
"09/10/2014 00:10:00","EDT","CAPITL",61757,1172.8\n\
"09/10/2014 00:10:00","EDT","CENTRL",61754,1569.1\n\
"09/10/2014 00:10:00","EDT","DUNWOD",61760,601.2\n\
"09/10/2014 00:10:00","EDT","GENESE",61753,992.6\n\
"09/10/2014 00:10:00","EDT","HUD VL",61758,935.1\n\
"09/10/2014 00:10:00","EDT","LONGIL",61762,2067.5\n\
"09/10/2014 00:10:00","EDT","MHK VL",61756,712.9\n\
"09/10/2014 00:10:00","EDT","MILLWD",61759,247.2\n\
"09/10/2014 00:10:00","EDT","N.Y.C.",61761,5428.1\n\
"09/10/2014 00:10:00","EDT","NORTH",61755,431.4\n\
"09/10/2014 00:10:00","EDT","WEST",61752,1676.3\n\
"09/10/2014 00:15:00","EDT","CAPITL",61757,1172.8\n\
"09/10/2014 00:15:00","EDT","CENTRL",61754,1570.5\n\
"09/10/2014 00:15:00","EDT","DUNWOD",61760,595.8\n\
"09/10/2014 00:15:00","EDT","GENESE",61753,978.9\n\
"09/10/2014 00:15:00","EDT","HUD VL",61758,934.7\n\
"09/10/2014 00:15:00","EDT","LONGIL",61762,2040.8\n\
"09/10/2014 00:15:00","EDT","MHK VL",61756,724.5\n\
"09/10/2014 00:15:00","EDT","MILLWD",61759,235.8\n\
"09/10/2014 00:15:00","EDT","N.Y.C.",61761,5399.5\n\
"09/10/2014 00:15:00","EDT","NORTH",61755,430.3\n\
"09/10/2014 00:15:00","EDT","WEST",61752,1661.1\n\
"09/10/2014 19:35:00","EDT","CAPITL",61757,\n\
"09/10/2014 19:35:00","EDT","CENTRL",61754,\n\
"09/10/2014 19:35:00","EDT","DUNWOD",61760,\n\
"09/10/2014 19:35:00","EDT","GENESE",61753,\n\
"09/10/2014 19:35:00","EDT","HUD VL",61758,\n\
"09/10/2014 19:35:00","EDT","LONGIL",61762,\n\
"09/10/2014 19:35:00","EDT","MHK VL",61756,\n\
"09/10/2014 19:35:00","EDT","MILLWD",61759,\n\
"09/10/2014 19:35:00","EDT","N.Y.C.",61761,\n\
"09/10/2014 19:35:00","EDT","NORTH",61755,\n\
"09/10/2014 19:35:00","EDT","WEST",61752,\n\
')

        self.load_forecast_csv = """
"Time Stamp","Capitl","Centrl","Dunwod","Genese","Hud Vl","Longil","Mhk Vl","Millwd","N.Y.C.","North","West","NYISO"
"11/22/2015 00:00",1047,1447,541,842,844,1749,571,223,4522,474,1459,13719
"11/22/2015 01:00",1010,1415,516,823,810,1658,555,216,4330,468,1434,13235
"11/22/2015 02:00",990,1388,503,809,793,1603,547,217,4193,467,1418,12928
"11/22/2015 03:00",970,1372,491,799,775,1560,538,212,4125,467,1401,12710
"11/22/2015 04:00",929,1327,460,758,740,1507,502,177,4039,439,1367,12245
"11/22/2015 05:00",937,1341,464,785,753,1511,527,202,3961,463,1372,12316
"11/22/2015 06:00",1003,1427,483,839,803,1587,579,215,4028,475,1430,12869
"11/22/2015 07:00",1087,1524,523,890,864,1694,624,232,4266,494,1500,13698
"11/22/2015 08:00",1148,1578,558,925,919,1812,660,241,4539,502,1540,14422
"11/22/2015 09:00",1184,1606,583,946,944,1893,680,246,4792,508,1563,14945
"11/22/2015 10:00",1200,1629,606,962,959,1945,687,248,4981,507,1588,15312
"11/22/2015 11:00",1204,1642,608,977,961,1966,688,247,5077,505,1592,15467
"11/22/2015 12:00",1188,1628,613,970,954,1979,680,247,5127,503,1589,15478
"11/22/2015 13:00",1185,1628,613,972,956,1978,673,243,5136,499,1600,15483
"11/22/2015 14:00",1189,1634,614,977,958,2001,674,242,5131,497,1609,15526
"11/22/2015 15:00",1212,1653,616,985,973,2048,682,247,5155,499,1616,15686
"11/22/2015 16:00",1295,1721,651,1028,1033,2196,728,268,5303,514,1663,16400
"11/22/2015 17:00",1405,1866,710,1133,1138,2425,791,307,5609,534,1784,17702
"11/22/2015 18:00",1415,1894,724,1144,1152,2446,799,323,5664,535,1819,17915
"11/22/2015 19:00",1391,1878,720,1129,1132,2418,787,321,5631,534,1807,17748
"11/22/2015 20:00",1353,1843,704,1100,1103,2361,767,313,5547,526,1782,17399
"11/22/2015 21:00",1290,1784,676,1058,1055,2250,712,296,5392,517,1741,16771
"11/22/2015 22:00",1211,1700,634,999,992,2092,679,275,5169,507,1696,15954
"11/22/2015 23:00",1142,1618,593,943,924,1910,638,248,4882,499,1614,15011
"11/23/2015 00:00",1066,1522,541,875,860,1758,616,223,4532,494,1553,14040
"11/23/2015 01:00",1030,1495,513,855,827,1670,610,206,4348,508,1521,13583
"11/23/2015 02:00",1019,1480,500,854,808,1631,613,217,4225,493,1509,13349
"11/23/2015 03:00",1029,1487,497,864,811,1618,625,230,4174,498,1506,13339
"11/23/2015 04:00",1084,1550,528,904,850,1678,641,255,4237,510,1547,13784
"11/23/2015 05:00",1134,1655,550,961,885,1778,691,257,4457,523,1605,14496
"11/23/2015 06:00",1279,1835,621,1075,995,2015,796,292,4954,547,1767,16176
"11/23/2015 07:00",1360,1936,673,1143,1060,2160,835,310,5485,560,1861,17383
"11/23/2015 08:00",1363,1948,689,1156,1085,2223,838,307,5854,558,1882,17903
"11/23/2015 09:00",1360,1946,698,1159,1084,2250,837,302,6095,553,1889,18173
"11/23/2015 10:00",1351,1950,707,1159,1082,2261,830,297,6216,549,1904,18306
"11/23/2015 11:00",1338,1939,706,1157,1070,2270,822,294,6265,546,1890,18297
"11/23/2015 12:00",1317,1913,707,1141,1060,2269,809,291,6288,541,1874,18210
"11/23/2015 13:00",1309,1919,707,1145,1058,2256,797,286,6280,537,1878,18172
"11/23/2015 14:00",1306,1905,706,1140,1057,2270,792,286,6266,534,1865,18127
"11/23/2015 15:00",1318,1904,712,1135,1066,2305,787,293,6289,535,1851,18195
"11/23/2015 16:00",1395,1953,747,1166,1127,2475,825,311,6414,551,1884,18848
"11/23/2015 17:00",1514,2090,810,1264,1246,2752,886,354,6640,570,1992,20118
"11/23/2015 18:00",1525,2111,820,1270,1268,2798,894,371,6544,572,2009,20182
"11/23/2015 19:00",1492,2069,805,1241,1255,2731,881,364,6388,568,1975,19769
"11/23/2015 20:00",1442,2014,776,1198,1212,2629,855,350,6198,556,1925,19155
"11/23/2015 21:00",1355,1911,731,1132,1140,2458,793,326,5924,541,1850,18161
"11/23/2015 22:00",1253,1791,669,1053,1052,2228,745,293,5553,527,1765,16929
"11/23/2015 23:00",1170,1680,609,980,962,1996,690,259,5113,515,1651,15625
"11/24/2015 00:00",1114,1590,562,925,898,1851,657,235,4744,506,1595,14677
"11/24/2015 01:00",1082,1548,533,895,856,1747,645,227,4474,500,1552,14059
"11/24/2015 02:00",1072,1522,519,881,843,1693,643,230,4319,509,1534,13765
"11/24/2015 03:00",1078,1522,511,886,847,1669,655,241,4250,512,1524,13695
"11/24/2015 04:00",1123,1591,537,913,892,1735,674,268,4301,520,1548,14102
"11/24/2015 05:00",1184,1681,564,975,925,1833,723,269,4526,533,1627,14840
"11/24/2015 06:00",1329,1853,639,1090,1033,2059,819,306,5027,560,1774,16489
"11/24/2015 07:00",1401,1947,688,1149,1089,2181,852,323,5548,571,1860,17609
"11/24/2015 08:00",1394,1947,701,1154,1106,2223,850,319,5896,569,1873,18032
"11/24/2015 09:00",1392,1939,708,1153,1099,2234,845,312,6110,566,1875,18233
"11/24/2015 10:00",1380,1950,714,1154,1093,2227,838,305,6207,560,1883,18311
"11/24/2015 11:00",1368,1939,713,1153,1079,2220,829,302,6241,554,1860,18258
"11/24/2015 12:00",1346,1922,713,1135,1068,2208,818,298,6253,550,1846,18157
"11/24/2015 13:00",1339,1894,712,1130,1064,2190,806,293,6238,545,1848,18059
"11/24/2015 14:00",1336,1879,710,1127,1062,2204,800,292,6222,541,1837,18010
"11/24/2015 15:00",1350,1871,715,1119,1070,2242,796,299,6239,542,1818,18061
"11/24/2015 16:00",1421,1920,749,1143,1130,2411,832,318,6360,557,1841,18682
"11/24/2015 17:00",1537,2062,809,1245,1246,2676,892,358,6588,576,1956,19945
"11/24/2015 18:00",1545,2080,817,1250,1269,2719,899,374,6499,578,1984,20014
"11/24/2015 19:00",1516,2054,804,1231,1259,2663,885,368,6348,575,1966,19669
"11/24/2015 20:00",1468,1998,777,1190,1220,2571,859,354,6163,562,1926,19088
"11/24/2015 21:00",1377,1900,731,1127,1151,2412,795,330,5898,545,1861,18127
"11/24/2015 22:00",1278,1772,668,1045,1062,2195,747,296,5532,528,1779,16902
"11/24/2015 23:00",1186,1664,608,973,972,1973,694,262,5097,516,1665,15610
"11/25/2015 00:00",1112,1575,560,917,899,1827,654,242,4727,512,1594,14619
"11/25/2015 01:00",1075,1526,529,886,856,1725,636,232,4464,506,1556,13991
"11/25/2015 02:00",1064,1494,515,869,838,1671,628,231,4309,514,1525,13658
"11/25/2015 03:00",1069,1493,506,876,837,1644,639,237,4234,518,1516,13569
"11/25/2015 04:00",1119,1566,528,906,878,1697,669,260,4274,526,1546,13969
"11/25/2015 05:00",1178,1648,558,968,919,1800,713,269,4501,538,1625,14717
"11/25/2015 06:00",1323,1834,632,1080,1028,2030,810,305,5004,564,1767,16377
"11/25/2015 07:00",1394,1931,681,1145,1081,2152,843,322,5518,575,1857,17499
"11/25/2015 08:00",1387,1926,694,1152,1097,2194,840,318,5859,572,1862,17901
"11/25/2015 09:00",1379,1919,701,1153,1089,2203,832,312,6070,568,1866,18092
"11/25/2015 10:00",1366,1913,708,1155,1084,2199,826,305,6164,563,1872,18155
"11/25/2015 11:00",1351,1901,707,1147,1071,2195,811,303,6193,556,1848,18083
"11/25/2015 12:00",1335,1878,707,1127,1059,2185,802,299,6208,553,1834,17987
"11/25/2015 13:00",1327,1864,707,1121,1054,2170,789,295,6190,549,1833,17899
"11/25/2015 14:00",1326,1844,704,1116,1053,2181,784,294,6174,545,1819,17840
"11/25/2015 15:00",1338,1834,711,1108,1062,2215,778,300,6194,548,1797,17885
"11/25/2015 16:00",1407,1875,745,1132,1120,2383,816,319,6317,565,1823,18502
"11/25/2015 17:00",1518,2024,804,1234,1238,2645,877,358,6540,583,1938,19759
"11/25/2015 18:00",1526,2053,810,1242,1257,2685,885,372,6433,584,1961,19808
"11/25/2015 19:00",1497,2026,795,1222,1245,2623,873,366,6274,581,1941,19443
"11/25/2015 20:00",1453,1972,767,1176,1206,2534,846,352,6080,568,1898,18852
"11/25/2015 21:00",1364,1874,718,1108,1137,2372,782,326,5818,551,1830,17880
"11/25/2015 22:00",1255,1747,656,1021,1046,2152,731,295,5464,534,1743,16644
"11/25/2015 23:00",1170,1636,598,945,953,1930,677,260,5033,522,1623,15347
"11/26/2015 00:00",1096,1536,554,882,892,1793,653,242,4662,505,1535,14350
"11/26/2015 01:00",1054,1450,530,839,867,1713,627,228,4437,507,1479,13731
"11/26/2015 02:00",1027,1397,517,809,853,1664,597,227,4273,512,1438,13314
"11/26/2015 03:00",1010,1376,503,794,838,1627,589,235,4182,512,1412,13078
"11/26/2015 04:00",1006,1360,491,778,823,1604,567,220,4138,513,1375,12875
"11/26/2015 05:00",1031,1401,511,822,855,1649,604,246,4202,522,1415,13258
"11/26/2015 06:00",1073,1451,542,858,882,1732,642,260,4329,533,1451,13753
"11/26/2015 07:00",1138,1524,565,884,931,1809,679,271,4504,535,1481,14321
"11/26/2015 08:00",1212,1590,602,924,991,1928,729,287,4737,554,1517,15071
"11/26/2015 09:00",1269,1634,627,956,1029,2035,766,295,4954,566,1553,15684
"11/26/2015 10:00",1290,1655,648,977,1051,2100,780,297,5132,565,1586,16081
"11/26/2015 11:00",1299,1658,657,990,1047,2144,779,299,5226,558,1586,16243
"11/26/2015 12:00",1260,1608,660,967,1032,2168,747,299,5245,555,1574,16115
"11/26/2015 13:00",1199,1539,648,923,1002,2146,694,285,5214,541,1536,15727
"11/26/2015 14:00",1148,1478,625,887,964,2091,656,273,5144,528,1499,15293
"11/26/2015 15:00",1111,1429,602,854,942,2031,634,266,5072,520,1458,14919
"11/26/2015 16:00",1123,1418,614,845,954,2051,647,278,5112,528,1454,15024
"11/26/2015 17:00",1152,1506,635,908,1000,2160,683,292,5250,536,1527,15649
"11/26/2015 18:00",1155,1517,625,915,1008,2126,697,292,5174,535,1559,15603
"11/26/2015 19:00",1160,1531,623,915,1004,2110,697,295,5090,538,1573,15536
"11/26/2015 20:00",1161,1534,619,915,1003,2097,690,292,5027,532,1581,15451
"11/26/2015 21:00",1147,1522,614,906,989,2075,662,288,4961,530,1577,15271
"11/26/2015 22:00",1104,1475,589,869,955,1998,642,273,4853,522,1560,14840
"11/26/2015 23:00",1064,1422,561,830,909,1867,612,251,4649,516,1488,14169
"11/27/2015 00:00",1025,1365,525,799,857,1753,598,238,4447,503,1436,13546
"11/27/2015 01:00",1003,1316,498,769,835,1660,576,218,4271,501,1400,13047
"11/27/2015 02:00",993,1285,485,747,811,1606,566,223,4134,509,1369,12728
"11/27/2015 03:00",987,1290,479,750,794,1572,575,227,4054,523,1361,12612
"11/27/2015 04:00",1018,1329,472,764,806,1584,589,208,4083,511,1364,12728
"11/27/2015 05:00",1046,1365,494,799,835,1648,611,235,4223,527,1403,13186
"11/27/2015 06:00",1102,1428,529,849,878,1748,653,251,4510,535,1470,13953
"11/27/2015 07:00",1148,1481,554,871,919,1832,686,261,4835,527,1513,14627
"11/27/2015 08:00",1203,1526,588,898,964,1926,714,273,5147,539,1550,15328
"11/27/2015 09:00",1242,1573,611,931,996,1987,735,279,5351,545,1577,15827
"11/27/2015 10:00",1243,1589,635,951,1015,2024,734,284,5498,544,1590,16107
"11/27/2015 11:00",1241,1593,646,958,1014,2039,733,284,5559,542,1582,16191
"11/27/2015 12:00",1232,1589,651,955,1012,2049,728,285,5604,538,1577,16220
"11/27/2015 13:00",1225,1583,643,941,1007,2042,719,277,5607,538,1570,16152
"11/27/2015 14:00",1225,1587,642,941,998,2060,718,277,5588,536,1556,16128
"11/27/2015 15:00",1251,1596,642,941,1009,2082,720,282,5612,534,1566,16235
"11/27/2015 16:00",1318,1645,677,977,1072,2242,756,299,5739,545,1609,16879
"11/27/2015 17:00",1386,1743,725,1078,1151,2493,796,331,5989,561,1742,17995
"11/27/2015 18:00",1367,1736,721,1073,1149,2511,788,338,5928,554,1749,17914
"11/27/2015 19:00",1319,1689,699,1035,1117,2449,765,327,5810,547,1715,17472
"11/27/2015 20:00",1281,1662,675,1006,1083,2365,739,314,5655,539,1686,17005
"11/27/2015 21:00",1228,1607,646,962,1036,2253,692,298,5456,531,1648,16357
"11/27/2015 22:00",1162,1530,617,908,979,2097,656,279,5209,519,1600,15556
"11/27/2015 23:00",1087,1449,576,846,903,1907,617,250,4905,511,1497,14548
"""

        self.trade_csv = StringIO(u'Timestamp,Interface Name,Point ID,Flow (MWH),Positive Limit (MWH),Negative Limit (MWH)\n\
09/10/2014 00:00,WEST CENTRAL,23312,-106.15,2250,-9999\n\
09/10/2014 00:00,SCH - PJM_HTP,325905,0,660,-660\n\
09/10/2014 00:00,UPNY CONED,23315,1102.21,4850,-9999\n\
09/10/2014 00:00,SCH - PJ - NY,23316,-163.13,2450,-1300\n\
09/10/2014 00:00,SCH - OH - NY,23317,1011.6,1900,-1900\n\
09/10/2014 00:00,SCH - NE - NY,23318,-66.48,1400,-1600\n\
09/10/2014 00:00,MOSES SOUTH,23319,1452.05,2150,-1600\n\
09/10/2014 00:00,SPR/DUN-SOUTH,23320,2032.45,4350,-9999\n\
09/10/2014 00:00,SCH - HQ - NY,23324,1057,1320,-500\n\
09/10/2014 00:00,DYSINGER EAST,23326,303.25,2850,-9999\n\
09/10/2014 00:00,CENTRAL EAST - VC,23330,1738.13,2235,-9999\n\
09/10/2014 00:00,SCH - NPX_CSC,325154,330,330,-330\n\
09/10/2014 00:00,SCH - HQ_CEDARS,325274,7,190,-40\n\
09/10/2014 00:00,SCH - NPX_1385,325277,57,200,-200\n\
09/10/2014 00:00,SCH - PJM_NEPTUNE,325305,495,660,-660\n\
09/10/2014 00:00,SCH - HQ_IMPORT_EXPORT,325376,1001,1310,-9999\n\
09/10/2014 00:00,SCH - PJM_VFT,325658,-14,315,-315\n\
09/10/2014 00:00,TOTAL EAST,23314,2274.4,6500,-9999\n\
09/10/2014 00:05,SCH - HQ_CEDARS,325274,0,190,-40\n\
09/10/2014 00:05,SCH - NPX_CSC,325154,330,330,-330\n\
09/10/2014 00:05,SCH - PJM_NEPTUNE,325305,330,660,-660\n\
09/10/2014 00:05,SCH - HQ_IMPORT_EXPORT,325376,1059,1310,-9999\n\
09/10/2014 00:05,SCH - PJM_VFT,325658,-28,315,-315\n\
09/10/2014 00:05,SCH - PJM_HTP,325905,0,660,-660\n\
09/10/2014 00:05,WEST CENTRAL,23312,-127.47,2250,-9999\n\
09/10/2014 00:05,TOTAL EAST,23314,2492.19,6500,-9999\n\
09/10/2014 00:05,UPNY CONED,23315,1201.06,4850,-9999\n\
09/10/2014 00:05,SCH - PJ - NY,23316,-56.74,2450,-1300\n\
09/10/2014 00:05,SCH - OH - NY,23317,961.71,1900,-1900\n\
09/10/2014 00:05,SCH - NE - NY,23318,-93.37,1400,-1600\n\
09/10/2014 00:05,MOSES SOUTH,23319,1496.56,2150,-1600\n\
09/10/2014 00:05,SPR/DUN-SOUTH,23320,1993.25,4350,-9999\n\
09/10/2014 00:05,SCH - HQ - NY,23324,1109,1320,-500\n\
09/10/2014 00:05,DYSINGER EAST,23326,274.64,2850,-9999\n\
09/10/2014 00:05,CENTRAL EAST - VC,23330,1794.95,2235,-9999\n\
09/10/2014 00:05,SCH - NPX_1385,325277,65,200,-200\n\
09/10/2014 00:10,WEST CENTRAL,23312,-81.81,2250,-9999\n\
09/10/2014 00:10,SCH - PJM_HTP,325905,0,660,-660\n\
09/10/2014 00:10,UPNY CONED,23315,1217.03,4850,-9999\n\
09/10/2014 00:10,SCH - PJ - NY,23316,-60.19,2450,-1300\n\
09/10/2014 00:10,SCH - OH - NY,23317,961.12,1900,-1900\n\
09/10/2014 00:10,SCH - NE - NY,23318,-92.84,1400,-1600\n\
09/10/2014 00:10,MOSES SOUTH,23319,1484.79,2150,-1600\n\
09/10/2014 00:10,SPR/DUN-SOUTH,23320,2036.56,4350,-9999\n\
09/10/2014 00:10,SCH - HQ - NY,23324,1109,1320,-500\n\
09/10/2014 00:10,DYSINGER EAST,23326,314.15,2850,-9999\n\
09/10/2014 00:10,CENTRAL EAST - VC,23330,1802.89,2235,-9999\n\
09/10/2014 00:10,SCH - NPX_CSC,325154,330,330,-330\n\
09/10/2014 19:55,MOSES SOUTH,23319,1896.72,2150,-1600\n\
09/10/2014 19:55,SCH - NE - NY,23318,-302.78,1400,-1600\n\
09/10/2014 19:55,SCH - HQ - NY,23324,1274,1320,-500\n\
09/10/2014 19:55,DYSINGER EAST,23326,413.3,2850,-9999\n\
09/10/2014 19:55,CENTRAL EAST - VC,23330,2072.8,2380,-9999\n\
09/10/2014 19:55,SCH - NPX_CSC,325154,330,330,-330\n\
09/10/2014 19:55,SCH - HQ_CEDARS,325274,83,190,-40\n\
09/10/2014 19:55,SCH - NPX_1385,325277,90,200,-200\n\
09/10/2014 19:55,SCH - PJM_NEPTUNE,325305,580,660,-660\n\
09/10/2014 19:55,SCH - HQ_IMPORT_EXPORT,325376,1014,1310,-9999\n\
09/10/2014 19:55,SCH - PJM_VFT,325658,69,315,-315\n\
09/10/2014 19:55,SCH - PJM_HTP,325905,0,660,-660\n\
09/10/2014 19:55,WEST CENTRAL,23312,-55.11,2250,-9999\n\
09/10/2014 19:55,TOTAL EAST,23314,2841.45,6500,-9999\n\
09/10/2014 19:55,UPNY CONED,23315,1569.15,4850,-9999\n\
09/10/2014 19:55,SCH - PJ - NY,23316,-320.58,2450,-1300\n\
09/10/2014 19:55,SCH - OH - NY,23317,1259.54,1900,-1900\n\
09/10/2014 19:55,SPR/DUN-SOUTH,23320,2380.44,4350,-9999\n\
')

        self.genmix_csv = StringIO(u'Time Stamp,Time Zone,Fuel Category,Gen MWh\n\
01/19/2016 00:05,EST,Dual Fuel,2678.0\n\
01/19/2016 00:05,EST,Hydro,2385.0\n\
01/19/2016 00:05,EST,Natural Gas,1820.0\n\
01/19/2016 00:05,EST,Nuclear,5425.0\n\
01/19/2016 00:05,EST,Other Fossil Fuels,169.0\n\
01/19/2016 00:05,EST,Other Renewables,248.0\n\
01/19/2016 00:05,EST,Wind,1173.0\n\
01/19/2016 00:10,EST,Dual Fuel,2583.0\n\
01/19/2016 00:10,EST,Hydro,2259.0\n\
01/19/2016 00:10,EST,Natural Gas,1772.0\n\
01/19/2016 00:10,EST,Nuclear,5427.0\n\
01/19/2016 00:10,EST,Other Fossil Fuels,168.0\n\
01/19/2016 00:10,EST,Other Renewables,252.0\n\
01/19/2016 00:10,EST,Wind,1182.0\n\
01/19/2016 00:15,EST,Dual Fuel,2531.0\n\
01/19/2016 00:15,EST,Hydro,2212.0\n\
01/19/2016 00:15,EST,Natural Gas,1724.0\n\
01/19/2016 00:15,EST,Nuclear,5424.0\n\
01/19/2016 00:15,EST,Other Fossil Fuels,167.0\n\
01/19/2016 00:15,EST,Other Renewables,248.0\n\
01/19/2016 00:15,EST,Wind,1173.0\n\
')

        self.lmp_csv = StringIO(u'\n\
"Time Stamp","Name","PTID","LBMP ($/MWHr)","Marginal Cost Losses ($/MWHr)","Marginal Cost Congestion ($/MWHr)"\n\
"02/18/2016 00:15:00","CAPITL",61757,21.53,1.69,0.00\n\
"02/18/2016 00:15:00","CENTRL",61754,20.70,0.85,0.00\n\
"02/18/2016 00:15:00","DUNWOD",61760,21.73,1.89,0.00\n\
"02/18/2016 00:15:00","GENESE",61753,20.46,0.62,0.00\n\
"02/18/2016 00:15:00","H Q",61844,19.21,-0.64,0.00\n\
"02/18/2016 00:15:00","HUD VL",61758,21.73,1.89,0.00\n\
"02/18/2016 00:15:00","LONGIL",61762,21.97,2.12,0.00\n\
"02/18/2016 00:15:00","MHK VL",61756,20.86,1.01,0.00\n\
"02/18/2016 00:15:00","MILLWD",61759,21.77,1.92,0.00\n\
"02/18/2016 00:15:00","N.Y.C.",61761,21.85,2.00,0.00\n\
"02/18/2016 00:15:00","NORTH",61755,18.69,-1.15,0.00\n\
"02/18/2016 00:15:00","NPX",61845,21.55,1.71,0.00\n\
"02/18/2016 00:15:00","O H",61846,20.30,0.46,0.00\n\
"02/18/2016 00:15:00","PJM",61847,21.13,1.29,0.00\n\
"02/18/2016 00:15:00","WEST",61752,20.74,0.89,0.00\n\
"02/18/2016 00:30:00","CAPITL",61757,21.42,1.68,0.00\n\
"02/18/2016 00:30:00","CENTRL",61754,20.57,0.83,0.00\n\
"02/18/2016 00:30:00","DUNWOD",61760,21.64,1.90,0.00\n\
"02/18/2016 00:30:00","GENESE",61753,20.34,0.59,0.00\n\
"02/18/2016 00:30:00","H Q",61844,19.11,-0.63,0.00\n\
"02/18/2016 00:30:00","HUD VL",61758,21.62,1.88,0.00\n\
"02/18/2016 00:30:00","LONGIL",61762,21.90,2.15,0.00\n\
"02/18/2016 00:30:00","MHK VL",61756,20.73,0.99,0.00\n\
"02/18/2016 00:30:00","MILLWD",61759,21.66,1.91,0.00\n\
"02/18/2016 00:30:00","N.Y.C.",61761,21.72,1.97,0.00\n\
"02/18/2016 00:30:00","NORTH",61755,18.60,-1.15,0.00\n\
"02/18/2016 00:30:00","NPX",61845,21.46,1.72,0.00\n\
"02/18/2016 00:30:00","O H",61846,20.18,0.43,0.00\n\
"02/18/2016 00:30:00","PJM",61847,21.03,1.28,0.00\n\
"02/18/2016 00:30:00","WEST",61752,20.59,0.85,0.00\n\
"02/18/2016 00:45:00","CAPITL",61757,21.42,1.68,0.00\n\
"02/18/2016 00:45:00","CENTRL",61754,20.57,0.83,0.00\n\
"02/18/2016 00:45:00","DUNWOD",61760,21.62,1.88,0.00\n\
"02/18/2016 00:45:00","GENESE",61753,20.34,0.59,0.00\n\
"02/18/2016 00:45:00","H Q",61844,19.13,-0.61,0.00\n\
"02/18/2016 00:45:00","HUD VL",61758,21.62,1.88,0.00\n\
"02/18/2016 00:45:00","LONGIL",61762,21.90,2.15,0.00\n\
"02/18/2016 00:45:00","MHK VL",61756,20.73,0.99,0.00\n\
"02/18/2016 00:45:00","MILLWD",61759,21.66,1.91,0.00\n\
"02/18/2016 00:45:00","N.Y.C.",61761,21.70,1.96,0.00\n\
"02/18/2016 00:45:00","NORTH",61755,18.62,-1.12,0.00\n\
"02/18/2016 00:45:00","NPX",61845,21.46,1.72,0.00\n\
"02/18/2016 00:45:00","O H",61846,20.18,0.43,0.00\n\
"02/18/2016 00:45:00","PJM",61847,21.03,1.28,0.00\n\
"02/18/2016 00:45:00","WEST",61752,20.59,0.85,0.00')

    def test_parse_load_rtm(self):
        c = client_factory('NYISO')
        c.options = {'data': 'dummy'}
        data = c.parse_load_rtm(self.load_csv)
        for idx, row in data.iterrows():
            self.assertEqual(idx.date(), date(2014, 9, 10))
            self.assertGreater(row['load_MW'], 15700)
            self.assertLess(row['load_MW'], 16100)

        # should have 4 dps, even though file has 5 (last one has no data)
        self.assertEqual(len(data), 4)

    def test_parse_load_forecast(self):
        c = client_factory('NYISO')
        c.options = {'data': 'dummy'}
        data = c.parse_load_forecast(self.load_forecast_csv)
        for idx, row in data.iterrows():
            self.assertGreaterEqual(idx.date(), date(2015, 11, 22))
            self.assertLessEqual(idx.date(), date(2015, 11, 28))
            self.assertGreater(row['load_MW'], 12000)
            self.assertLess(row['load_MW'], 20200)

        # should have 6 days of hourly data
        self.assertEqual(len(data), 24*6)

    def test_parse_trade(self):
        c = client_factory('NYISO')
        c.options = {'data': 'dummy'}
        df = c.parse_trade(self.trade_csv)

        for idx, row in df.iterrows():
            self.assertEqual(idx.date(), date(2014, 9, 10))

            self.assertLess(row['net_exp_MW'], -1400)
            self.assertGreater(row['net_exp_MW'], -6300)

        # should have 3 timestamps
        self.assertEqual(len(df), 3)

        self.assertEqual(df.index.name, 'timestamp')

    def test_parse_genmix(self):
        c = client_factory('NYISO')
        c.options = {'data': 'dummy'}
        df = c.parse_genmix(self.genmix_csv)

        for idx, row in df.iterrows():
            self.assertEqual(idx.date(), date(2016, 1, 19))

            self.assertLess(row['gen_MW'], 5500)
            self.assertGreater(row['gen_MW'], 100)
            self.assertIn(row['fuel_name'], c.fuel_names.values())

        # should have 3 timestamps with 7 fuels
        self.assertEqual(len(df), 3*len(c.fuel_names))

        self.assertEqual(df.index.name, 'timestamp')

    def test_parse_lmp(self):
        c = client_factory('NYISO')
        c.options = {'data': 'lmp', 'node_id': 'LONGIL', 'latest': True}
        df = c.parse_lmp(self.lmp_csv)

        for idx, row in df.iterrows():
            self.assertEqual(idx.date(), date(2016, 2, 18))

            self.assertLess(row['lmp'], 1000)
            self.assertGreater(row['lmp'], -100)

            self.assertEqual(row['node_id'], 'LONGIL')

        self.assertEqual(df.index.name, 'timestamp')

    def test_fetch_csv_load(self):
        c = client_factory('NYISO')
        c.options = {'data': 'dummy'}
        now = pytz.utc.localize(datetime.utcnow())
        today = now.astimezone(pytz.timezone(c.TZ_NAME)).date()
        content_list = c.fetch_csvs(today, 'pal')
        self.assertEqual(len(content_list), 1)
        self.assertEqual(content_list[0].split('\r\n')[0],
                         '"Time Stamp","Time Zone","Name","PTID","Load"')

    def test_fetch_csv_load_forecast(self):
        c = client_factory('NYISO')
        c.options = {'data': 'dummy'}
        now = pytz.utc.localize(datetime.utcnow())
        today = now.astimezone(pytz.timezone(c.TZ_NAME)).date()
        content_list = c.fetch_csvs(today, 'isolf')
        self.assertEqual(len(content_list), 1)
        self.assertEqual(content_list[0].split('\n')[0],
                         '"Time Stamp","Capitl","Centrl","Dunwod","Genese","Hud Vl","Longil","Mhk Vl","Millwd","N.Y.C.","North","West","NYISO"')

    def test_fetch_csv_trade(self):
        c = client_factory('NYISO')
        c.options = {'data': 'dummy'}
        now = pytz.utc.localize(datetime.utcnow())
        today = now.astimezone(pytz.timezone(c.TZ_NAME)).date()
        content_list = c.fetch_csvs(today, 'ExternalLimitsFlows')
        self.assertEqual(len(content_list), 1)
        self.assertEqual(content_list[0].split('\r\n')[0],
                         'Timestamp,Interface Name,Point ID,Flow (MWH),Positive Limit (MWH),Negative Limit (MWH)')

    def test_fetch_csv_genmix(self):
        c = client_factory('NYISO')
        c.options = {'data': 'dummy'}
        now = pytz.utc.localize(datetime.utcnow())
        today = now.astimezone(pytz.timezone(c.TZ_NAME)).date()
        content_list = c.fetch_csvs(today, 'rtfuelmix')
        self.assertEqual(len(content_list), 1)
        self.assertEqual(content_list[0].split('\r\n')[0],
                         'Time Stamp,Time Zone,Fuel Category,Gen MWh')

    def test_fetch_csv_lmp(self):
        c = client_factory('NYISO')
        c.options = {'data': 'lmp'}
        now = pytz.utc.localize(datetime.utcnow())
        today = now.astimezone(pytz.timezone(c.TZ_NAME)).date()
        content_list = c.fetch_csvs(today, 'realtime')
        self.assertEqual(len(content_list), 1)
        self.assertEqual(content_list[0].split('\r\n')[0],
                         '"Time Stamp","Name","PTID","LBMP ($/MWHr)","Marginal Cost Losses ($/MWHr)","Marginal Cost Congestion ($/MWHr)"')
