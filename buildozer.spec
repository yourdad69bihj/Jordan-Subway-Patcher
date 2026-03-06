[app]

# (str) Title of your application
title = Jordan Patcher

# (str) Package name
package.name = jordanpatcher

# (str) Package domain (needed for android packaging)
package.domain = org.jordan

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# packagelist.include_patterns = 

# (list) Permissions
# THE MOST IMPORTANT PART: Requesting full storage access
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE, INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the hook list
android.skip_update_hooks = False

# (str) Icon of the application (Black outlined dog/key)
# icon.filename = %(source.dir)s/icon.png

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/presplash.png

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
