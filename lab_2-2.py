# Author: JAP (AMDG) 12/4/20

def invite(guest):
    for x in guest:
        print("Hi {0} You're invite to my party on Friday!".format(x))


def party_invites(lst):
    for name in lst:
        print("Hi {0} You're invite to my party on Friday!".format(name))


party_invites(["Sean", "Josh", "Manny"])
# party_invites(input(["Please put who you would want to invite, seprate with comma!"]))
