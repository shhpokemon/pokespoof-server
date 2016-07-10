#!/usr/bin/env python

import cgi
import cgitb
import sqlite3
cgitb.enable(display=0, logdir="/logs")



location = cgi.FieldStorage()

if "latitude" not in location or "longitude" not in location or "user" not in location:
    print "Status: 400"
    print
    print "Bad request"
else:
    conn = sqlite3.connect("locations.db")
    c = conn.cursor()

    c.execute("BEGIN TRANSACTION")
    c.execute("INSERT INTO 'Locations' VALUES(?,?,?)", location['user'].value,
                                                        float(location['latitude'].value),
                                                        float(location['longitude'].value))
    c.execute("COMMIT")

    print "Status: 200"
    print
