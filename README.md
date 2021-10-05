# demo

```sh
# setup locally
virtualenv -p python3.8 -v venv
source venv/bin/activate
pip install -r tests/requirements.txt -r app/requirements.txt

# test
pytest -v

# deploy
sam build --use-container
sam deploy --guided

# destroy
aws cloudformation delete-stack --stack-name demo

# run
uvicorn app.app:app --reload
```
