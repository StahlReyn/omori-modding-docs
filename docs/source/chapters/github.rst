GitHub
======

So. GitHub. What is it, exactly?

GitHub is a source control software and development platform that is
used for a variety of reasons. It has a lot of tools to make development
easier for programmers, it enables software developers to collaborate on
tools (such as RPGMaker MV) that don’t have built-in collaboration
features, and it saves your edit history— almost like snapshots— of your
code so that you can do things like trace bugs back to their sources.

Also, GitHub increases visibility into every aspect of what you’re
actually doing when you mod. You can literally see exactly what you
changed when you commit to a repository. This is called a diff.

Here’s an example of one:



.. image:: ../images/image220.png
   :align: center



(Source, parallels diff, courtesy of FruitDragon)

The red is the old change, the green is the new change.

I know I’m throwing a lot of new words out, so here’s a brief dictionary
for GitHub terms.

- Repository: Short form “repo”, it's a folder that basically acts like
  a project folder. It can be compared to a Google Drive folder.
- Local Repository: The repository where it is located on your computer.
- Source Control: Also known as version control, it’s a system or
  software used to track changes to files (such as code files) over
  time.
- Diff: Short for ‘difference’, it’s basically a summary or overview of
  the changes that have occurred to a file.
- Origin: The online copy of your repository hosted by GitHub.
- Commit: Saving your changes to the repository, essentially creating a
  snapshot of the changes at the time of committing.
- Push: Uploading your commits to the origin, so that they can be
  downloaded (or pulled) by other collaborators or devices.
- Pull: Downloading new commits from the origin, so that your local
  repository is updated to the most recent version.
- Main: The main branch of your repository.
- Branch: A controlled environment to test certain changes before
  committing to the main branch, where the majority of the code resides.
  Can also be used to save a previous version, especially if you have an
  old release you want to keep. (Such as a demo release.)



.. image:: ../images/image1.png
   :align: center



Here’s an example of the branches in the parallels repository.

And now here’s a handy link to a
\ `slideshow <https://www.google.com/url?q=https://docs.google.com/presentation/d/19Bi-uSRFUoT2zRqaMCeWgNKQf5VjvmUBXRWGg6CesrI/edit%23slide%3Did.g2dc6bc93425_4_1783&sa=D&source=editors&ust=1782966892275538&usg=AOvVaw3taLx3fEz8JrRFw9D1ZDkx>`__\  that
talks more about the terms I just defined.

(Note: GitHub isn’t the only type of source control software out there.
If you’d rather use something else, that’s up to you. OMORI itself was
made using DropBox as a source control software (somehow…?), which goes
to show that you could probably use just about anything. However, GitHub
is definitely one of the most versatile and powerful tools out there for
source control and collaboration, and a lot of OMORI modders use it.
Once you understand what to do, it’s also easy to use. So this tutorial
will be talking only about GitHub specifically.)

Now let’s get into how to use GitHub for OMORI modding.

.. _h.44ppgi9hcyvp:

Creation
--------

To start, we’re going to need a GitHub account.

Go to the \ `GitHub
website <https://www.google.com/url?q=https://github.com/&sa=D&source=editors&ust=1782966892276528&usg=AOvVaw1oB_kesom6Bt-P_xWdm_w_>`__\  and
create one. It’s free, and it’ll only take a few minutes. You don’t need
two-factor authentication, but feel free to add it to your account—
it’ll ensure that your repository is the most protected that it can be
from hackers.

Once you have an account, you’ll need to download \ `GitHub
Desktop <https://www.google.com/url?q=https://desktop.github.com/download/&sa=D&source=editors&ust=1782966892276877&usg=AOvVaw33zpyhufzrEcGF8RTUu9r0>`__\ .
Install it, then open it.

You’ll end up with a screen that looks something like this.



.. image:: ../images/image43.png
   :align: center



(source: zoewillowz)

Click “Sign in with GitHub.com” and log into your account. Make sure to
click “Authorize Desktop”. Return to GitHub Desktop.

Then you’ll get a screen that looks something like this.



.. image:: ../images/image26.png
   :align: center



(source: zoewillowz)

Here’s where we’ll have to make the repository or clone a repository
from the internet.

.. _h.m7k5oo19ojkl:

Making a new Repository
~~~~~~~~~~~~~~~~~~~~~~~

If you don’t already have a repository for your project folder, it’s
fairly straightforward to make one.

First, locate your playtest folder in your hard drive. I’ve named mine
“repo practice”.



.. image:: ../images/image261.png
   :align: center



Next, go to GitHub Desktop and select “Add an Existing Repository from
your local drive… ”



.. image:: ../images/image26.png
   :align: center



(source: zoewillowz)

Select your repository.

You’ll get the following alert:



.. image:: ../images/image247.png
   :align: center



Click “create a repository”.

You’ll get the following window. (Your filepath will be grayed out).
Fill it out. You don’t need to initialize a README, select a license, or
add a Git ignore.



.. image:: ../images/image50.png
   :align: center



Then click “Create repository”! After a while of loading, you’ll get the
following window.



.. image:: ../images/image216.png
   :align: center



Now all you need to do is publish this repository to GitHub, which
enables you to share it with others and back it up. To do that, simply
click the button at the top!

.. _h.3bcj251z8z1q:

Cloning a Repository
~~~~~~~~~~~~~~~~~~~~

If instead of making your own repository, you’re being added to someone
else’s repository, you’re going to need to clone a repository from the
internet.

If you’ve already been added to the repository (see the \ `Collaboration
section <#h.e8eze2higkg0>`__\  for how to do that) adding your new
repository should be a breeze.

On the GitHub Desktop main page, click “Clone a repository from the
Internet…”



.. image:: ../images/image182.png
   :align: center



The following window will pop up.



.. image:: ../images/image152.png
   :align: center



Select the repository that you want to clone from the list (if your
GitHub account is new, the list shouldn’t be that long haha), then set
your local path to wherever you want the folder to be and click “Clone.”



.. image:: ../images/image76.png
   :align: center



If, for some reason, the repository is not visible in the selection
window, open it in your browser and copy the link. The repository page
will look something like this:



.. image:: ../images/image30.png
   :align: center

  

Copy the link from the search bar.

In the repository selection window, click the “URL” tab. Then, paste in
the repository link and click “Clone”.



.. image:: ../images/image228.png
   :align: center



(Note: Putting the parallels repo link in your GitHub and trying to
clone it won’t work. Even by URL, GitHub checks to make sure that the
repository you’re trying to clone is one you have access to. You still
need to have it shared with you or accessible to you if you’re trying to
clone it by URL.)

Once you click “Clone”, it’ll redirect you to the following window.



.. image:: ../images/image9.png
   :align: center



(I didn’t clone the parallels repository because I already have it
downloaded to my computer.)

Ensure that you have a stable internet connection, because what this is
essentially doing is downloading the entire project from online, where
GitHub hosts it.

Wait for the entire repository to download. One it’s done, it’ll take
you to the following window:



.. image:: ../images/image178.png
   :align: center



And that’s it! This is the main window in GitHub Desktop, and you can
access your repository, commit, push, pull, and more from here.

But what do you do now? How do you use GitHub?

.. _h.bti29u1ruwzs:

Source Control
--------------

First, let’s practice pushing to our repository. I’m going to do
something simple: add a new image file to the img/characters folder.
Let’s see what that looks like in GitHub Desktop.



.. image:: ../images/image283.png
   :align: center



It shows me a preview of what I’ve added! This is super helpful when I’m
trying to see what I’ve added without having to navigate the folder.

GitHub does the same thing for most file types (pretty much all file
types you’ll work with in basic OMORI modding). In the sidebar, it shows
you what files you’ve added and their file paths, and once selected,
shows you a preview of what you’ve added into the repository.

The icon next to the filename indicates whether the file was created,
edited, or removed. A green plus sign indicates a file addition, yellow
dot indicates a change, and a red minus sign indicates a file removal.

When the file is a text-based file, such as a .js plugin file or a .yaml
dialogue file, individual line changes will display in the window.
Green-highlighted text or lines indicate add changes, and
red-highlighted text or lines indicate subtract changes.

When the file is an image-based file, such as a .png, you will get
several options for how to view the changes.



.. image:: ../images/image142.png
   :align: center



2-up will display the previous version and the current version
side-by-side.



.. image:: ../images/image67.png
   :align: center

  

Swipe will swipe through the change, as though you are dragging a
curtain over the previous version.



.. image:: ../images/image167.png
   :align: center



Onion Skin will give you a slider bar to show the change overlaid on top
of each other. This is especially helpful when the change is small, as
you can see it change by sliding the bar back and forth.

And finally, my favorite, the Difference tab.



.. image:: ../images/image292.png
   :align: center



This tab overlays one version on top of the other and sets the blend
mode to Difference, showing the exact pixel color change for each pixel.
It can lead to some very hilarious results!

.. _h.e8eze2higkg0:

Collaboration
-------------

Probably the number one reason OMORI modders use GitHub is for
collaboration. In mod projects that require more than one person, you
need a way to collaborate with the other members of the team.

.. _h.uo1es89od7de:

Personal Stories
----------------

To finish it off, I’m going to share some personal stories from OMORI
modders that have used GitHub, just to show how amazing a tool this is
to use. (That is, if the rest of this section hasn’t sold you on using
it, hopefully this section will.)

.. _h.eyo0h7t5nx1p:
