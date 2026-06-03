[app]

# (str) Title of your application
title = Table Tennis Mobile

# (str) Package name
package.name = tabletennis

# (str) Package domain (needed for android packaging)
package.domain = org.ayomide

# (str) Source code directory where main.py resides
source.dir = .

# (list) Source files to include (let's grab all Python and KV files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Core modules required to execute the table tennis code
requirements = python3,kivy==2.3.1,pillow

# (str) Supported orientations (landscape is perfect for a wide ping pong table)
orientation = landscape

# (bool) Use fullscreen mode
fullscreen = 1

# =============================================================================
# Android specific configurations
# =============================================================================

# (int) Android API to use (Targeting modern Android)
android.api = 34

# (int) Minimum API required (Supports older devices back to Android 7.0)
android.minapi = 24

# (str) Android NDK version to use (Stable pairing for Kivy 2.3+)
android.ndk = 26b

# (bool) If True, then skip trying to update the Android sdk
# This prevents the workflow from breaking during background license checks
android.skip_update = False

# (bool) Accept SDK licenses automatically
android.accept_sdk_license = True

# (str) The Android architectural targets
android.archs = arm64-v8a, armeabi-v7a

# (list) Permissions
android.permissions = INTERNET

# =============================================================================
# Buildozer configurations
# =============================================================================

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug and stdout)
log_level = 2

# (int) Display warning if buildozer is run as root (1 = yes, 0 = no)
warn_on_root = 0
