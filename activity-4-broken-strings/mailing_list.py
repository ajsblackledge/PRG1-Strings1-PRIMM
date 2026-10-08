# This program prepares a mailing list. Three things about it are wrong.
# Nothing crashes.

CONTACTS = ["Ada Lovelace", "Grace Hopper", "Alan Turing"]


def as_heading(text):
    return text.upper()


def surname_first(full_name):
    parts = full_name.split(" ")
    forename = parts[0]
    surname = parts[1]
    initial = forename[0]
    return f"{surname}, {initial}."


def matches_search(full_name, search_term):
    return search_term.lower() in full_name.lower()


print(as_heading("mailing list"))

for contact in CONTACTS:
    print(surname_first(contact))

print(matches_search("Ada Lovelace", "ada"))
