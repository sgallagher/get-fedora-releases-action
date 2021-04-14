#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get('https://bodhi.fedoraproject.org/releases?state=current')
r.raise_for_status()

stable = set()
for release in r.json()['releases']:
    if release['id_prefix'] == "FEDORA":
        stable.add(release['version'])

print("::set-output name=stable::{}".format(list(stable)))

r = requests.get('https://bodhi.fedoraproject.org/releases?state=pending')
r.raise_for_status()

devel = set()
for release in r.json()['releases']:
    if release['id_prefix'] == "FEDORA" and release['version'] != "eln":
        devel.add(release['version'])

print("::set-output name=development::{}".format(list(devel)))
print("::set-output name=active::{}".format(list(devel.union(stable))))