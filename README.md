# mle-26

Author: Samantha Roska

### Dependancies

- Python 3.0
- Fastapi
- Pydantic
- Pandas
- Joblib
- pytest
- uvicorn

### Variables

| Parameter      | Description |
| ----------- | ----------- |
| REGISTRY      | container image registry       |
| CLUSTER   | Kubernetes Cluster Host      |


### Local Development

1. Install python dependancies
```
$ pip3 install -r packages.txt
```

2. Start-up locally
```
$ cd model-app
$ python3 -m uvicorn api.predict:app --reload
```
3. Swagger like api at http://127.0.0.1:8080/docs#/


### Local Docker Build

1. Build image locally  Note: using 'latest' is not best practice. You should ALWAYS version your image in the registry
```
$ cd MLE-26
$ docker build -t ml26:latest .
$ docker image ls
```

2. Run container will newly created image

```
$ docker container run --name ml26 -p 80:1313 ml26:latest
```
Docker image will expose port 1313. the -p will portforward your localhost:80 to use the container port 1313

3. Stop container
```
$ docker container stop ml26
```

### Next Steps
 - parameterize the training process by providing an endpoint to supply new training data and output new pkl file
 - logging/monitoring pattern for metrics
 - Terraform development if deployment is to a Cloud provider
 - joblib has a memory functionality - useful for some usecases and might explore for batches