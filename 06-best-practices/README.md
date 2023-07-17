* Run Localstack docker-compose.yml file
```bash
docker-compose -f integration-test/docker-compose.yaml up
```
* Install `awslocal`
```bash
pip install awscli-local
```

* Create Localstack S3 bucket
```bash
awslocal s3 mb s3://nyc-duration
```

* List files in S3 bucket
```bash
awslocal s3 ls s3://nyc-duration
```

awslocal --endpoint-url=http://localhost:4566 s3 ls s3://nyc-duration