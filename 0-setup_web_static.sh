#!/bin/bash
# Update package lists and install Nginx
apt update && apt install -y nginx

# Create /data/ directory if it doesn't exist
if [ ! -d "/data" ]; then
  mkdir /data
fi

# Create subdirectories within /data/web_static/
directories=(
  "/data/web_static"
  "/data/web_static/releases"
  "/data/web_static/shared"
  "/data/web_static/releases/test"
)

for dir in "${directories[@]}"; do
  if [ ! -d "$dir" ]; then
    mkdir -p "$dir"
  fi
done

echo "Hello Test" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data

cat <<EOF | sudo tee "/etc/nginx/sites-available/default" > /dev/null
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  root /data/web_static/current/;
  index index.html index.htm;

  location /hbnb_static/ {
    alias /data/web_static/current/;
    autoindex off;
  }

  # ... other your existing server configuration
}
EOF

service nginx restart
