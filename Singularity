#Export http_proxy=http://
#Bootstrap: shub
Bootstrap: docker
#From: singularityhub/ubuntu
From: ubuntu:18.04

%environment
   TMPDIR=/tmp/

%post
    apt-get update && apt-get -y install xkb-data x11-apps bzip2 qt5-default mesa-utils libgl1-mesa-dev libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 iproute2 libgtk2.0-0 evince
