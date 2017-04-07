Li'l Configure
==============

A program that generates a ``./configure`` script that generates a
``./config.status`` script that generates a ``Makefile`` along with any
other configurable files.

It'll probably read a yaml file, but I'm nowhere near ready to start
thinking about that part yet.

Seems pretty... recursive?
--------------------------

Yeah. Here's how I think about it:

#.  I'm writing an **application.**
#.  The application will read a **config file.**
#.  The application will generate the ``./configure`` script based on
    what it finds in the config file.
#.  ``./configure`` will read command-line arguments and will create a
    custom ``./config.status`` file.
#.  While ``./config.status`` will be a script, it will be a very simple
    one that does little more than run some static ``cat <<\EOF`` calls
    (to a ``Makefile`` at the very least).

So the ``./configure`` shell script may need to be complicated, but it
won't need to generate anything dynamic in ``./config.status``.

And, honestly, automating the generation of ``./configure`` is easier
than writing it from scratch, since complicated shell scripts can
necessitate a lot of repeating oneself. This way, I can minimize
repetition, and I can even automate the ordering of such as function
definitions.

GNU General Public License v3 (GPLv3)
-------------------------------------

This is a GPLv3 project. If you don't know what it means, it means that
you can copy, distribute, and modify anything and everything here, but
you have to preserve headers and licensing. Pretty standard stuff.

What sets this license apart from others is that, if your project
includes any of my code, then your project must in turn be released
under the GPLv3.

For more information, see COPYING_.

.. _COPYING: COPYING
