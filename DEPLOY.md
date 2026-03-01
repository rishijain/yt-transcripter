# Deployment Guide

## Server Requirements

- Python 3.12
- `python3.12-venv` package

## First-Time Setup

```bash
# Install venv support if not already installed
apt install -y python3.12-venv

# Clone the repo
cd /root/projects
git clone <your-repo-url> yt-transcripter
cd yt-transcripter

# Create virtualenv and install dependencies
python3 -m venv venv
venv/bin/pip install -r requirements.txt

# Install and enable the systemd service
cp yt-transcripter.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable yt-transcripter
systemctl start yt-transcripter

# Verify it's running
systemctl status yt-transcripter
```

The app will be available at `http://<server-ip>:8001`.

## Subsequent Deploys

```bash
cd /root/projects/yt-transcripter
git pull
venv/bin/pip install -r requirements.txt  # only if dependencies changed
systemctl restart yt-transcripter
```
