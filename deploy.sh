#!/bin/bash

# YT Transcripter Deployment Script
# Usage: ./deploy.sh

set -e  # Exit on error

echo "Starting deployment..."

# Pull latest code from main branch
echo "Pulling latest code from main branch..."
git pull origin main

# Install/update dependencies
echo "Installing dependencies..."
venv/bin/pip install -r requirements.txt

# Restart the service
sudo systemctl restart yt-transcripter
echo "Restarted yt-transcripter"
