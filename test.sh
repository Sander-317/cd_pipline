cd /home/cd_pipline
git pull origin main
pip install -r requirements.txt
pkill gunicorn
gunicorn main:app --bind 0.0.0.0