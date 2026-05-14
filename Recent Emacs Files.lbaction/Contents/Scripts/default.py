#!/usr/bin/env python3
# LaunchBar Action Script — Recent Emacs Files (recentf)

import json
import os
import re

RECENTF_PATH = os.path.expanduser("~/.cache/emacs/recentf.eld")
HOME = os.path.expanduser("~")


def parse_recentf(path):
    with open(path) as f:
        content = f.read()
    return re.findall(r'"(.+?)"', content)


def expand_path(p):
    return os.path.expanduser(p)


def file_visible(item_path):
    expanded = expand_path(item_path)
    if not expanded.startswith(HOME):
        return False
    return os.path.exists(expanded)


def create_main_item(item_path):
    expanded = expand_path(item_path)
    return dict(
        title=os.path.basename(expanded),
        subtitle=os.path.dirname(expanded),
        path=expanded,
    )


try:
    files = parse_recentf(RECENTF_PATH)
    items = [create_main_item(p) for p in files if file_visible(p)]
except Exception:
    items = []

print(json.dumps(items))
