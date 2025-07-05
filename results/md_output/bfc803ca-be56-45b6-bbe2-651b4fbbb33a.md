Advisor
Introduction
Advisor is the hyper parameters tuning system for black box optimization.
It is the open‑source implementation of Google Vizier with these features.
• Easy to use with API, SDK, WEB and CLI
• Support abstractions of Study and Trial
• Included search and early stop algorithms
• Recommend parameters with trained model
• Same programming interfaces as Google Vizier
• Command‑line tool just like Microsoft NNI.
Supported Algorithms
⊠
Grid Search
⊠
Random Search
⊠
Bayesian Optimization
⊠
TPE(Hyperopt)
⊠
Random Search(Hyperopt)
1

⊠
Simulate Anneal(Hyperopt)
⊠
Quasi Random(Chocolate)
⊠
Grid Search(Chocolate)
⊠
Random Search(Chocolate)
⊠
Bayes(Chocolate)
⊠
CMAES(Chocolate)
⊠
MOCMAES(Chocolate)
□
SMAC Algorithm
⊠
Bayesian Optimization(Skopt)
⊠
Early Stop First Trial Algorithm
⊠
Early Stop Descending Algorithm
□
Performance Curve Stop Algorithm
Quick Start
It is easy to setup advisor service in local machine.
1 pip install advisor
2
3 advisor_admin server start
Then go to http://127.0.0.1:8000 in the browser and submit tuning jobs.
1 git clone --depth 1 https://github.com/tobegit3hub/advisor.git && cd ./
advisor/
2
3 advisor run -f ./advisor_client/examples/python_function/config.json
4
5 advisor study describe -s demo
Advisor Server
Run server with official package.
1 advisor_admin server start
Or run with official docker image.
1 docker run -d -p 8000:8000 tobegit3hub/advisor
Or run with docker‑compose.
1
2

| 1 pip install advisor        |
|:-----------------------------|
| 2                            |
| 3 advisor_admin server start |

| 1 git clone --depth 1 https://github.com/tobegit3hub/advisor.git && cd ./   |
|:----------------------------------------------------------------------------|
| advisor/                                                                    |
| 2                                                                           |
| 3 advisor run -f ./advisor_client/examples/python_function/config.json      |
| 4                                                                           |
| 5 advisor study describe -s demo                                            |

2 wget https://raw.githubusercontent.com/tobegit3hub/advisor/master/
docker-compose.yml
3
4 docker-compose up -d
Or run in Kubernetes cluster.
1 wget https://raw.githubusercontent.com/tobegit3hub/advisor/master/
kubernetes_advisor.yaml
2
3 kubectl create -f ./kubernetes_advisor.yaml
Or run from scratch with source code.
1 git clone --depth 1 https://github.com/tobegit3hub/advisor.git && cd ./
advisor/
2
3 pip install -r ./requirements.txt
4
5 ./manage.py migrate
6
7 ./manage.py runserver 0.0.0.0:8000
Advisor Client
Install with pip or use docker container.
1 pip install advisor
2
3 docker run -it --net=host tobegit3hub/advisor bash
Use the command‑line tool.
1 export ADVISOR_ENDPOINT="http://127.0.0.1:8000"
2
3 advisor study list
4
5 advisor study describe -s "demo"
6
7 advisor trial list --study_name "demo"
Use admin tool to start/stop server.
1 advisor_admin server start
2
3 advisor_admin server stop
Use the Python SDK.
3

| 2 wget https://raw.githubusercontent.com/tobegit3hub/advisor/master/   |
|:-----------------------------------------------------------------------|
| docker-compose.yml                                                     |
| 3                                                                      |
| 4 docker-compose up -d                                                 |

| 1 wget https://raw.githubusercontent.com/tobegit3hub/advisor/master/   |
|:-----------------------------------------------------------------------|
| kubernetes_advisor.yaml                                                |
| 2                                                                      |
| 3 kubectl create -f ./kubernetes_advisor.yaml                          |

| 1 git clone --depth 1 https://github.com/tobegit3hub/advisor.git && cd ./   |
|:----------------------------------------------------------------------------|
| advisor/                                                                    |
| 2                                                                           |
| 3 pip install -r ./requirements.txt                                         |
| 4                                                                           |
| 5 ./manage.py migrate                                                       |
| 6                                                                           |
| 7 ./manage.py runserver 0.0.0.0:8000                                        |

| 1 pip install advisor                                |
|:-----------------------------------------------------|
| 2                                                    |
| 3 docker run -it --net=host tobegit3hub/advisor bash |

| 1 export ADVISOR_ENDPOINT="http://127.0.0.1:8000"   |
|:----------------------------------------------------|
| 2                                                   |
| 3 advisor study list                                |
| 4                                                   |
| 5 advisor study describe -s "demo"                  |
| 6                                                   |
| 7 advisor trial list --study_name "demo"            |

| 1 advisor_admin server start   |
|:-------------------------------|
| 2                              |
| 3 advisor_admin server stop    |

1 client = AdvisorClient()
2
3 # Create the study
4 study_configuration = {
5 "goal": "MAXIMIZE",
6 "params": [
7 {
8 "parameterName": "hidden1",
9 "type": "INTEGER",
10 "minValue": 40,
11 "maxValue": 400,
12 "scalingType": "LINEAR"
13 }
14 ]
15 }
16 study = client.create_study("demo", study_configuration)
17
18 # Get suggested trials
19 trials = client.get_suggestions(study, 3)
20
21 # Complete the trial
22 trial = trials[0]
23 trial_metrics = 1.0
24 client.complete_trial(trial, trial_metrics)
Please checkout examples for more usage.
Configuration
Study configuration describe the search space of parameters. It supports four types and here is the
example.
1 {
2 "goal": "MAXIMIZE",
3 "randomInitTrials": 1,
4 "maxTrials": 5,
5 "maxParallelTrials": 1,
6 "params": [
7 {
8 "parameterName": "hidden1",
9 "type": "INTEGER",
10 "minValue": 1,
11 "maxValue": 10,
12 "scalingType": "LINEAR"
13 },
14 {
15 "parameterName": "learning_rate",
16 "type": "DOUBLE",
4

| 1 client = AdvisorClient()                                  |
|:------------------------------------------------------------|
| 2                                                           |
| 3 # Create the study                                        |
| 4 study_configuration = {                                   |
| 5 "goal": "MAXIMIZE",                                       |
| 6 "params": [                                               |
| 7 {                                                         |
| 8 "parameterName": "hidden1",                               |
| 9 "type": "INTEGER",                                        |
| 10 "minValue": 40,                                          |
| 11 "maxValue": 400,                                         |
| 12 "scalingType": "LINEAR"                                  |
| 13 }                                                        |
| 14 ]                                                        |
| 15 }                                                        |
| 16 study = client.create_study("demo", study_configuration) |
| 17                                                          |
| 18 # Get suggested trials                                   |
| 19 trials = client.get_suggestions(study, 3)                |
| 20                                                          |
| 21 # Complete the trial                                     |
| 22 trial = trials[0]                                        |
| 23 trial_metrics = 1.0                                      |
| 24 client.complete_trial(trial, trial_metrics)              |

| 1 {                                  |
|:-------------------------------------|
| 2 "goal": "MAXIMIZE",                |
| 3 "randomInitTrials": 1,             |
| 4 "maxTrials": 5,                    |
| 5 "maxParallelTrials": 1,            |
| 6 "params": [                        |
| 7 {                                  |
| 8 "parameterName": "hidden1",        |
| 9 "type": "INTEGER",                 |
| 10 "minValue": 1,                    |
| 11 "maxValue": 10,                   |
| 12 "scalingType": "LINEAR"           |
| 13 },                                |
| 14 {                                 |
| 15 "parameterName": "learning_rate", |
| 16 "type": "DOUBLE",                 |

17 "minValue": 0.01,
18 "maxValue": 0.5,
19 "scalingType": "LINEAR"
20 },
21 {
22 "parameterName": "hidden2",
23 "type": "DISCRETE",
24 "feasiblePoints": "8, 16, 32, 64",
25 "scalingType": "LINEAR"
26 },
27 {
28 "parameterName": "optimizer",
29 "type": "CATEGORICAL",
30 "feasiblePoints": "sgd, adagrad, adam, ftrl",
31 "scalingType": "LINEAR"
32 },
33 {
34 "parameterName": "batch_normalization",
35 "type": "CATEGORICAL",
36 "feasiblePoints": "true, false",
37 "scalingType": "LINEAR"
38 }
39 ]
40 }
Here is the configuration file in JSON format for advisor run.
1 {
2 "name": "demo",
3 "algorithm": "BayesianOptimization",
4 "trialNumber": 10,
5 "concurrency": 1,
6 "path": "./advisor_client/examples/python_function/",
7 "command": "./min_function.py",
8 "search_space": {
9 "goal": "MINIMIZE",
10 "randomInitTrials": 3,
11 "params": [
12 {
13 "parameterName": "x",
14 "type": "DOUBLE",
15 "minValue": -10.0,
16 "maxValue": 10.0,
17 "scalingType": "LINEAR"
18 }
19 ]
20 }
21 }
Or use the equivalent configuration file in YAML format.
5

| 17 "minValue": 0.01,                             |
|:-------------------------------------------------|
| 18 "maxValue": 0.5,                              |
| 19 "scalingType": "LINEAR"                       |
| 20 },                                            |
| 21 {                                             |
| 22 "parameterName": "hidden2",                   |
| 23 "type": "DISCRETE",                           |
| 24 "feasiblePoints": "8, 16, 32, 64",            |
| 25 "scalingType": "LINEAR"                       |
| 26 },                                            |
| 27 {                                             |
| 28 "parameterName": "optimizer",                 |
| 29 "type": "CATEGORICAL",                        |
| 30 "feasiblePoints": "sgd, adagrad, adam, ftrl", |
| 31 "scalingType": "LINEAR"                       |
| 32 },                                            |
| 33 {                                             |
| 34 "parameterName": "batch_normalization",       |
| 35 "type": "CATEGORICAL",                        |
| 36 "feasiblePoints": "true, false",              |
| 37 "scalingType": "LINEAR"                       |
| 38 }                                             |
| 39 ]                                             |
| 40 }                                             |

| 1 {                                                     |
|:--------------------------------------------------------|
| 2 "name": "demo",                                       |
| 3 "algorithm": "BayesianOptimization",                  |
| 4 "trialNumber": 10,                                    |
| 5 "concurrency": 1,                                     |
| 6 "path": "./advisor_client/examples/python_function/", |
| 7 "command": "./min_function.py",                       |
| 8 "search_space": {                                     |
| 9 "goal": "MINIMIZE",                                   |
| 10 "randomInitTrials": 3,                               |
| 11 "params": [                                          |
| 12 {                                                    |
| 13 "parameterName": "x",                                |
| 14 "type": "DOUBLE",                                    |
| 15 "minValue": -10.0,                                   |
| 16 "maxValue": 10.0,                                    |
| 17 "scalingType": "LINEAR"                              |
| 18 }                                                    |
| 19 ]                                                    |
| 20 }                                                    |
| 21 }                                                    |

1 name: "demo"
2 algorithm: "BayesianOptimization"
3 trialNumber: 10
4 path: "./advisor_client/examples/python_function/"
5 command: "./min_function.py"
6 search_space:
7 goal: "MINIMIZE"
8 randomInitTrials: 3
9 params:
10 - parameterName: "x"
11 type: "DOUBLE"
12 minValue: -10.0
13 maxValue: 10.0
Screenshots
List all the studies and create/delete the studies easily.
List the detail of study and all the related trials.
6

| 1 name: "demo"                                       |
|:-----------------------------------------------------|
| 2 algorithm: "BayesianOptimization"                  |
| 3 trialNumber: 10                                    |
| 4 path: "./advisor_client/examples/python_function/" |
| 5 command: "./min_function.py"                       |
| 6 search_space:                                      |
| 7 goal: "MINIMIZE"                                   |
| 8 randomInitTrials: 3                                |
| 9 params:                                            |
| 10 - parameterName: "x"                              |
| 11 type: "DOUBLE"                                    |
| 12 minValue: -10.0                                   |
| 13 maxValue: 10.0                                    |

List all the trials and create/delete the trials easily.
List the detail of trial and all the related metrics.
7

Development
You can edit the source code and test without re‑deploying the server and client.
1 git clone git@github.com:tobegit3hub/advisor.git
2
3 cd ./advisor/advisor_client/
4
5 python ./setup.py develop
6
7 export PYTHONPATH="/Library/Python/2.7/site-packages/:$PYTHONPATH"
8

| 1 git clone git@github.com:tobegit3hub/advisor.git                   |
|:---------------------------------------------------------------------|
| 2                                                                    |
| 3 cd ./advisor/advisor_client/                                       |
| 4                                                                    |
| 5 python ./setup.py develop                                          |
| 6                                                                    |
| 7 export PYTHONPATH="/Library/Python/2.7/site-packages/:$PYTHONPATH" |