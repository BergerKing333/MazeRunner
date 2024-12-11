# MazeRunner
Simple Pygame program, demonstrating various path planning algorithms
This project was originally intended as a very simple maze generator / solver that allowed the user to interface by click the mouse. 
These features still exist but are now contained inside the No-Costmap-Search branch on the repo. 
The Main Branch has now been repurposed for my CSCI 4511W Final Project: Cost Map Based Search Algorithms. 

# How To Use
To use this repo, clone it locally and cd into the repo. Ensure that all dependencies are installed, including Numpy, MatPlotLib, PyGame, and the Python Noise library. 
If any of these are not installed, install them with ```pip install <package name>```

There are a couple of ways to run this code; 
### Interactive Mode:
To run this code in the interactive mode, with a GUI and with the ability to click to set start/end positions, run ```python3 .\main.py```. This will open a PyGame window that shows a gray scale cost map. From there, left click anywhere in the grid to set a start position, and right click to set an end position. After doing this, the algorithm will start, and after some computation, will draw a bright blue line indicating the generated path.

To swap the type of agent being used, change the pathType variable on line 38. Acceptable options for this variable are: ["basicAddition", "noCostImplementation", "multiplication", "exponent"]. This string must be set manually in the code to change the type of agent being used. 

As a note, the GUI for this was developed with the intention that it would be used for the simpler maze solver, and is poorly optimized for rendering the ~2 million perlin noise squares every frame. Things run slowly when the user interface is enabled. This is not the intended use case so these issues haven't been addressed.

### Test Running
To run all of the tests that were used as experimental data in the final paper, run ```python3 .\runTests.py```. Running this will test all 4 A* variants across the same randomized maps, recording all of the necessary data. This data will be printed to the terminal in a semi-readable manner, and published to the 'data.csv' file locally, which can then be used to generate graphs.

### Graph Generation
To generate the graphs that I used in my Final Paper, ensure that the data.csv file has been populated with the correct information-- this will be done automatically after running runTests.py, but if you didn't run that file first, this won't work.
Simply running ```python3 .\drawData.py``` in the terminal will start this script, generating and then showing each of the 6 charts included in my Final Paper. They open one at a time, and to get to the next one you'll have to close the current one. These graphs can be saved to images with the image saver built into MatPlotLib.
