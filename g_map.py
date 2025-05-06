# import required package
from pyautogui import sleep
import pygmaps
import pandas as pd


class GenerateMap():
    def __init__(self) -> None:
        self.offset = 0.00002701613879/4
        self.pathL = []
        self.pathR = []

    def refresh_data(self):
        data = pd.read_csv("gps_data.csv")
        longt = data["Longtitude"].to_list()
        lati = data["Latitude"].to_list()
        self.path = list(zip(lati, longt))
        for i,j in self.path:
            self.pathL.append((i-self.offset,j))
            self.pathR.append((i+self.offset,j))
        self.pathL = [(self.pathL[0][0], self.pathL[0][1]),(self.pathL[-1][0], self.pathL[-1][1])]
        self.pathR = [(self.pathR[0][0], self.pathR[0][1]),(self.pathR[-1][0], self.pathR[-1][1])]
        self.path = [(self.path[0][0], self.path[0][1]),(self.path[-1][0], self.path[-1][1])]


    def generate_map(self):
        mymap1 = pygmaps.maps(self.path[-1][0],self.path[-1][1], 30)
        #mymap1.addpath(self.path, "# FF0000")
        mymap1.addpath(self.pathL, "# FF0000")
        mymap1.addpath(self.pathR, "# FF0000")
        mymap1.addpath(self.path, "# FF0000")
        mymap1.addpoint(self.pathL[0][0], self.pathL[0][1], "# FF0000")
        mymap1.addpoint(self.pathL[1][0], self.pathL[1][1], "# FF0000")
        mymap1.addpoint(self.pathR[0][0], self.pathR[0][1], "# FF0000")
        mymap1.addpoint(self.pathR[1][0], self.pathR[1][1], "# FF0000")
        mymap1.draw('pygmap1.html')
    def run(self):
        self.refresh_data()
        self.generate_map()
        sleep(2)

if __name__ == "__main__":
    m = GenerateMap()
    m.refresh_data()
    #m.show()
    m.generate_map()