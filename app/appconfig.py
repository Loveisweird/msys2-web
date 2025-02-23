# Copyright 2016-2020 Christoph Reiter
# SPDX-License-Identifier: MIT

from typing import Optional


REPO_URL = "https://repo.msys2.org"
DOWNLOAD_URL = "https://mirror.msys2.org"
REPOSITORIES = [
    ("mingw32", "", REPO_URL + "/mingw/mingw32", DOWNLOAD_URL + "/mingw/mingw32", "https://github.com/msys2/MINGW-packages"),
    ("mingw64", "", REPO_URL + "/mingw/mingw64", DOWNLOAD_URL + "/mingw/mingw64", "https://github.com/msys2/MINGW-packages"),
    ("ucrt64", "", REPO_URL + "/mingw/ucrt64", DOWNLOAD_URL + "/mingw/ucrt64", "https://github.com/msys2/MINGW-packages"),
    ("clang64", "", REPO_URL + "/mingw/clang64", DOWNLOAD_URL + "/mingw/clang64", "https://github.com/msys2/MINGW-packages"),
    ("clang32", "", REPO_URL + "/mingw/clang32", DOWNLOAD_URL + "/mingw/clang32", "https://github.com/msys2/MINGW-packages"),
    ("clangarm64", "", REPO_URL + "/mingw/clangarm64", DOWNLOAD_URL + "/mingw/clangarm64", "https://github.com/msys2/MINGW-packages"),
    ("msys", "x86_64", REPO_URL + "/msys/x86_64", DOWNLOAD_URL + "/msys/x86_64", "https://github.com/msys2/MSYS2-packages"),
]
DEFAULT_REPO = "mingw64"

ARCH_REPO_URL = "https://mirror.f4st.host/archlinux"
ARCH_REPO_CONFIG = []
for repo in ["core", "extra", "community", "testing", "community-testing",
             "multilib"]:
    ARCH_REPO_CONFIG.append(
        (ARCH_REPO_URL + "/{0}/os/x86_64/{0}.db".format(repo), repo)
    )
AUR_METADATA_URL = "https://aur.archlinux.org/packages-meta-v1.json.gz"

SRCINFO_URLS = [
    "https://github.com/msys2/MINGW-packages/releases/download/srcinfo-cache/srcinfo.json.gz",
    "https://github.com/msys2/MSYS2-packages/releases/download/srcinfo-cache/srcinfo.json.gz",
]

EXTERNAL_MAPPING_URL = "https://raw.githubusercontent.com/msys2/msys2-web/main/arch-mapping.json"

CYGWIN_METADATA_URL = "https://ftp.acc.umu.se/mirror/cygwin/x86_64/setup.zst"

BUILD_STATUS_URL = "https://github.com/msys2/msys2-autobuild/releases/download/status/status.json"

# Update every 30 minutes by default, at max 2 times every 5 minutes if triggered
UPDATE_INTERVAL = 60 * 30
UPDATE_MIN_INTERVAL = 60 * 5
UPDATE_MIN_RATE = 2

REQUEST_TIMEOUT = 60
CACHE_DIR: Optional[str] = None
