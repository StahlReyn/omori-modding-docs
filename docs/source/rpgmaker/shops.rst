Shops
=====

Shops are strange little things, since they don’t really appear much.
Nonetheless, I’ll explain how to set them up.

First off, assuming you’re making a shop with new dialogue, you’ll have
to write all of that dialogue. This dialogue has to be placed in
System.yaml. The easiest way to do this is just copy paste one of the
pre-existing dealers and just change their name and their dialogue.

Note: You’ll notice that most of the Faraway Town dealers call for other
yaml files. You should also do this.

Now we’re going to actually make our shop. First things first, make your
new event and add whatever beginning dialogue or other stuff you want.
Then, once you get to the point of buying or selling, make a dialogue
selection between Buying, Selling, and Cancel. You can refer to the
above sections on how to do that. 

Now, in the Buying section, we’re going to use a Script Command, that
being “this.setupShop(‘name’, 0)” What this does is it tells the game
what dialogue it should be showing, which is done through the ‘name’,
which should be the name you gave your dealer in the System.yaml file.
Then the 0 tells the game you are buying. Now just use the Shop
Processing Command to add all your items and set their prices. Make sure
to not tick the “Purchase Only” box. It doesn’t work in OMORI.

Then, for Selling, we’re going to do all of that the exact same, except
for one change. We’re going to replace the 0 with a 1, to tell the game
we are selling instead of buying. You’re still going to need the Shop
Processing by the way, even if it does nothing when selling, since it’s
what tells the game to actually pull up the shop menu.

Lastly for Cancel, you just end the event. Not much to say about it. 

| 
| Also if you want to add a portrait for your dealer, you’ll have to
  mess with plugins to do that.
  `Reverie <http://mods.one/mod/reverie>`__ does this, so you can look
  at that to figure out how it’s done if you so want. Honestly, though,
  it’s not super important, as only the Mailbox has a portrait in OMORI.
