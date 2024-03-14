<div id="top"></div>


<!-- ABOUT THE PROJECT -->
## About The Project

This project is for a lecture at Karlsruhe Institute of Technology. It aims at mechanical engineers diving into deep learning and enabling to get their hands dirty on some practical application of deep learning.

Here's why this project fits so well for this:
* The project is an interactive jupyter notebook, which makes it easy to walk through the explanations, run the code and immediately experience the change
* The project is hosted on binder so there is no setup necessary and students can directly run the project in their browser
* It covers a fundamental tensorflow tutorial on MNIST, including essential validation approaches

Of course, no one project will serve all levels of expertice since your needs may be different. This is an attempt to kickstart rookies. You may also contribute or suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this project so far! You started your own deep learning projects and wonder 'why does my neural network not learn?' - here are my [coffee table solutions](https://www.amazon.de/dp/B09QRGWWZP) for you.


### Built With

* [tensorflow](https://tensorflow.org/)
* [jupyter notebook](https://jupyter.org/)
* [binder](https://mybinder.org/)



<!-- GETTING STARTED -->
## Getting Started

Buckle up, click the button and off you go..


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/schutera/DeepDive/HEAD?filepath=%2FDeepDive.ipynb)


## Run it locally

If you prefer to run the examples as a full-fledged 'project' on your *nix machine, `deep_dive` folder is the place to start.

First, we'll create a [virtual environment](https://docs.python.org/3/library/venv.html):
```
python3 -m venv deep-dive-venv
source deep-dive-venv/bin/activate
```
The examples rely heavily on a few 3rd party libraries such as numpy or TensorFlow mentioned previously. In order to install them, we'll use the supplied `requirements.txt` file. Assuming you're in the repository's root right now, issue the following (make sure the virtual environment is activated):
```
pip install -r deep_dive/requirements.txt
```
Now let's run our application thorough its main [entry point](https://en.wikipedia.org/wiki/Entry_point):
```
python -m deep_dive.src
```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.




<!-- CONTACT -->
## Contact

Mark Schutera - mark.schutera@gmail.com




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

So long, and thanks for all the fish.

<p align="right">(<a href="#top">back to top</a>)</p>

