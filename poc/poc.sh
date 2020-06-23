tar -xvzf /opt/poc/geckodriver-v0.26.0-linux64.tar.gz 
chmod +x geckodriver 
cp geckodriver /usr/local/bin/ 
sleep 30
echo "start"

python3 /opt/poc/exp.py http://web

echo "poc ok"