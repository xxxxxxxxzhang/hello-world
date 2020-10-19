FROM php:7.2-fpm-alpine

RUN apk add --no-cache \
    nginx \
    supervisor

# Install dependencies
RUN set -ex; \
    \
    apk add --no-cache --virtual .build-deps \
        bzip2-dev \
        freetype-dev \
        libjpeg-turbo-dev \
        libpng-dev \
        libwebp-dev \
        libxpm-dev \
    ; \
    \
    docker-php-ext-configure gd --with-freetype-dir=/usr --with-jpeg-dir=/usr --with-webp-dir=/usr --with-png-dir=/usr --with-xpm-dir=/usr; \
    docker-php-ext-install bz2 gd mysqli opcache zip; \
    \
    runDeps="$( \
        scanelf --needed --nobanner --format '%n#p' --recursive /usr/local/lib/php/extensions \
            | tr ',' '\n' \
            | sort -u \
            | awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
    )"; \
    apk add --virtual .phpmyadmin-phpexts-rundeps $runDeps; \
    apk del .build-deps

# Copy configuration
COPY ./etc /etc/
# Copy main script
COPY ./run.sh /run.sh
RUN chmod u+rwx /run.sh

# Calculate download URL
ENV VERSION 4.8.1
ENV URL https://files.phpmyadmin.net/phpMyAdmin/${VERSION}/phpMyAdmin-${VERSION}-all-languages.tar.gz
LABEL version=$VERSION
COPY phpMyAdmin.tar.gz .

# Download tarball, verify it using gpg and extract
RUN  set -ex; \
     apk add --no-cache --virtual .fetch-deps \
        gnupg \
    ; \
    \
    export GNUPGHOME="$(mktemp -d)"; \
    export GPGKEY="3D06A59ECE730EB71B511C17CE752F178259BD92"; \
    ls;\
    tar xzf phpMyAdmin.tar.gz; \
    cd phpMyAdmin;\
    pwd;\   
    mv phpMyAdmin-$VERSION-all-languages /www; \
    rm -rf /www/setup/ /www/examples/ /www/test/ /www/po/ /www/composer.json /www/RELEASE-DATE-$VERSION; \
    sed -i "s@define('CONFIG_DIR'.*@define('CONFIG_DIR', '/etc/phpmyadmin/');@" /www/libraries/vendor_config.php; \
    chown -R root:nobody /www; \
    find /www -type d -exec chmod 750 {} \; ; \
    find /www -type f -exec chmod 640 {} \; ; \
    apk del .fetch-deps

# Add directory for sessions to allow session persistence
RUN mkdir /sessions \
    && mkdir -p /www/tmp \
    && chmod -R 777 /www/tmp
RUN echo "http://mirrors.aliyun.com/alpine/latest-stable/main/" > /etc/apk/repositories
RUN echo "http://mirrors.aliyun.com/alpine/latest-stable/community/" >> /etc/apk/repositories
 
# 同步时间
 
# 更新源、安装openssh 并修改配置文件和生成key 并且同步时间
RUN apk update && \
    apk add --no-cache openssh tzdata && \ 
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    sed -i "s/#PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \
       ssh-keygen -t dsa -P "" -f /etc/ssh/ssh_host_dsa_key && \
    ssh-keygen -t rsa -P "" -f /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -t ecdsa -P "" -f /etc/ssh/ssh_host_ecdsa_key && \
    ssh-keygen -t ed25519 -P "" -f /etc/ssh/ssh_host_ed25519_key && \
    echo "root:admin" | chpasswd
# We expose phpMyAdmin on port 80
EXPOSE 80
EXPOSE 22

ENTRYPOINT [ "/run.sh" ]
CMD ["phpmyadmin"]
