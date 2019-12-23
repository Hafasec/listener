A simple listener that can be used with conjunction with the [backdoor](https://github.com/Hafasec/manual_backdoor) published here previously.
Usage:
```
python listener.py -i [IP] -p [PORT]
```
or
```
python listener.py -ip [IP] -port [PORT]
```
ex.
```
python listener.py -i 192.168.1.10 -p 1234
[+] Listening for connections on port 1234
```
```
python listener.py -i 192.168.1.10 -p 1234
[+] Listening for connections on port 1234
[+] Received a connection from IP 192.168.1.10
```
