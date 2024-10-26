# PrScnr

A simple port scanning tool.

# Installation

```
python -m pip install -r requirements.txt
```


>[!NOTE]
>You Should have installed python.

>[!TIP]
>You can install python from <a href="https://www.python.org/downloads/" target="_blank">here</a>.


# Usage

```
python PrScnr.py -h
```

This will display help for the tool. Here are all the switches it supports.

```
Usage:
     python PrScnr.py [Flags]
Flags:
     -t, --target     Use to specify the target IP
     -ft, --firstport Use to specify the start port
     -lp, --lastport  use to specify the end port
Example:
     python PrScnr.py -t <IP address> -ft <start port> -lp <end port>
     python PrScnr.py --target <IP address> --firstport <start port> --lastport <end port>
```
