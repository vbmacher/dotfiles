#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script is a simple wrapper which prefixes each i3status line with custom
# information. It is a python reimplementation of:
# http://code.stapelberg.de/git/i3status/tree/contrib/wrapper.pl
#
# To use it, ensure your ~/.i3status.conf contains this line:
#     output_format = "i3bar"
# in the 'general' section.
# Then, in your ~/.i3/config, use:
#     status_command i3status | ~/i3status/contrib/wrapper.py
# In the 'bar' section.
#
# In its current version it will display the cpu frequency governor, but you
# are free to change it to display whatever you like, see the comment in the
# source code below.
#
# © 2012 Valentin Haenel <valentin.haenel@gmx.de>
#
# This program is free software. It comes without any warranty, to the extent
# permitted by applicable law. You can redistribute it and/or modify it under
# the terms of the Do What The Fuck You Want To Public License (WTFPL), Version
# 2, as published by Sam Hocevar. See http://sam.zoy.org/wtfpl/COPYING for more
# details.

import sys
import json
import subprocess
import random

def get_next_meeting():
    work = subprocess.check_output("gcalcli --nocolor --nostarted agenda | head -2 | tail -1", 
            shell=True).rstrip()

    attendees = subprocess.check_output("gcalcli --nocolor --nostarted --detail_attendees -w 200 agenda", shell=True).rstrip()
    attendees = attendees.split("\n")

    if (len(attendees) > 3):
      # 0th line is empty
      # 1st line is the meeting title
      # 2nd line is attendees "                     Attendees:"

      if (attendees[2] == "                     Attendees:"):
        attendees = attendees[3:]

        offset = 0
        while (len(attendees) > offset and "                       " in attendees[offset]):
          offset += 1

        attendees = attendees[0:offset]
        rooms = []
        for k,v in enumerate(attendees):
          if ("resource.calendar.google.com" in v and "Prague" in v):
            rooms.append(v.lstrip().split(":")[0].split("[")[0].rstrip().split("(")[0].rstrip())

        if (len(rooms) > 0):
          work = work + " (" + ','.join(str(e) for e in rooms) + ")"

    perso = subprocess.check_output("gcalcli --nocolor --nostarted --configFolder ~/.gcalcli-perso agenda | head -2 | tail -1", 
            shell=True).rstrip()

    return work + ' | ' + perso

def print_line(message):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def read_line():
    """ Interrupted respecting reader for stdin. """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    # Skip the first line which contains the version header.
#    print_line(read_line())

    # The second line contains the start of the infinite array.
#    print_line(read_line())

#    while True:
#        line, prefix = read_line(), ''
        # ignore comma at start of lines
#        if line.startswith(','):
#            line, prefix = line[1:], ','

#        j = json.loads(line)
        # insert information into the start of the json, but could be anywhere
        # CHANGE THIS LINE TO INSERT SOMETHING ELSE
        #j.insert(0, {'full_text' : '%s' % get_governor(), 'name' : 'gov'})

        # and echo back new encoded json
#        print_line(prefix+json.dumps(j))
  print_line("{\"full_text\" : \"%s\"" % get_next_meeting() + ",\"short_text\" : \"agenda\"}")
