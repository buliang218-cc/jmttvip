import os
import requests

APK_URL = "https://79a67.jtalvee.xyz/chan/jm0484/zAGk"  # 假设这个为最新 APK 下载地址
APK_FILE = "jmcomic_latest.apk"
VERSION_FILE = "APK_VERSION.txt"

def get_remote_version():
    # 模拟：请求头部查看是否有版本信息（例如自定义 header 或重定向）
    response = requests.head(APK_URL, allow_redirects=True)
    location = response.url
    version = location.split("/")[-1].replace(".apk", "")  # 从URL提取版本号
    return version

def get_local_version():
    if not os.path.exists(VERSION_FILE):
        return ""
    with open(VERSION_FILE, "r") as f:
        return f.read().strip()

def download_apk():
    with requests.get(APK_URL, stream=True) as r:
        r.raise_for_status()
        with open(APK_FILE, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def update_version_file(version):
    with open(VERSION_FILE, "w") as f:
        f.write(version)

def main():
    remote_version = get_remote_version()
    local_version = get_local_version()

    if remote_version != local_version:
        print(f"New version found: {remote_version}, downloading...")
        download_apk()
        update_version_file(remote_version)
    else:
        print("No update needed.")

if __name__ == "__main__":
    main()
