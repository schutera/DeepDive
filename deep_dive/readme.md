# DeepDive locally

Don't like the Jupyter environment? Worry not, as here's a short guide on how to run the whole course locally, in very similar blocks as in the Jupyter version. Excercises/side-quests might be slightly different, though!

## Preparing the environment

First, we'll create a [virtual environment](https://docs.python.org/3/library/venv.html):
```
python3 -m venv deep-dive-venv
source deep-dive-venv/bin/activate
```
It's always a good idea to create a virtual environment whenever starting a python project. The idea behind this is to isolate 3rd party packages and not pollute the system. A LOT of 3rd party python packages installed via `pip` consist not only of python scripts, but also of stand-alone executables, added to the PATH. We usually don't want that. And what if you want to simulatnously work on two Deep Learning projects and the other one will be using an older version of TensorFlow?

The examples rely heavily on a few 3rd party libraries such as numpy or TensorFlow mentioned previously. In order to install them, we'll use the supplied `requirements.txt` file. Assuming you're in the repository's root right now, issue the following (make sure the virtual environment is activated):
```
pip install -r deep_dive/requirements.txt
```
Now let's run our application thorough its main [entry point](https://en.wikipedia.org/wiki/Entry_point):
```
python -m deep_dive.src
```

`__main__.py` is usually referred to as the "entry point" to your application. `-m` switch tells Python to start execution from that particular script.
