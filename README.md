# Sri Lankan Lawyer Chatbot

## Overview
The Sri Lankan Lawyer Chatbot is a specialized chatbot designed to provide answers related to Sri Lankan law. It's a Language Model Lawyer (LLM) chatbot capable of answering legal queries. This chatbot is intended for any Sri Lankan user seeking legal information and developers interested in creating their domain-specific chatbot.

## Features
- **Legal Query Resolution**: The chatbot can answer a wide range of legal queries based on Sri Lankan law.
- **Domain-Specific Dataset Creation Pipeline**: Developers can leverage the pipeline to create their domain-specific chatbot.
- **Website PDF Downloader PDF**: This can be used to download all the PDFs on a specific website.
- **Discord Bot Initializer**: Initialize Discord Bot for created Chatbot.

## Usage 
The chatbot can be used in [Discord](https://discord.com/oauth2/authorize?client_id=1219937929330425967&permissions=2183991392320&scope=bot). Simply invite the bot to your server and start asking your legal queries! but note the server won't be up at all times

## Installation steps for Domain-Specific Dataset creation

### 1. Clone the Questgen repository and install dependencies

Clone the Questgen repository to your Colab environment and install the necessary dependencies using the following command:

~~~
!pip install --upgrade --verbose git+https://github.com/omarShiraz/Questgen.ai.git
~~~

### 2. Install other dependencies

Install all other dependencies using the following commands:

~~~
!pip install fitz
!pip install PyMuPDF
!pip install transformers
!pip install --upgrade numpy
!pip install spaCy==2.3.3
!pip install --quiet git+https://github.com/boudinfl/pke.git
!python -m nltk.downloader universal_tagset
!python -m spacy download en_core_web_sm
~~~
After installing these dependencies, make sure to restart the runtime.

### 3. Download and extract the Sense2Vec word vectors

~~~
!wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
!tar -xvf  s2v_reddit_2015_md.tar.gz
!ls s2v_old
~~~

### 4. Import libraries and initialize Questgen

Import the necessary libraries and initialize Questgen using the following Python code:

~~~
import nltk
from pprint import pprint
from Questgen import main
qg = main.QGen()
~~~

### 5. Upload your zip file

Upload your zip file and run the remaining code block to generate the CSV file.

### 6. Install libraries for Hugging Face

Install the necessary libraries to upload the dataset to Hugging Face using the following command:

~~~
!pip install -q datasets transformers sentence_transformers faiss-gpu
~~~
Follow the necessary steps according to the Colab Python notebook file to push the dataset to Hugging Face. Make sure to create a Hugging Face dataset and copy the tokens accordingly.

### 7. Train the chatbot

Run the Fine_Tune_Llama2.ipynb file. Make sure to change the Hugging Face token and the Hugging Face model. Create a new model and use a base model Llama 2 of your choice the official one requires hugginface pro account to fine-tune the LLM model for your domain. After training, make sure to push to Hugging Face. This training can be done over and over (Use different datasets don't train with the same) to refine results and get a better outcome.

## To test Chatbot Lawyer

Chatbot_Lawyer_Model_Inference.ipynb better run this on colab since it takes around 8GB GPU memory. Please avoid starting the server just test it by editing the variable "prompt" in the ipynb file it should work fine

## Tools to ease process

### Automatic PDF downloader Setup

Note: Some websites won't allow this and might block you out

Install these libraries
~~~
pip install os-win
pip install requests
pip install beautifulsoup4
~~~

Edit referer and URL to the website URL you want to download PDFs from

~~~
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Referer': 'https://citizenslanka.org/'
          }
url = "https://citizenslanka.org/laws-of-sri-lanka/" # Website directory
~~~

Change the save directory to the place where the PDFs need to be stored

~~~
save_dir = "/Users/omar/Projects/PycharmProjects/Webscrape/LawData"  # directory to save PDFs
~~~

### Discord Bot Initializer

Note you need to create a discord bot [here](https://discord.com/developers/applications)

Install discord dependency 

~~~
pip install discord
~~~

Change the API_URL and Bot Token accordingly

## Contributing 
Contributions are welcome! Please read the contributing guidelines to get started.

## References

[1]: Questgen: An Open-Source Question Generation Library. Ramsri Goutham Golla
. (2023). *GitHub repository*. https://github.com/ramsrigouthamg/Questgen.ai

[2]: Fine-Tune Llama2Base model used: "NousResearch/Llama-2-7b-chat-hf"

[3]: Hugging Face: A Platform for Natural Language Processing Models. (2023). *Hugging Face*. https://huggingface.co/


## Necessary links below:

LLM-Backed Chatbot Lawyer for Enhanced Legal Services in Sri Lanka

Reference List - https://app.bibguru.com/p/e8e1b7eb-8ffd-4ead-a2ce-4b76df764773

Dataset Example - https://huggingface.co/datasets/totally-not-an-llm/EverythingLM-data-V3/viewer/default/train?p=10

Question Generation Repo - https://github.com/ramsrigouthamg/Questgen.ai

LLM Model Falcon-7B - https://huggingface.co/tiiuae/falcon-7b

Bibguru - https://app.bibguru.com/p/e8e1b7eb-8ffd-4ead-a2ce-4b76df764773

FYP Materials - https://drive.google.com/drive/folders/1_lWNnOaNq81I23H-x6dstfOX0bpm9LJL

Literature review structure - https://docs.google.com/document/d/1ShTjqXpKcEQ2d7wmhSGbaYl1bNPOU5FC/edit

Past FYP projects - https://docs.google.com/spreadsheets/d/1iaDG9pUIJQNYAHMYFq0uStdTzgLah2d1ODMfQlfqjCg/edit#gid=10835512

Research Papers - https://sci-hub.se/

Canva Diagrams - https://www.canva.com/folder/FAF1oNE0SrA

FYP Reports - https://drive.google.com/drive/folders/13oZezcOKrhu7M4l-lF7DHNQMz93FTOxC?usp=drive_link
