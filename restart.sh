#!/bin/sh

echo "Restarting server....."
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
echo "Done"
