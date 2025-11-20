# Web Crawler vs Spider Trap — Demonstration Project

This project is a simple, educational example showing how spider traps can be used as a cyber-deception technique to slow down, mislead, or detect automated web crawlers and scrapers.
It is part of the Cyber Security module under the theme “Cyber Deception: Honeypots and Decoys.”

# Overiew

## the site

very basic web site build with svelte kit contains hidden links for :

- api endpoint that blocks the ip address of the client .
- a dinamic uri generator for endless navigation.

check

```bash
/spider-trap/src
```

for further info

# Usage

you will need python and node.js installed on your machine.  
after cloning the repo :

```shell
cd spider-trap
npm i
npm run build
node build # to get a standalone server running
```

now after you got the site up and running now it's time to set up the crawler

```bash
cd web-crawler
# create and activate a virtual environment
python -m venv venv
venv\Scripts\activate
# install dependencies
pip install -r requirements.txt
# run the crawler
python index.py
```

here you go you have the example running.
