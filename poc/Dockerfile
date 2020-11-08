FROM ubuntu:18.04

#COPY ./poc/ /opt/poc/
COPY requirements_poc.txt /opt/poc/requirements_poc.txt
RUN sed -i s@/archive.ubuntu.com/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update --fix-missing && apt-get install -y\
  curl \
  python3 \
  python3-pip \
  libgtk-3-0 gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1   libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation  libappindicator1 libnss3 lsb-release xdg-utils wget
ADD firefox-81.0.2.tar.bz2 /opt/poc/firefox-81.0.2.tar.bz2  
RUN pip3 install -r /opt/poc/requirements_poc.txt
CMD bash /opt/poc/poc.sh