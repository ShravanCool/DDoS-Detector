# DDoS Detection

Classification and Prediction of DDoS attacks using Machine Learning techniques. Using a web-based interface, the model gets its input from the user, and predicts whether the given inputs match that of a DDoS attack, or is beningn traffic.

## Directions for Setting up Environment-

To install the source, pre-requisites include-

- Python 3.6 or above
- Dependencies from requirements.txt

First, clone this repository onto your system. Then, create a virtual environment and install the packages from requirements.txt:
```
cd path/to/folder
virtualenv venv -p python3.6  //or any other name and version
source venv/bin/activate
```
Now, install the python dependencies from requirements.txt:
```
pip install -r requirements.txt
```

## Directions to execute-

Inside the main project directory(the directory with the 'manage.py' file), run the following command-
```
python manage.py runserver
```

Now, open the below mentioned link in a new tab in your browser-
[https://127.0.0.1:8000](https://127.0.0.1:8000)
