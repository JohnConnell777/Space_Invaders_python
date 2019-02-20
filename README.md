# Space_Invaders_python
Project One, Space Invaders, due Wednesday, 20 Feb 2019 (by 1130)
In this assignment, you will create the Space Invaders game, based on the Alien Invasions! code from
Project One. The image resources you will need (ship, ship animation destruction, bunker, different
types of aliens, alien animation destruction, and ufo destruction) will all have to be created using an
Image editing tool such as Inkscape or Gimp. The audio resources you will need can be captured
using an audio editor such as Audacity from an online version of Space Invaders.
Classic Space Invaders has several differences from the Alien Invasions! Game. You will need to
complete the following:
1. You will need PyCharm, Pygame, and Python 3 installed on your computer.
2. Using classic Space Invaders as a guide, and using an Image editor such
as Inkscape or Gimp, create the four types of aliens shown above, the
traditional Space Invaders ship, and the bunkers to hide behind.
3. The aliens must include a simple, slow, two-state animation while they are
moving (it looks better if alternating aliens are synchronized). Aliens must have a different
image when they explode (could show a simple, fast animation as well).
4. A UFO should move across the screen at random intervals. It makes a continuous oscillating
sound as it moves. If it is destroyed, it shows its (random) value instead of an explosion.
CPSC 386 – project one – page 1 of 3
5. The ship must have a fast. animated explosion (8-12 frames) when it is destroyed. Be sure to
move the pixels of the exploding parts around from frame to frame. (Note: the ship we used in
Alien Invasions! Is not the same as that used in Classic Space Invaders.)
6. Create a start screen, that shows the name of the game (in white and green), the aliens and
their values, and the menus for Play Game and High Scores. The start screen should show at
the beginning of each game, including if you have just lost a game.
7. Add lasers to the aliens, so they can shoot back at the ship. Use a random number generator
and a timer (pygame.time.get_ticks()) so they don’t shoot too often.
8. Add bunkers to the game that the ship can hide behind. The bunker can be damaged by both
the ship’s and aliens’ lasers. Use a random number generator to set the bunker’s pixels to
transparent when a laser strikes a part of the bunker to avoid a bite-out-of-a-sandwich look.
Use the Python Imaging Library to set the pixels.
9. Push the contents of your project to a new GitHub repository using a git client (e.g., the git
command-line client, GitHub Desktop, or GitHub for Atom). Do not submit files using drag-anddrop onto the repository web page, and do not push this assignment to the same repository as
your previous homework assignments.
Submission
Turn in the code for this homework by uploading all of the Python source files you created, the images
directory, and the sounds directory to a single public repository on GitHub. While you may discuss this
homework assignment with other students. Work you submit must have been completed on your own.
To complete your submission, print the following sheet, fill out the spaces below, and submit it to the
professor in class by the deadline. Failure to follow the instructions exactly will incur a 10% penalty on
the grade for this assignment.
