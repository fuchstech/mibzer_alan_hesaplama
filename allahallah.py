# Importing pygmaps
import pygmaps

mymap5 = pygmaps.maps(41.666680767,26.567793, 15)

latitude_list =[30.343769, 30.307977]
longitude_list =[77.999559, 78.048457]

for i in range(len(latitude_list)) :
	mymap5.addpoint(latitude_list[i], longitude_list[i], "# FF0000")

# list of coordinates		
path = [(41.666680767,26.567793),
		(41.666681433,26.56779255)]

# draw a line in b / w the given coordinates
# 1st argument is list of coordinates
# 2nd argument is colour of the line
mymap5.addpath(path, "# 00FF00")

mymap5.draw('pygmap5.html')


