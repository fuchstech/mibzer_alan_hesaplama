import threading 
from g_map import GenerateMap
import refreshmap
import gps_data

m = GenerateMap()
map = threading.Thread(m.run())
brow = threading.Thread(refreshmap.runmap())
gps = threading.Thread(gps_data.get_gps())

map.start()
brow.start()
gps.start()
