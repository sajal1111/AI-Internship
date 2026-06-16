\# Task 3: Model Deployment



\## Objective



Deploy the Resume Classification model using FastAPI and Docker.



\## Requirements



Python 3.11



FastAPI



TensorFlow



Pandas



NumPy



scikit-learn



\## Run locally



Activate virtual environment:



```bash

venv\\Scripts\\activate

```



Run API:



```bash

python -m uvicorn app:app --reload

```



Open:



```

http://127.0.0.1:8000/docs

```



\## Example Request



```json

{

&#x20; "resume":"Python developer with machine learning experience"

}

```



\## Example Response



```json

{

&#x20; "category":"Python Developer",

&#x20; "confidence":"93.42%"

}

```



\## Docker



Build:



```bash

docker build -t resume-api .

```



Run:



```bash

docker run -p 8000:8000 resume-api

```



