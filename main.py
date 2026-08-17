name: Build Android APK

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libffi-dev libssl-dev
        pip install --upgrade buildozer cython

    - name: Build APK with Buildozer
      run: |
        buildozer init
        buildozer -v android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v3
      with:
        name: slot-game-apk
        path: bin/*.apk
