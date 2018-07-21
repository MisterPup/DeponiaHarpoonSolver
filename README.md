# Deponia Harpoon Puzzle Solver

This project solves the Harpoon puzzle from the first game of the Deponia series.

![Image of Harpoon Puzzle from Deponia](Deponia.PNG?raw=true "Harpoon Puzzle")

The grid is converted into a Cartesian coordinate plane.  
The starting point is (4, 1).  
The ending point is (1,3).

The lever can be used to move the harpoon on the plane.

Each point in the grid is adjacent only to other points by means of the lever.  
For example starting from (4, 1) you can go to (5, 3) by pushing the lever to the top right.  
The top right moves the harpoon by (+1, +2).  

We generate a directed graph by calculating each position that can be reached starting from a point in the grid.  
Each edge of the graph has a cost of 1.

We then use Dijkstra's algorithm to find the shortest path from (4, 1) to (1,3).

And then we go back playing :)
