[app]
title = Matrix App
package.name = matrixapp
package.domain = com.matrixapp
source.dir = .
source.include_exts = py,png,jpg,kv
version = 0.1
requirements = python3,kivy,numpy
orientation = portrait
fullscreen = 0
android.api = 31
android.minapi = 21
android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
android.release_artifact = aab
android.debug_artifact = apk

[buildozer]
log_level = 2
