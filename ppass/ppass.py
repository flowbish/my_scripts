#!/usr/bin/env python

from optparse import OptionParser
import sys,os,re

def main():
    parser = OptionParser(usage="usage: %prog [options] command",
                          version="%prog 0.1")
    parser.add_option("-u","--user",
                      action="store",
                      dest="username",
                      help="Username to add or search for")

    parser.add_option("-l","--location",
                      action="store",
                      dest="location",
                      help="Location to add or search for")
    
    parser.add_option("-p","--password",
                      action="store",
                      dest="password",
                      help="Location to add or search for")

    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("wrong number of arguments")

    print options

    if args[0] == "add":
        add_user(username=options.username,
                 location=options.location,
                 password=options.password)

def add_user(username, location, password):
    if not username:
        username=raw_input("username: ")
    if not location:
        location=raw_input("location: ")
    if not password:
        password=raw_input("password: ")
    #add (username,location,password) to database
    print username+(":"+password,"")[password==""]+("@","")[username==""]+location

if __name__ == "__main__":
    main()
