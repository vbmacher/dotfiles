#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import subprocess
import random


def get_jumpshot_agenda():
    work = subprocess.check_output("gcalcli --nocolor --configFolder ~/.gcalcli-js agenda --nostarted | head -2 | tail -1", 
            shell=True).rstrip()

    attendees = subprocess.check_output("gcalcli --nocolor --configFolder ~/.gcalcli-js agenda --nostarted --detail_attendees -w 200", shell=True).rstrip()
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
    return work

def get_personal_agenda():
    return subprocess.check_output("gcalcli --nocolor agenda --nostarted --nodeclined | head -2 | tail -1", 
            shell=True).rstrip()


def get_agenda():
    #return get_jumpshot_agenda() + ' | ' + get_personal_agenda()
    return get_personal_agenda()

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
  agenda = get_agenda().decode()
  print_line("{\"full_text\" : \"%s\"" % agenda + ",\"short_text\" : \"agenda\"}")

