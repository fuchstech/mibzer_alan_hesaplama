#! /usr/bin/env python3
"""
example  Python gpsd client
run this way: python3 example1.py.txt
"""

import gps               # the gpsd interface module
from time import sleep 
#os.system("gpsd -N udp://192.168.118.57:9988")
session = gps.gps(mode=gps.WATCH_ENABLE)
liste = []
def get_gps():
    print("gps started")
    while 1:
        try:
            while 0 == session.read():
                if not (gps.MODE_SET & session.valid):
                    # not useful, probably not a TPV message
                    continue

                print('Mode: %s(%d) Time: ' %
                    (("Invalid", "NO_FIX", "2D", "3D")[session.fix.mode],
                    session.fix.mode), end="")
                # print time, if we have it
                if gps.TIME_SET & session.valid:
                    print(session.fix.time, end="")
                else:
                    print('n/a', end="")
                #sleep(1)
                if ((gps.isfinite(session.fix.latitude) and
                    gps.isfinite(session.fix.longitude))):
                    print(" Lat %.6f Lon %.6f" %
                        (session.fix.latitude, session.fix.longitude))
                    liste.append((session.fix.latitude, session.fix.longitude))
                    if liste[-2:][0] != (session.fix.latitude, session.fix.longitude):
                        with open("gps_data.csv","a") as file:
                            file.write(str(session.fix.latitude)+","+str(session.fix.longitude)+"\n")
                else:
                    print(" Lat n/a Lon n/a")

        except KeyboardInterrupt:
            # got a ^C.  Say bye, bye
            print('')
            session.close()

# Got ^C, or fell out of the loop.  Cleanup, and leave.
if __name__=="__main__":
    get_gps()