#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from fedora_distro_aliases import get_distro_aliases

output_file = os.getenv("GITHUB_OUTPUT")
if not output_file:
    raise ValueError("No output file available")

aliases = get_distro_aliases()

with open(output_file, "w") as f:

    stable_versions = sorted([ x.version for x in aliases["fedora-stable"]])
    print(f"stable={stable_versions}", file=f)

    devel_versions = sorted([ x.version for x in aliases["fedora-development"]])
    print(f"development={devel_versions}", file=f)

    all_versions = sorted([ x.version for x in aliases["fedora-all"]])
    print(f"active={all_versions}", file=f)
