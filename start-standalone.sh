#!/bin/bash
set -e

# Start Flask app in background
python /app/app.py &

# Wait a moment for Flask to start
sleep 2

# Start Caddy in foreground
exec caddy run --config /etc/caddy/Caddyfile --adapter caddyfile
