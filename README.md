A simple osint tool written in Python.


$> passive --help

OPTIONS:
-fn         Search with full-name
-ip         Search with ip address
-u          Search with username


$>  passive -fn "Jean Dupont"

First name: John
Name: Dupont
Address: 7 rue du Progrès
75016 Paris
Number: +33601010101


$>  passive -ip 127.0.0.1

ISP: FSociety, S.A.
City Lat/Lon:	(13.731) / (-1.1373)


$>  passive -u "Lucas02"

Facebook : yes
Twitter : yes
Linkedin : yes
Instagram : no
Skype : yes
