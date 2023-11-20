cd /home/cd_pipline
git pull origin main
pip install -r requirements.txt
systemctl restart farm.service
systemctl status farm.service
