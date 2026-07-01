Plot Armor
==========

*"Plot Armor" refers to the mechanic in OMORI where the titular
character "will not succumb" when taking fatal damage once.*

To add Plot Armor to characters other than OMORI you first have to find
the first entry in the troops tab. It is labeled ``DO NOT TOUCH`` but we
will touch it anyways. Add the following event blocks in the 7th page
(it has the condition "Turn 0".

Here, ``Player`` is standing in for the actor of your choice.

Then, create a new page with the condition being that the actor you want
to add Plot Armor to reaches 0 HP. Add the following to that page:

In this example image, the actor ID is 8.

If you want to add the "OMORI did not succumb" dialog, create another
new page like this:

|image1|

Find page 5 and add the event blocks shown below,

|image2|

In this example, "NATHAN" is the new actor.

Next, download the plugin below and add it to your playtest folder or
mod:

https://www.dropbox.com/s/9s9ys8vlrgcrg6a/NEB_PlotArmorFix.js?dl=0

There are instructions commented in to walk you through the remainder of
the process. For the most part you will be replacing the number it asks
you to with your own actor's ID.

Now your actor should be able to "not succumb" just like OMORI can!

.. |image1| image:: https://lh5.googleusercontent.com/xuHE4WxZ3ETFLICpRYTtMVJwJWW3XqUdxrPnDCwtlPEegRxgd3-TCkWPaPlYyomzppG49Urh6Ls5CBq4H9GFCQTkmKi6Sq1x3Fgwon6dlgBh2WQK5f9EvGqUYhOIHpZeS4JiWHWimRZ0GZIAGv5l77k
.. |image2| image:: https://lh6.googleusercontent.com/kaGeO8FZND-ms9jr8yRv7APD-vMkeYsEMa58Y3aBp1NXsMzUFgjoiA1QlEpf8wCLp9UIiq0jYaBfDG2UwyiHvcOPrreCEfMFPYEH1nB2XtSNnAlNapl3kCThPJyyNCB02j-cxii-4Yvc4JnHI4-bWrs
