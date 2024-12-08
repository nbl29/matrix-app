[app]

# (str) Title of your application
title = Matrix App

# (str) Package name
package.name = matrixapp

# (str) Package domain (needed for android/ios packaging)
package.domain = com.matrixapp

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,requests,python-socketio

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (str) Application icon
icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (bool) Enable Android auto backup feature (Android API >=23)
android.allow_backup = True

# (list) Android permissions required by the app (for example INTERNET, ACCESS_FINE_LOCATION)
android.permissions = android.permission.INTERNET

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) Skip byte compile for .py files
android.no-byte-compile-python = False

# (str) The format used to package the app for release mode (aab or apk or aar).
android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
# ios.kivy_ios_url = https://github.com/kivy/kivy-ios
# ios.kivy_ios_branch = master

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
bin_dir = ./bin