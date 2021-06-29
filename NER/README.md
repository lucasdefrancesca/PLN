
# NER

<p  align="center">
<img  src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg"  alt="Sklearn"  width="50"  height="50"/>
<img  src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg"  alt="tensorflow"  width="40"  height="40"/>
<img  src="https://upload.wikimedia.org/wikipedia/commons/a/ae/Keras_logo.svg"  alt="keras"  width="30"  height="30"/>
<img  src="https://huggingface.co/front/assets/huggingface_logo.svg"  alt="hugginface"  width="40"  height="40"/>
<img  src="https://www.vectorlogo.zone/logos/docker/docker-icon.svg"  alt="docker"  width="50"  height="50"/>
<img  src="https://www.vectorlogo.zone/logos/python/python-icon.svg"  alt="python"  width="40"  height="40"/>
</p>
<p>&nbsp;</p>

Para la implementación de los distintos modelos de reconocimiento de entidades nombradas, vamos a utilizar los datos del desafió abierto [CoNLL-2002](https://www.aclweb.org/anthology/W02-2024.pdf).

Mostraré tres enfoques distintos para el desarrollo de un sistema NER. El primero se basa en una implementación de un clasificador con ventana deslizante usando *support vector machine* como modelo (directorio  ``` SVM```) . Luego una implementación basada en redes neuronales, donde se crea un modelo híbrido el cual posee en la arquitectura una capa BiLSTM y una CNN para la representación a nivel carácter de las palabras (directorio  ``` BiLSTM```). Y por último una implementación utilizando modelos de lenguajes con la arquitectura *Transformers*, en este caso utilizando el modelo de lenguaje BETO (*Spanish BERT model*) por medio de la librería [HuggingFace](https://huggingface.co/) (directorio  ```BERT```).

### Obtener el *Dataset*

```
cd dataset && sh download.sh
```
El conjunto de datos tiene definido cuatro tipos de entidades, *personas* (PER), *organizaciones* (ORG), *ubicación* (LOC) y *terminología general* (MISC). El mismo se encuentra en formato CoNLL utilizando el esquema de etiquetas BIO y particionado en tres subconjuntos:
* *train set*
* *dev set*
* *test set* 

Ejemplo de oración del conjunto de datos
```
Izquierda  B-ORG
Unida      I-ORG
de         I-ORG
Santander  I-ORG
presentó   O
hoy        O
su         O
nuevo      O
boletín    O
trimestral O
```
### Correr con Docker

Construcción de la imagen 
```
docker build -t ner .
```

Ejecución de la imagen
```
docker run --rm -p 8888:8888 ner
```

### Trabajo futuro
```
- [ ] Crear Blog Post mas detallado sobre NER.
```
