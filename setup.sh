#!/bin/bash

# Deployment Script for FRC Object Detection on Jetson Orin Nano

APP_DIR="/home/photonorin/FRC-Game-Piece-Pos-Estimation"
SERVICE_NAME="frc-object-detection.service"

echo "Starting deployment..."

# 1. Create directory if it doesn't exist
mkdir -p "$APP_DIR"
mkdir -p "$APP_DIR/RaspberryPiCode"
mkdir -p "$APP_DIR/Data"

# 2. Copy files (Assumes this script is run from the directory containing the package files)
# Check if files exist in current directory before moving
if [ -f "best 1.pt" ]; then
    cp "best 1.pt" "$APP_DIR/"
fi
if [ -f "requirements.txt" ]; then
    cp "requirements.txt" "$APP_DIR/"
fi
if [ -d "RaspberryPiCode" ]; then
    cp -r RaspberryPiCode/* "$APP_DIR/RaspberryPiCode/"
fi
if [ -d "Data" ]; then
    cp -r Data/* "$APP_DIR/Data/"
fi

# 3. Install dependencies
echo "Installing dependencies..."
# It is recommended to use a venv, but for service simplicity user might prefer system or user install.
# 'ultralytics' can be heavy.
pip3 install -r "$APP_DIR/requirements.txt"

# 4. Install and enable Service
echo "Installing systemd service..."
sudo cp "$SERVICE_NAME" /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable "$SERVICE_NAME"
sudo systemctl restart "$SERVICE_NAME"

echo "Deployment complete."
echo "Check status with: systemctl status $SERVICE_NAME"
echo "View logs with: journalctl -u $SERVICE_NAME -f"
