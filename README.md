# PB-PyQuake3
**PyQuake3** Python module that can query and execute rcon commands on a Quake 3 server.

- [Gerald Kaszuba](http://geraldkaszuba.com/)
- [gak](https://github.com/gak) - [pyquake3](https://github.com/gak/pyquake3)
- [urthub](https://github.com/urthub) - [pyquake3](https://github.com/urthub/pyquake3)

# Example

    from pyquake3 import PyQuake3
    QUAKE = PyQuake3(server='localhost:27960', rcon_password='password')

    QUAKE.update()
    print "The server name of '%s' is %s, running map %s with %s player(s)." % (QUAKE.get_address(), QUAKE.values['sv_hostname'], QUAKE.values['mapname'], len(QUAKE.players))

    for gamer in QUAKE.players:
        print "%s with %s frags and a %s ms ping" % (gamer.name, gamer.frags, gamer.ping)

    QUAKE.rcon_update()
    for gamer in QUAKE.players:
        print "%s (%s) has IP address of %s" % (gamer.name, gamer.num, gamer.address)

    QUAKE.rcon('bigtext "pyquake3 is great"')