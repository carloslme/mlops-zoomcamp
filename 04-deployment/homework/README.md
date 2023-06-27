# Homework 04-Deployment 
You can find the files for this homework in this current directory.

## Run script with parameters
```bash
python deployment_homework.py {year} {month}
```

You should expect something like this by inserting `2022` and `4`:
```bash
Standard Deviation: 5.648592560412704
Mean: 12.865128336784926
```

## Run Docker API
### Build the image
```bash
cd 04-deployment/homework
docker build -t api .
```

### Run the image
```bash
docker run -d --name api -p 8000:8000 api
```
Inspect the logs
```bash
docker logs api -f
```

Run the following command to perform a batch prediction:
```bash
curl -X 'POST' \
  'http://localhost:3000/predict?year=2022&month=4' \
  -H 'accept: application/json' \
  -d ''
```

The response will be this:
```bash
"Mean predict value for the year 2022 and month 4 is 12.9"
```
