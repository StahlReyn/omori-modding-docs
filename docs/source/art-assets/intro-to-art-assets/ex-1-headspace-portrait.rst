Ex 1: Headspace Portrait
========================

Intro
-----

For this we’ll be attempting to recreate Basil’s portrait as close to
the original as possible.

This example is done in **Clip Studio Paint**. Though this is also
possible on Krita and Photoshop as they support all features required.

.. container::

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   Original Basil Portrait

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>

Layout
~~~~~~

Here is a quick rundown on general step layout.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Layer layout in Clip Studio Paint

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

Line Art
--------

For this example, the image is drawn at **512x512**, far larger than
game sprite of 106x106. This is so the specific brush detail will be
“averaged out” later when sized smaller, and allow for more leeway of
wobbliness.

Line width is estimated by just sizing the original to also 512x512 and
comparing line brush.

Since the goal here is just to recreate for demonstration, the line art
will be traced over.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Basil portrait line art recreation

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

Brush and Texture
~~~~~~~~~~~~~~~~~

**Brush** used in example is `Pencil R on Clip
Studio <https://assets.clip-studio.com/en-us/detail?id=1702962>`__. At
around 6px size.

**Texture** used is **Impasto**, a default texture on Clip Studio.
Resized slightly smaller at 8% opacity.

Line Coloring
-------------

For coloring, **tone curve** will be used as it’s simple but still gives
enough control over specific values. 

Taking a look at original sprite, notice that the darkest value remains
black, changing to blue. With the lighter area being more
purple/magenta.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Basil with headspace coloring

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

Tone Curve Settings
~~~~~~~~~~~~~~~~~~~

Tone curve here is done in **Clip Studio Paint**. Here are settings
used.

More info can be found `here on Tonal Correction
Effects <https://help.clip-studio.com/en-us/manual_en/390_filters/Tonal_Correction_Effects.htm#1364001>`__.

{% tabs %} {% tab title=“RGB” %} **RGB** Channel can be thought of in
this case as brightness value. Being 0 = Black to 255 = White.

For this, dark value is made **darker** to make the black values pop
through the other colors and help increase **contrast**. This is shown
as curve pushed down on left to middle.

The bright value is made slightly **brighter** to increase contrast and
reduce the back texture of the paper a little. Not too much, as paper
texture is still wanted. This is shown as curved pushed up a little on
right side.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

{% endtab %}

{% tab title=“Red” %} In this case, the **red** curve is pushed down on
the left, making darker value more **cyan**, with it being opposite of
red on light color wheel.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Red Channel

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

{% endtab %}

{% tab title=“Blue” %} The **blue** channel is heavily pushed up to give
a strong blue color on line art. The point still pass at 0,0 as we still
want dark **black** values to be retained.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Blue Channel

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

{% endtab %}

{% tab title=“Green” %} In this case, the **green** curve is pushed down
on the left, making darker value more **magenta**, with it being
opposite of red on light color wheel. 

The push happens more on the right side, being lighter values. This is
done as we have already established that we want lighter color like the
skin to be magenta colored.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Green Channel

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

{% endtab %} {% endtabs %}

Cropping
--------

This can be done quickly with **masking** at the end product, **magic
wand** or **fill tool** with transparent value both works.

.. container::

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   Basil now cropped

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   Layout shown. The masking layer is done on the folder for ease.

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>

{% hint style=“info” %} Sometimes there may be issue with selection
fill, it may be good idea to increase contrast or remove the texture
layer temporarily first.

If done grouped in a folder, make sure it is set to **Normal** blending
mode. {% endhint %}

Chromatic Aberration (Optional)
-------------------------------

Curiously, in Basil’s portrait sprite and some other headspace sprites
there seems to be slight amount of chromatic aberration. In this case
can be seen by slight magenta shade above lines and cyan shade below.

Chromatic aberration gives the sprite a slight more pop with more color
variance, though might be annoying to work with.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Zoomed in original sprite, notice the cyan below lines and magenta above

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

Chromatic aberration can be quite differing in method in different art
program, so it may be better to research about it in your own program
case rather than explained here.

In this example, the red channel is offset by 2 pixels upward.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Chromatic Aberration applied, 2 pixels vertical difference in red and
blue channel

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

Resizing
--------

Now that the sprite is done, it is time to resize back to the game file
size of 106x106. The **interpolation method** used here is **average
colors** to give it a smooth look and accurate coloring.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Sprite now resized to 106x106

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

{% hint style=“info” %} From this point on it might be good idea to do
the steps in mass after making multiple sprites already, to avoid taking
time to individually resize everytime. {% endhint %}

Sharpen
-------

Take a look at original sprite, you may notice how portraits tends to
have strange white border around the lines. This is a result from
sharpen effect.

Sharpen is used to make the image less blurry making lines more defined.
In this case the “blur” is due to resizing.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Unsharp tool applied on image

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

Final Result
------------

And it is finished! Here are comparison between original (left) and
recreation (right).

.. container::

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   Original

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   Recreation

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>

[Tip] Separating Head and Face
------------------------------

To save time on making multiple face, a faceless head template could be
made, and have the face variants be added on top later.

Older Omori sprites are all redrawn entirely for every frame, but for
more newer sprites, like Basil’s battle portraits for console content,
the face are split.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Basil’s sprite in Nucleus Art Gallery

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>
