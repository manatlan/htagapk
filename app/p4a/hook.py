import os
import shutil
from pathlib import Path
from pythonforandroid.toolchain import ToolchainCL

def after_apk_build(toolchain: ToolchainCL):
    manifest_file = Path(toolchain._dist.dist_dir) / "src" / "main" / "AndroidManifest.xml"
    old_manifest = manifest_file.read_text(encoding="utf-8")
    new_manifest = old_manifest.replace(
        '<application android:label',
        '<application android:usesCleartextTraffic="true" android:label',
    )
    manifest_file.write_text(new_manifest, encoding="utf-8")
    if old_manifest != new_manifest:
        print("Set android:usesCleartextTraffic SUCCESSFULLY")
    else:
        print("Set android:usesCleartextTraffic FAILED")