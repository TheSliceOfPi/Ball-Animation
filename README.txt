Edith Flores
Ball Animation


The Ball class module contains a constructor method, three mutator methods, and two normal methods, and two child classes.
The constructor method contains nine instance variables: x (x positions), y (y position), xVel (velocity on x) ,yVel (velocity on y), size ( size of the ball object), rColor(red component of the Ball), gColor( green component of the Ball), bColor(blue component of the Ball), and bTurtle (Turtle that represents the Ball). 
The constructor method then shapes the Turtle into a circle and calls the setSize, setColor, and setPos methods.
The three mutator methods are setPos, setColor, and setSize that sets the position the Ball should be on the window, sets what color the Ball should be, and sets the size the Ball should, respectively. 
The two normal methods are update and move which updates the state of the Ball and makes sure the Ball stays within limits, and moves the Ball based on the position and velocity the Ball has. 
The two child classes are BreathingBall and WarpBall. BreathingBall inherits all of the Ball class methods and instance variables but overrides the update method so the BreathingBall object gets bigger and smaller. 
The WarpBall inherits all of the Ball class methods and instance variables but overrides the update method so that the WarpBall does not bounce off the “walls” (stay within limits) but “warps” around the window to the opposite side. 
The ballworld module acts as a driver module that creates a window and creates Ball, BreathingBall, and WarpBall objects to be displayed on the screen. 
In other words, the ballworld module tests out the methods of the Ball class. 



#Run: python3 ballworld.py 
