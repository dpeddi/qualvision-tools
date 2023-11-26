Qualvision - tools
==================

L'avventura è iniziata dopo l'acquisto di un citofono Vimar - K40945/K40955.

Come si può vedere il citofono una volta collegato al wifi esporta un server http/https:

```
nmap 192.168.1.100
Starting Nmap 7.80 ( https://nmap.org ) at 2023-11-26 11:44 CET
Nmap scan report for 192.168.1.100
Host is up (0.029s latency).
Not shown: 998 closed ports
PORT    STATE SERVICE
80/tcp  open  http
443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 0.60 seconds
```

```
# telnet 192.168.1.100 80
Trying 192.168.1.100...
Connected to 192.168.1.100.
Escape character is '^]'.
get /
HTTP/1.1 400 Page not found
Server: Qualvision -HTTPServer
Date: Sun Nov 26 11:43:11 2023
Pragma: no-cache
Cache-Control: no-cache
Content-Type: text/html

<html><head><title>Document Error: Page not found</title></head>
                <body><h2>Access Error: Page not found</h2>
                <p>Bad request type</p></body></html>

Connection closed by foreign host.
```

L'OEM di questo prodotto è quindi QualVision.

Dopo qualche ricerca con google ho trovato alcuni siti che referenziano degli exploit su questo webserver (non ho testato se il citofono è vulnerabile)
https://github.com/fxdunt111ed/camFF/blob/9e16da07beb6df9f04d7335ffecd0a103ded4e6c/README.md
https://github.com/R3DRUN3/RedTeaming-Qualvision-HTTPServer-Exploit/blob/main/qualvision_httpserver_exploit.py

Il citofono si connette inoltre al cloud utilizzando il dns vimar.qvcloud.net

L'applicazione Vimar View Door è basata invece su QvHome.

Collegandosi su http://vimar.qvcloud.net si apre la medesima interfaccia di http://web.qvcloud.net (utilizzato da QvHome)

Da http://web.qvcloud.net si possono scaricare delle librerie che permettono di utilizzare i dispositivi di Qualvision da PC. Installando e analizzando in velocità questo "plugin" 
sembra che sfrutti diverse tecnologie cloud: tdkcloud, qvcloud e p2p/udp.

Decompilando sia l'app android che il plugin windows, non ci ho capito niente... sembrano scatole cinesi... troppi livelli di astrazione.

Però DeviceRequestHelp.java ha informazioni interessanti... sembrano esserci i vari comandi supportati dal web server esposto in lan dal citofono.

Ho provato a modificare uno dei due exploit e sono riuscito ad avere delle risposte da alcuni dei comandi:


"get.device.status"
```
<?xml version="1.0" encoding="UTF-8"?>
<envelope>
<body>
<error>0</error>
<content>
<info>
<version>V401R001B002</version>
</info>
<time>
<timezone>gmt+01:00</timezone>
</time>
<upgradestatus>5</upgradestatus>
<fps>20</fps>
</content>
</body>
</envelope>
```

