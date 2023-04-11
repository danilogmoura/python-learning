#!/usr/bin/env python3
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as imputFile:
        print("Download...")
        data = imputFile.read().decode("latin1")
        print("Download complete.")
        for city in csv.reader(data.splitlines()):
            print(f"{city[8]}: {city[3]}")


if __name__ == "__main__":
    read(r"http://files.cod3r.com.br/curso-python/desafio-ibge.csv")
