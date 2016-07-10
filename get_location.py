#!/usr/bin/env python

import cgi
import cgitb
import sqlite3
cgitb.enable(display=0, logdir="/logs")

query = cgi.FieldStorage()
if "user" not in query:
    print "Status: 400 Bad Request"
    print
    print "Must query user"
else:
    user = query["user"].value
    conn = sqlite3.connect("locations.db")
    c = conn.cursor()
    c.execute("SELECT * FROM 'Locations' WHERE Id=?", [user])
    l = c.fetchone()

    if l == None:
        print "Status: 404 User Not Found"
        print
        print "Please try a different user"
    else:
        print "Content-Type: text/html"
        print
        print "{'user':\'%s\', 'latitude':%f, 'longitude':%f}" % (l[0],l[1],l[2])
