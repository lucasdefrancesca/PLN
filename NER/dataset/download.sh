#!/bin/bash

wget http://www.cnts.ua.ac.be/conll2002/ner.tgz && tar -xvzf ner.tgz

gzip -d ner/data/esp.testa.gz && cp ner/data/esp.testa .
gzip -d ner/data/esp.testb.gz && cp ner/data/esp.testb .
gzip -d ner/data/esp.train.gz && cp ner/data/esp.train .

iconv --from-code=iso-8859-1 --to-code=utf-8 esp.train > train.txt
iconv --from-code=iso-8859-1 --to-code=utf-8 esp.testa > dev.txt
iconv --from-code=iso-8859-1 --to-code=utf-8 esp.testb > test.txt

rm -rf ner 
rm -f ner.tgz esp.testa esp.testb esp.train
