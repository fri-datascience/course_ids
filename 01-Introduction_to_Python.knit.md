# Python programming language {#python-introduction-chapter}

## Basic characteristics

Python is an [interpreted](https://en.wikipedia.org/wiki/Interpreted_language), [dynamically typed](https://en.wikipedia.org/wiki/Dynamic_programming_language), [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming) language.

Advantages:

* Simple.
* Easy to learn.
* Extensive packages.
* Cross-platform.
* Free and open source.
* Large user base.

Disadvantages:

* Being interpreted results in slower execution.
* Dynamic typing can lead to errors that only show up at runtime.
* Higher memory consumption, less suitable for memory-intensive tasks.

<!-- 
  * Underdeveloped database access layers.
  * Less suitable for mobile development and mobile computing. 
-->

## Why Python?

The Python language is one of the two most popular languages for data science (the other being R). The two main reasons are:

* The advantages of Python fit the typical data science workflow and its disadvantages are not that deterimental to the data science workflow.
* Python has a large ecosystem of packages, libraries and tools for data science, some of which are discussed later in this chapter.
* Often libraries and software developed in other languages provide Python API or bindings.

The typical data science workflow consists of acquiring and manipulating data and applying standard machine learning or statistical methods. In essence, the data flows through different methods. The emphasis is on obtaining results - extracting meaningful information from data.

The advantages of Python are extremely beneficial to such a workflow: Being simple, easy to learn and free, it is accessible to a larger user base, including users with little or no prior programming experience. Being an interpreted language (and straightforward piecewise execution through read-eval-print loop shells or REPL) makes Python very flexible - multiple alternatives can be explored and quick decisions made on how to procede, depending on intermediary results.

The disadvantages of Python are of minor consequence: The data science workflow is not time-critical - even an order-of-magnitude slowdown typically makes little difference. Memory and time consumption can be significantly decreased by using popular libraries such as numpy and scipy. Code maintainability is less important - data science scripts are often short and discarded after use. Specific platforms development or enterprise-level applications development are also not part of the typical data science workflow. Data science products used in such applications are normally rewritten as final models in a production-ready code.


## Setting up the environment

Before using Python, we need to select and install a desired Python distribution. We can choose to install a pure Python distribution or an Anaconda Python distribution. Some advantages of using an Anaconda distribution are:

* Anaconda makes it easy for the user to install the Python version of choice. Anaconda will also resolve issues with administrator privileges if a user does not have administrative rights for his system.
* [Anaconda Accelerate](https://docs.continuum.io/accelerate/index.html) can provide the user with high performance computing and several other components.
* Anaconda removes bottlenecks involved in installing the right packages while taking into considerations their compatibility with various other packages as might be encountered while using the traditional package manager (pip).
* There is no risk of breaking required system libraries. There are also many open source packages available for Anaconda, which are not within the pip repository.

We encourage you to use the Anaconda Python distribution.

### Anaconda distribution installation

Install the desired [Anaconda Python distribution](https://www.anaconda.com/distribution/). A useful way of managing multiple Python projects is to use Conda environments. An environment enables you to use a specific version of Python along with specific dependencies completely separately on a single system. To create and use an environment with a name *itds*, issue the following command:


```bash
$ conda create -n itds
$ conda activate itds
```

At the beginning of a line in the console you can see currently active environment. To run Python within this evironment, issue the `python` command in the console. You should see something similar to the following:


```bash
(itds)$ python
Python 3.6.8 |Anaconda, Inc.| (default, Dec 29 2018, 19:04:46)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

To exit the Python interpreter, enter and commit the command `exit()`;

To exit the environment, use `conda deactivate`. To show existing environments and their locations, issue `conda info --envs`. 

### Pure Python distribution installation

You can also install a pure Python distributiondirectly to your system from [the official Python Downloads web page](https://www.python.org/downloads/).

To run Python, issue the `python` command in the console (there may be more interpreters installed on your machine and Python 3.5 might be run also using `python3.5`). After running the command, you should see something similar to the following:


```bash
$ python
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

When using the distribution directly, all packages and settings are changed system-wide, which may lead to problems when maintaining multiple Python projects (e.g. problems in having installed different versions of a specific library). Similar to an Anaconda distribution, one can use *virtualenv* virtual environments. First, we need to install *virtualenv* via *pip*:


```bash
$ pip3 install virtualenv
$ virtualenv --version
16.6.1
```

To set up a virtual environment for a project, first create a project folder and set up a new environment in that folder. The latter will create Python executables within that folder and a copy of *pip* library that is used to install libraries local to the environment (parameter *p* is optional).


```bash
$ cd itds_project
$ virtualenv -p /usr/local/bin/python2 itds
```

To activate the environment, run the script `venv/bin/activate` from the project folder and use project specific Python:


```bash
$ source itds/bin/activate
(itds)$ python
Python 2.7.14 (default, Mar  9 2018, 23:57:12)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

After you finish working on your project, deactivate the current virtual environment:


```bash
(itds)$ deactivate
$
```

## Installing dependencies

An Anaconda distribution provides its own [package repository](https://anaconda.org/anaconda/repo) and Anaconda packages can be installed as follows:


```bash
$ conda install nltk
```

If a package is not available in the official repository, it may be available from some private or community-led channels, for example *conda-forge*:


```bash
$ conda install -c conda-forge pyspark
```

Many useful libraries are available online, mostly in the [Python Package Index (PyPI) repository](https://pypi.org/) which can also be used directly in a conda environment. Well-built libraries consist of installation instructions and a *setup.py* file to install them. The common location for installing libraries is the folder *%PYTHON_BASE%/lib*, *%PYTHON_BASE%/site-packages* or *%PYTHON_BASE%/Lib*.
 
Packages can be installed using the `pip` command. For example, to install the [NLTK library](https://www.nltk.org/), we issue the following command: 


```bash
$ pip install nltk
```

In some cases packages will be prebuilt for a specific OS, because the installation of its dependencies can be tedious. In such cases, *wheel packages* can be provided and installed using the following command:


```bash
$ pip install YOUR_DOWNLOADED_PACKAGE.whl
```

## Jupyter notebooks

The [Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

To add support for Anaconda environments to Jupyter, issue the command below. This will add Conda extensions to Jupyter. The feature will be installed for currently active environment. When running Jupyter, you will notice a Conda tab in the file browser, which will enable the listing and selection of existing Anaconda environments, overview of the installed packages in the environment, installing new packages from the available package list, checking for updates packages and updating packages in the environment.


```bash
$ conda install nb_conda
```

### Running a Jupyter notebook

Prior to running a Jupyter notebook we first need to start a Jupyter web server by issuing a command:


```bash
$ jupyter notebook
```

By default the server is started in the current folder and accessible via the web interface: [http://localhost:8888](http://localhost:8888). The root web page shows a file browser where we can create a new Jupyter notebook or open an existing one: 

![](data/PythonIntroduction/JupyterFileBrowser.png)

To get a similar view, save the provided [Jupyter notebook](jupyter/Python programming language.ipynb) into the folder where you run `jupyter notebook` command. Click the filename of the notebook and it will open in a new window:

![](data/PythonIntroduction/JupyterNotebook.png)

As you notice, a notebook consists of linearly ordered blocks of types *Markdown*, *Code*, *Raw NBConvert* and *Heading*. If you double click a text block you can edit it using [Markdown syntax](https://www.markdownguide.org/basic-syntax/). To evaluate the block again and show rendered view, click the *Run* button or press *Alt+Enter*. The same holds for other types of blocks. 

Sometimes we just want to view or execute a notebook online. There exist multiple services offering this functionality, for example [https://gke.mybinder.org/](https://gke.mybinder.org/).


## Short introduction to Python

All the examples presented in this section are also provided in a [Jupyter notebook](jupyter/Python programming language.ipynb).

### Basics {-}

Let's first say hello:


```python
print("Hello Data science!")
```

```
## Hello Data science!
```

Now we know how to print something to the output. Before we dive into details, let's first check how we can easily output literal values and variables. Let's have a variable *name* and *age* with specific values and form a form a final string to show to a user.























































