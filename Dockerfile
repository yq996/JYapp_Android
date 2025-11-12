FROM ubuntu:22.04

#设置工作目录
WORKDIR /app

# 设置环境变量
ENV DEBIAN_FRONTEND=noninteractive
ENV JAVA_HOME=/usr/lib/jvm/jdk-17.0.12+7
ENV ANDROID_SDK_ROOT=/opt/android-sdk
ENV PATH=$JAVA_HOME/bin:${ANDROID_SDK_ROOT}/cmdline-tools/latest/bin:${ANDROID_SDK_ROOT}/platform-tools:$PATH

# 换源 + 安装依赖（一次性安装，最后清理）
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    apt-get update && apt-get install -y \
    python3 python3-dev python3-pip \
    curl gnupg wget unzip git \
    && rm -rf /var/lib/apt/lists/*

# Python 依赖
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Node.js 22 + npm + 设置淘宝镜像
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs && \
    npm config set registry https://registry.npmmirror.com/ && \
    npm cache clean --force && \
    rm -rf /var/lib/apt/lists/*

# 安装 Appium v3.0.1 + 驱动
RUN npm install -g appium@3.0.1 && \
    appium driver install uiautomator2@5.0.0 && \
    appium driver install --source=npm appium-flutter-driver@3.0.0 && \
    npm cache clean --force

# 安装 JDK 17 (精简安装)
RUN curl -L https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.12+7/OpenJDK17U-jdk_x64_linux_hotspot_17.0.12_7.tar.gz -o /tmp/jdk17.tar.gz && \
    mkdir -p /usr/lib/jvm && \
    tar -xzf /tmp/jdk17.tar.gz -C /usr/lib/jvm && \
    rm /tmp/jdk17.tar.gz

# 安装 Android SDK (只装必要组件)
RUN mkdir -p ${ANDROID_SDK_ROOT}/cmdline-tools && \
    cd ${ANDROID_SDK_ROOT}/cmdline-tools && \
    wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip -O cmdline-tools.zip && \
    unzip cmdline-tools.zip -d latest_tmp && \
    mv latest_tmp/cmdline-tools latest && \
    rm -rf cmdline-tools.zip latest_tmp && \
    yes | ${ANDROID_SDK_ROOT}/cmdline-tools/latest/bin/sdkmanager --licenses && \
    ${ANDROID_SDK_ROOT}/cmdline-tools/latest/bin/sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2"

#代码
COPY . .
