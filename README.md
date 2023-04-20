
# Extractive summarizer 

A simple nlp based app to generate short summaries of long texts based on their importace




# Link 

https://extractive-summarizer-h9du.onrender.com/







## Installation

Install spacy 

```bash
  pip install spacy
```
Install Textrank

```bash
  pip install pytextrank
```
Install Flask

```bash
  pip install Flask
```
Install pipeline pakage "en_core_web_sm"

```bash
  python -m spacy download en_core_web_sm
```

## Tech Stack

**Client:** HTML CSS

**Server:** Flask

## SETUP
ADD NLP WITH SPACY
```bash
  nlp=spacy.load("en_core_web_sm")
```
ADD A PIPELINE TO SUPPLY TEXTS USING TEXTRANK 

```bash
 nlp.add_pipe('textrank')
```

USE SPACEY PIPELINE WITH TEXTRANK

```bash
doc=nlp(example text)
```
Iterate through each word and create summary using generator object:

```bash
for i in doc._.textrank.summary():
  print(i)

```
# LESSONS

Learnt about nlp models and their working

## Documentation

 - [Spacey](https://spacy.io/usage/spacy-101/)
 - [pipeline](https://spacy.io/models/)
 - [pytextrank](https://github.com/DerwenAI/pytextrank)


## Screenshots

![App Screenshot](https://i.ibb.co/LQKFGfx/Screenshot-2023-03-04-160026.png )


![App Screenshot](https://i.ibb.co/J33WVVw/8.png )
