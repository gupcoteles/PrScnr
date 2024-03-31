# Port Scanner

a simple port scanning tool

# Installation

```
python3 -m pip install -r requirements.txt
```

# Usage

```
python3 "port scanner.py" -h
```

This will display help for the tool. Here are all the switches it supports.

```
Usage:
     python3 PrScnr.py [Flags]
Flags:
     -t, --target     Use to specify the target IP
     -ft, --firstport Use to specify the start port
     -lp, --lastport  use to specify the end port
Example:
     python3 PrScnr.py -t <IP address> -ft <start port> -lp <end port>
     python3 PrScnr.py --target <IP address> --firstport <start port> --lastport <end port>
```
