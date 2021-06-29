FROM jupyter/tensorflow-notebook

WORKDIR /NER

COPY . .

RUN pip install keras transformers

USER root

RUN cd dataset && sh download.sh
