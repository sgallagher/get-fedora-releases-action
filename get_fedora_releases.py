#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests

output_file = os.getenv("GITHUB_OUTPUT")
if not output_file:
    raise ValueError("No output file available")

with open(output_file, "w") as f:

    r = requests.get("https://bodhi.fedoraproject.org/releases?state=current")
    r.raise_for_status()

    stable = set()
    for release in r.json()["releases"]:
        if release["id_prefix"] == "FEDORA":
            stable.add(release["version"])

    print("stable={}".format(list(stable)), file=f)

    r = requests.get("https://bodhi.fedoraproject.org/releases?state=pending")
    r.raise_for_status()

    devel = set()
    for release in r.json()["releases"]:
        if release["id_prefix"] == "FEDORA" and release["version"] != "eln":
            devel.add(release["version"])

    print("development={}".format(list(devel)), file=f)
    print("active={}".format(list(devel.union(stable))), file=f)
