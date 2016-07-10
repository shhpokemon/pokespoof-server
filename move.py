#!/usr/bin/env python

import sqlite3
import curses
import locale

locale.setlocale(locale.LC_ALL,"")

delta = .0001
user = ""
while user == "":
    user = raw_input("Username: ")

lat = raw_input("Latitude: ")
lon = raw_input("Longitude: ")

if(lat == ""):
    lat = 40.7327
else:
    lat = float(lat)

if(lon == ""):
    lon = -73.9883
else:
    lon = float(lon)

conn = sqlite3.connect("locations.db")
c = conn.cursor()

c.execute("SELECT EXISTS(SELECT 1 FROM Locations WHERE ID=?)", [user])
if(c.fetchone()[0] == 0):
    print "Adding user %s" % user
    c.execute("INSERT INTO Locations VALUES(?,?,?)", (user, lat, lon))
    conn.commit()

def main(stdscr, lat, lon, user):
    curses.curs_set(0)
    (cy, cx) = stdscr.getmaxyx()
    (cy, cx) = (cy/2, cx/2)

    while 1:
        i = stdscr.getch()
        if i == curses.KEY_UP:
            lat+=delta
            stdscr.addstr(cy, cx, unichr(0x25B2).encode("utf-8"))
        elif i == curses.KEY_DOWN:
            lat -= delta
            stdscr.addstr(cy,cx, unichr(0x25BC).encode("utf-8"))
        elif i == curses.KEY_LEFT:
            lon -= delta
            stdscr.addstr(cy,cx,unichr(0x25C0).encode("utf-8"))
        elif i==curses.KEY_RIGHT:
            lon += delta
            stdscr.addstr(cy,cx,unichr(0x25B6).encode("utf-8"))
        stdscr.refresh()

        c.execute("UPDATE Locations SET Latitude=?, Longitude=? WHERE Id=?", (lat,lon,user))
        conn.commit()

curses.wrapper(main, lat, lon, user)
