============
User's guide
============

Pinder is a straightforward Python API to *script* Campfire_, the web 2.0 chat application kindly brought to us by the 37signals_ team.

Usage is all but rocket science so I'm gonna show you its full power in its simplicity.

If you want full details on what's going on through the wire make sure to checkout the official API documentation: <http://developer.37signals.com/campfire/>

Connect to the server
~~~~~~~~~~~~~~~~~~~~~

::
    >>> c = Campfire('SUBDOMAIN', 'SECRET_TOKEN')

Any need to explain? I don't think so. We shall move on.

Room tinkering
~~~~~~~~~~~~~~

::
    >>> print c.rooms() # the available rooms
    >>> room = c.room('ROOM_ID')
    >>> room2 = c.find_room_by_name('Room 1')

Only remember that *None* will be returned if you accidentally type in the wrong name. Ouch!

Let's see something about me::

    >>> print c.me() # who am I?
    {'user': {'admin': True,
          'created_at': '2000/01/01 09:34:18 +0000',
          'email_address': 'foo@bar.com',
          'id': 12345,
          'name': 'Foo Bar',
          'type': 'Member'}}

I shall speak to myself now::

    >>> room.join()
    >>> room.speak("I'm working hard to get you out of there. Keep strong!")
    I'm working hard to get you out of there. Keep strong!
    
Room eavesdropping!
~~~~~~~~~~~~~~~~~~~

You can peek inside the room reading the transcripts this way::

    >>> room.transcript(date.today())
    
A whole world will bestow before you.
    
Extra
~~~~~

You can lock yourself in the room if you really want to but it's sad so I won't mention how to that.

.. _Campfire: http://wwww.campfirenow.com/
.. _37signals: http://www.37signals.com/
.. _Tinder: http://rubyforge.org/projects/tinder
