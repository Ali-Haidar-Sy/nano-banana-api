<p align="center">
  <pre>
███╗   ██╗ █████╗ ███╗   ██╗ ██████╗     ██████╗  █████╗ ███╗   ██╗ █████╗ ███╗   ██╗ █████╗
████╗  ██║██╔══██╗████╗  ██║██╔═══██╗    ██╔══██╗██╔══██╗████╗  ██║██╔══██╗████╗  ██║██╔══██╗
██╔██╗ ██║███████║██╔██╗ ██║██║   ██║    ██████╔╝███████║██╔██╗ ██║███████║██╔██╗ ██║███████║
██║╚██╗██║██╔══██║██║╚██╗██║██║   ██║    ██╔══██╗██╔══██║██║╚██╗██║██╔══██║██║╚██╗██║██╔══██║
██║ ╚████║██║  ██║██║ ╚████║╚██████╔╝    ██████╔╝██║  ██║██║ ╚████║██║  ██║██║ ╚████║██║  ██║
╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
  </pre>
</p>

<h1 align="center">🍌 Nano Banana – Unofficial Python Client<br><sub>Unlock Caku.ai’s AI Image Generation</sub></h1>

<p align="center">
  <strong>Automated Sign‑up · Image‑to‑Image Generation · Real‑time Polling</strong><br>
  <em>Educational research tool – use responsibly</em>
</p>

<p align="center">
  <a href="https://github.com/Ali-Haidar-Sy/nano-banana-api/stargazers"><img src="https://img.shields.io/github/stars/Ali-Haidar-Sy/nano-banana-api?style=for-the-badge&color=yellow"></a>
  <a href="[https://github.com/Ali-Haidar-Sy/nano-banana-api/blob/main/LICENSE](https://github.com/Ali-Haidar-Sy/nano-banana-api/tree/main#)"><img src="https://img.shields.io/github/license/Ali-Haidar-Sy/nano-banana-api?style=for-the-badge&color=blue"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="https://t.me/P33_9"><img src="https://img.shields.io/badge/Telegram-@P33_9-2CA5E0?style=for-the-badge&logo=telegram"></a>
  <a href="https://www.instagram.com/_ungn"><img src="https://img.shields.io/badge/Instagram-@_ungn-E4405F?style=for-the-badge&logo=instagram"></a>
  <a href="https://github.com/Ali-Haidar-Sy"><img src="https://img.shields.io/badge/GitHub-Ali--Haidar--Sy-181717?style=for-the-badge&logo=github"></a>
</p>

---

## 🍌 What is Nano Banana?

**Nano Banana** is an unofficial Python client for [Caku.ai](https://caku.ai) – a third‑party platform that gives you access to the powerful **nano‑banana** image model (originally developed by Google / Gemini).  

With this tool you can:

*   ✅ **Auto‑register** a throw‑away Caku.ai account using a disposable email from [mail.tm](https://mail.tm)
*   ✅ **Submit an image‑to‑image generation request** (upload a photo and apply a prompt)
*   ✅ **Poll the task status** until the final output image URL is returned
*   ✅ **Save the result** or use it in your own pipeline – all programmatically

> ⚠️ **Educational purpose only.** Automating account creation may violate Caku.ai’s Terms of Service. Use this tool responsibly and never for abuse or spam.

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Ali-Haidar-Sy/nano-banana-api.git
cd nano-banana-api

# 2. Install dependencies (only requests is required)
pip install requests

# 3. Run the example
python NANOBANANAAPI.py
The script will:

Generate a random email address

Register a new Caku.ai account

Wait for the verification email and confirm it automatically

Send an image‑generation task ("make her hair a pink " applied to a sample image)

Print the final output image URL

🔧 Customisation
Edit the variables inside the main() function to fit your needs:

python
PROMPT_TEXT = "make her hair a pink "       # your natural language prompt
IMAGE_URL   = "https://files.catbox.moe/gomz5d.jpg"  # input image URL
MODEL_NAME  = "nano-banana"                 # you can change the model if needed
📁 Project Structure
text
nano-banana-api/
├── NANOBANANAAPI.py   # Main Python script
├── README.md
└── LICENSE
🧠 How It Works (API Flow)
Step	Method	Description
1. Create Mailbox	_create_mail()	Fetches a temporary domain from mail.tm, creates an inbox, and retrieves a bearer token.
2. Register Account	register()	Sends a sign‑up request to Caku.ai with the temporary email; extracts the verification link from the inbox and confirms the account.
3. Generate Image	generate()	Crafts a multipart/form-data request containing the prompt, the input image URL, and the model name.
4. Poll Status	_wait()	Checks the task status every 3 seconds until the image is ready (status 1) or failed (-1).
📦 Dependencies
Python 3.7+

requests – pip install requests

No other external libraries are required.

⚠️ Ethical & Legal Notice
This tool interacts with Caku.ai’s internal API and automates account creation.

Do not use it for denial‑of‑service, spam, or any activity that violates Caku.ai’s Terms of Service.

Do not attempt to bypass rate limits or protections.

This project is provided “as is” for educational and research purposes only. The author assumes no liability for misuse.

🛡️ Disclaimer
text
This project is not affiliated with Caku.ai or Google.
All trademarks belong to their respective owners.
🤝 Contributing
Found a bug? Want to add more features (e.g., text‑to‑image, batch processing)?

Open an Issue to report problems

Submit a Pull Request with improvements

All constructive contributions are welcome!

📞 Connect With Me
Platform	Handle
GitHub	Ali-Haidar-Sy
Telegram	@P33_9
Instagram	@_ungn
<p align="center"> <strong>🍌 Banana power! If this tool helped you, please ⭐ star the repository!</strong> </p> ```
