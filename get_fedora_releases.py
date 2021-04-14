#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get('https://bodhi.fedoraproject.org/releases?state=current')
r.raise_for_status()

releases = set()
for release in r.json()['releases']:
    if release['id_prefix'] == "FEDORA":
        releases.add(release['version'])

print("::set-output name=stable::{}".format(list(releases)))

r = requests.get('https://bodhi.fedoraproject.org/releases?state=pending')
r.raise_for_status()

releases = set()
for release in r.json()['releases']:
    if release['id_prefix'] == "FEDORA" and release['version'] != "eln":
        releases.add(release['version'])

print("::set-output name=development::{}".format(list(releases)))
