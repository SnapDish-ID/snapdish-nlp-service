# snapdish-nlp-service

SnapDish NLP Service provide recipes recommendation based on user input. This service receive main ingredient and list of ingredients from user and return top 3 recipes based on consine similarity score.

## Pre-requisites

- Python 3.9

## Run locally

1. Navigate to project root

2. Create python virtual environment

   ```shell
   python3.9 -m venv .venv
   ```

3. Activate virtual environment

   ```shell
   source .venv/bin/activate # for Linux, macOS
   ```

   ```powershell
   .venv\Scripts\activate # for Windows
   ```

4. Install dependencies

   ```shell
   pip install -r requirements.txt
   ```

5. Run flask app

   ```shell
   flask run
   ```
