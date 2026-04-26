import requests
import time
import random
import string
import re


class CakuAPI:
    def __init__(self):
        self.base_url = "https://caku.ai"
        self.mail_url = "https://api.mail.tm"
        self.session = requests.Session()
        self.session.headers.update({
            "accept": "*/*",
            "content-type": "application/json",
            "origin": "https://caku.ai",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        self.email = None
        self.password = None
        self.mail_token = None

    def _rand(self, n=10):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

    def _create_mail(self):
        headers = {"Content-Type": "application/json"}
        r = requests.get(f"{self.mail_url}/domains", headers=headers)
        domain = r.json()["hydra:member"][0]["domain"]
        self.email = f"{self._rand(12)}@{domain}"
        pwd = f"Pass{random.randint(1000,9999)}!"
        payload = {"address": self.email, "password": pwd}
        requests.post(f"{self.mail_url}/accounts", json=payload, headers=headers)
        r = requests.post(f"{self.mail_url}/token", json=payload, headers=headers)
        self.mail_token = r.json().get("token")
        return True

    def _get_verify_link(self, timeout=90):
        if not self.mail_token:
            return None
        headers = {"Authorization": f"Bearer {self.mail_token}"}
        start = time.time()
        while time.time() - start < timeout:
            r = requests.get(f"{self.mail_url}/messages", headers=headers)
            msgs = r.json().get("hydra:member", [])
            if msgs:
                r = requests.get(f"{self.mail_url}/messages/{msgs[0]['id']}", headers=headers)
                html = r.json().get("html", [])
                text = html[0] if isinstance(html, list) and html else r.json().get("text", "")
                m = re.search(r"token=([a-zA-Z0-9._-]{20,})", text)
                if m:
                    token = m.group(1).rstrip('"\'&;')
                    return f"{self.base_url}/api/auth/verify-email?token={token}&callbackURL=/dashboard"
            time.sleep(5)
        return None

    def register(self):
        self._create_mail()
        self.password = self._rand(12)
        print(f"Account: {self.email}")
        data = {
            "email": self.email,
            "password": self.password,
            "name": self._rand(10),
            "callbackURL": "/dashboard"
        }
        self.session.post(f"{self.base_url}/api/auth/sign-up/email", json=data)
        link = self._get_verify_link()
        if link:
            self.session.get(link, allow_redirects=True)
            return True
        return False

    def generate(self, prompt, image_url, model="nano-banana"):
        boundary = self._rand(16)
        form = (
            f"------{boundary}\r\n"
            f'Content-Disposition: form-data; name="prompt"\r\n\r\n{prompt}\r\n'
            f"------{boundary}\r\n"
            f'Content-Disposition: form-data; name="addWatermark"\r\n\r\ntrue\r\n'
            f"------{boundary}\r\n"
            f'Content-Disposition: form-data; name="model"\r\n\r\n{model}\r\n'
            f"------{boundary}\r\n"
            f'Content-Disposition: form-data; name="inputMode"\r\n\r\nurl\r\n'
            f"------{boundary}\r\n"
            f'Content-Disposition: form-data; name="imageUrls"\r\n\r\n["{image_url}"]\r\n'
            f"------{boundary}--\r\n"
        )
        headers = self.session.headers.copy()
        headers["content-type"] = f"multipart/form-data; boundary=----{boundary}"
        r = self.session.post(f"{self.base_url}/api/image/generate", data=form.encode(), headers=headers)
        task_id = r.json().get("taskId")
        print(f"Task: {task_id}")
        return self._wait(task_id)

    def _wait(self, task_id, timeout=90):
        start = time.time()
        while time.time() - start < timeout:
            r = self.session.get(f"{self.base_url}/api/image/status/{task_id}")
            d = r.json()
            status = d.get("status")
            if status == 1:
                return d.get("outputImage")
            elif status == -1:
                return None
            time.sleep(3)
        return None


def main():
    api = CakuAPI()

    PROMPT_TEXT = "make her hair a pink "
    IMAGE_URL = "https://files.catbox.moe/gomz5d.jpg"

    api.register()
    url = api.generate(PROMPT_TEXT, IMAGE_URL)

    if url:
        print(f"Done: {url}")
#py:@YAALI_515 IN TELEGRAM

if __name__ == "__main__":
    main()
