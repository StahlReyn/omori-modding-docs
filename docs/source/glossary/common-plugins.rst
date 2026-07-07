Common Plugins
==============

This is a list of common plugin or related terms that will be encountered.

.. glossary::

    Custom Battle Action Text (CBAT)
        A plugin called **Custom Battle Action Text.js** that manages text that
        displays for skills/item used

    Action Sequence
        Extension plugin for basic functions used for customized action
        sequences on a technical scale. Change switches, operate variables, add
        states, change damage rates, etc.

        .. seealso::

            For more information: `Action Sequence Pack 1 (YEP) - Yanfly.moe
            Wiki <http://www.yanfly.moe/wiki/Action_Sequence_Pack_1_(YEP)>`__



FPS Wait Optimization
---------------------

.. note::

    This changes the load delay and is not a speedup or an FPS boost.

OMORI utilizes a plugin that will make the game "pause" to give time for
engine to catch up when doing heavy loading. This makes the game run
smoother overall, but the current parameters for the plugin are
excessive and can be tweaked to remove artificial loading times.

First, go to the Plugin Manager in RPG Maker MV (the "puzzle" icon on
the top bar), then scroll down until you get to the WaitFPS plugin.

:samp:

Click on it to bring up its settings.

:samp:

You will want to change the numbers on the right until they match the
below screenshot.

:samp:

From there, click "OK" -> "Apply". There should be a decrease in loading
time during room transitions and when loading many objects at once.
