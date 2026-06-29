Animated Pictures
=================

In OMORI, pictures get animated all the time for various cutscenes, such
as the White Space intro. The game will also store multiple pictures
together in one sheet, and yet be able to only use one frame of it. So
how does it do that?

The answer is that it uses scripts.

The first thing we need to do is to create the picture we want to
animate. Simply use the Show Picture command and preferably set the
opacity for the time being to 0. Also make sure to keep in mind the ID
you are using. The higher IDs will always display higher, and an ID of 1
displays below the characters.

Now we can begin to script.

Firstly we need to define to the game what the divisions are between
each frame, so we use this script:

this.setupPictureCustomFrames(id, width, height, hframes, vframes);

Now let’s break down what each of those are.

The id is simply the ID of the picture you’re applying the frames to.

The width and height are the pixel widths and heights of the ENTIRE
image, not just one frame.

The hframes and vframes are the amount of horizontal and vertical frames
in the image.

Now what we add after is dependent on what we’re doing.

If you’re just setting a single frame of an image, like say a lighting
overlay, use this;

this.setPictureFrameIndex(id, frameId);

Once again id is the picture ID, meanwhile frameId is the ID of the
frame. Frame IDs are ordered from left-to-right, top-to-bottom, starting
at 0. So the top left is 0 and then the one to the right is 1 and so on.

However if you’re setting an Animation, then use this instead;

this.setPictureAnimation(id, frames, delay, loops, wait);

Alright now let’s break this down again.

First up the id is the same as always, the Picture ID.

Next is the frames. This is an Array of the frameIds that you want the
animation to go through. For those who don’t know, an Array in
JavaScript is a list of values stored as a variable. They look like
this: [value,value,value,value] So if you want to have your frames go
from 0-6, then your frames will look like [0,1,2,3,4,5,6].

The delay is the number of frames (as in your monitor’s fps) that it
takes to update from one frame to another.

The loops determines how many times the animation should play before
being complete, if you want to set it to infinity, use 0.

Lastly, the wait is a true or false (otherwise known as a boolean) that
determines whether or not the game waits for the animation’s completion.

Now with the Move Picture command, you can fade in your animating
picture. And once you’re done with all your custom framed pictures, make
sure to include a this.removePictureCustomFrames();
