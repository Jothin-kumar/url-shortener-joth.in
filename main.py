from json import load, dump

chrs = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890-."
with open("data.json") as d:
    data = load(d)

def new_slug():
    from random import choice
    return choice(chrs) + choice(chrs)

def slug_exists(slug):
    for d in data:
        if d['slug'] == slug:
            return True

def validate_slug(slug):
    if len(slug) != 2:
        return False
    for c in slug:
        if c not in chrs:
            return False
    return not slug_exists(slug)

def generate_slug():
    while True:
        slug = new_slug()
        if not slug_exists(slug):
            return slug

def new_redirect(slug):
    url = input("Enter url (without https://) (Example: jothin.tech): ")
    from requests import get
    assert get(f"https://{url}").status_code == 200
    data.append({'slug': slug, 'url': url})

choice = input("Enter own slug? (Y/n): ").lower().strip()
if not choice:
    choice = "y"

if choice == "n":
    while True:
        slug = generate_slug()
        approved = input(f"Use {slug} as slug? (Y/n): ").lower().strip()
        if not approved:
            approved = "y"
        if approved == "y":
            new_redirect(slug)
            break
elif choice == "y":
    while True:
        slug = input("Enter slug: ")
        if validate_slug(slug):
            new_redirect(slug)
            break
        else:
            print("Invalid, Try Again")

with open("data.json", "w") as d:
    dump(data, d, indent=4)