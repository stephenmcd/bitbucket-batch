#!/usr/bin/env python

import sys
import urllib2
from cookielib import CookieJar
from getpass import getpass
from urllib import urlencode

__version__ = "0.1.0"
LOGIN_URL = "http://bitbucket.org/account/signin/"
ADMIN_URL = "http://bitbucket.org/%s/admin"
OPS = ("add", "remove")
ROLES = ("reader", "writer", "admin")

def main():

    # Get args.
    args = sys.argv[1:]
    if len(args) != 4 or args[1] not in OPS or args[2] not in ROLES:
        usage = "usage: %s repo_owner %s %s user"
        print usage % (__file__, "|".join(OPS), "|".join(ROLES))
        sys.exit()
    credentials = {"username": args[0], 
        "password": getpass("Password for %s:" % args[0])}
    action = {"username": args[3], "op": args[1].title() + " " + args[2]}

    # Set up cookies and headers.
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()))
    opener.addheaders = [("X-Requested-With", "XMLHttpRequest")]
    urllib2.install_opener(opener)

    # Log in and loop through repos, applying action.
    all_html = urllib2.urlopen(LOGIN_URL, urlencode(credentials)).read()
    try:
        repos_html = all_html.split("repository-list")[1].split("</table>")[0]
    except IndexError:
        print "Could not access repos, most likely invalid username/password."
        sys.exit()
    for line in repos_html.split("\n"):
        if "href" in line:
            repo = line.split("href=")[1].split(">")[0].strip('"').strip("/")
            print "Updating %s" % repo
            urllib2.urlopen(ADMIN_URL % repo, urlencode(action))

if __name__ == "__main__":
    main()
