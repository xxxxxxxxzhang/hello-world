tar -xvzf /opt/poc/geckodriver-v0.26.0-linux64.tar.gz 
chmod +x geckodriver 
cp geckodriver /usr/local/bin/ 
echo "start"
firefox --version
sleep 10
echo "http://192.168.56.107:8000:"
curl http://192.168.56.107:8000
echo "http://web:"
curl http://web
python3 /opt/poc/exp.py http://web

echo "poc ok"