# Python programming language

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

The disadvantages of Python are of minor consequence: The data science workflow is not time-critical - even an order-of-magnitude slowdown typically makes little difference. Code maintainability is less important - data science scripts are often short and discarded after use. Specific platforms development or enterprise-level applications development are also not part of the typical data science workflow. Data science products used in such applications are normally rewritten as final models in a production-ready code.


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

Many useful libraries are available online, mostly in the [Python Package Index (PyPI) repository](https://pypi.org/). Well-built libraries consist of installation instructions and a *setup.py* file to install them. The common location for installing libraries is the folder *%PYTHON_BASE%/lib*, *%PYTHON_BASE%/site-packages* or *%PYTHON_BASE%/Lib*.
 
Packages can be installed using the `pip` command. For example, to install the [NLTK library](https://www.nltk.org/), we issue the following command: 


```bash
$ pip install nltk
```

In some cases packages will be prebuilt for a specific OS, because the installation of its dependencies can be tedious. In such cases, *wheel packages* can be provided and installed using the following command:


```bash
$ pip install YOUR_DOWNLOADED_PACKAGE.whl
```

An Anaconda distribution provides its own package repository and in addition to pip, Anaconda packages can be installed as follows:


```bash
$ conda install nltk
```

If a package is not available in the official repository, it may be available from some private or community-led channels, for example *conda-forge*:


```bash
$ conda install -c conda-forge pyspark
```

## Jupyter notebooks

The [Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

To add support for Anaconda environments to Jupyter, issue the command below. This will add Conda extensions to Jupyter. The feature will be installed for currently active environment, so you can also install it to the base environment and always run Jupyter from it. When running Jupyter, you will notice a Conda tab in the file browser, which will enable the listing and selection of existing Anaconda environments, overview of the installed packages in the environment, installing new packages from the available package list, checking for updates packages and updating packages in the environment.


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

To get a similar view, save the provided [Jupyter notebook](jupyter/Python programming language.ipynb) into the folder where you ran `jupyter notebook` command. Click the filename of the notebook and it will open in a new window:

![](data/PythonIntroduction/JupyterNotebook.png)

As you notice, a notebook consists of linearly ordered block of types *Markdown*, *Code*, *Raw NBConvert* and *Heading*. If you double click a text block you can edit it using [Markdown syntax](https://www.markdownguide.org/basic-syntax/). To evaluate the block again and show rendered view, click the *Run* button or press *Alt+Enter*. The same holds for other types of blocks. 

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

#### Variables and types

Python defines whole numbers (*int*, *long*) and real numbers (*float*). Whole numbers are integers ($\pm 2^{31}$ or $\pm 2^{63}$) and long numbers, limited by the memory size. Long is a number with a trailing *L* added at the end (Python 2, in Python 3, long is merged with int). Complex numbers are also supported using a trailing *j* to the imaginary part. Bool type is based on integer - value of 1 as *True* or anything else as *False*.

String values are represented as sequence of characters within \" or \'. 

A constant *None* is defined to represent the nonexistence of a value.


```python
a = 2864
print("Type of a is {}".format(type(a)))
```

```
## Type of a is <type 'int'>
```

```python
b = 2864L
print("Type of b is {}".format(type(b)))
```

```
## Type of b is <type 'long'>
```

```python
c = 18+64j
print("Type of c is {}".format(type(c)))
```

```
## Type of c is <type 'complex'>
```

```python
d = False
print("Type of d is {}".format(type(d)))
```

```
## Type of d is <type 'bool'>
```

```python
e = "I'm loving it!"
print("Type of e is {}".format(type(e)))
```

```
## Type of e is <type 'str'>
```

```python
f = None
print("Type of f is {}".format(type(f)))
```

```
## Type of f is <type 'NoneType'>
```

#### Numbers and basic operators {-}

Basic data manipulations:


```python
a = 3  
b = 2.5  
c = a + b 
print("Addition: {}".format(c))
```

```
## Addition: 5.5
```

```python
c = a * b
print("Multiplication: {}".format(c))
```

```
## Multiplication: 7.5
```

```python
c = a / b
print("Division: {}".format(c))
```

```
## Division: 1.2
```

```python
c = True + 5
print("Addition to Boolean: {}".format(c))
```

```
## Addition to Boolean: 6
```

```python
c = "5" * 5
print("String multiplication: {}".format(c))
```

```
## String multiplication: 55555
```

#### Strings, concatenation and formatting

Basic strings manipulations:


```python
a = "Data science" 
b = 'a multi-disciplinary field' # we can use double or single quotes
c = a + " " + b
print("Concatenated string: {}".format(c))
```

```
## Concatenated string: Data science a multi-disciplinary field
```

```python
first = c[:4]
last = c[-5:]
print("First word: '{}' and last word: '{}'.".format(first, last))
```

```
## First word: 'Data' and last word: 'field'.
```

```python
firstLower = first.lower()
lastUpper = last.upper()
print("First word lowercased: '{}' and last word uppercased: '{}'.".\
  format(firstLower, lastUpper))
```

```
## First word lowercased: 'data' and last word uppercased: 'FIELD'.
```

```python
management = c.replace("science", "management")
print("Substring replacement: '{}'".format(management))
```

```
## Substring replacement: 'Data management a multi-disciplinary field'
```

Explore more about strings in the official [Python 3 documentation for strings](https://docs.python.org/3/library/string.html).


```python
# string package
import string
print("Punctuation symbols: '{}'".format(string.punctuation))
```

```
## Punctuation symbols: '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'
```

String manipulation is essential for parsing and providing machine readable outputs when needed. For more sophisticated examples, see [https://pyformat.info/](https://pyformat.info/).


```python
number = 6/.7
text = "dyslexia"

format0 = "Number: " + str(round(number*100)/100.0) + ", Text: " + \
" "*(15-len(text)) + text
print(format0)
```

```
## Number: 8.57, Text:        dyslexia
```

```python
format1 = "Number: {:5.2f}, Text: {:>15}".format(number, text)
print(format1)
```

```
## Number:  8.57, Text:        dyslexia
```

```python
format2 = "Number: %5.2f, Text: %15s" % (number, text)
print(format2)
```

```
## Number:  8.57, Text:        dyslexia
```

#### Data stuctures: Lists, Tuples, Sets, Dictionaries

Below we create some of the data structures available in Python. Explore more of their functionality in [the official Python documentation](https://docs.python.org/3/tutorial/datastructures.html).


```python
l = [1, 2, 3, "a", 10] # List  
t = (1, 2, 3, "a", 10) # Tuple (immutable)
s = {"a", "b", "c"}     # Set
```



```python
dict = {
  "title": "Introduction to Data Science",
  "year": 1,
  "semester": "fall",
  "classroom": "P02"
}
dict["classroom"] = "P03" 
```

We often use inline functions to map, filter or calculate values on an iterable data structure. For example, to apply a function to all values (map), filter out unnecessary values or use all values in a calculation:


```python
#from functools import reduce # Python 3 import for reduce (not needed for Python 2)

l = [6, 8, 22, 4, 12]
doubled = map(lambda x: x*2, l)
print("Doubled: {}".format(doubled))
```

```
## Doubled: [12, 16, 44, 8, 24]
```

```python
filtered = filter(lambda x: x > 10, l)
print("Filtered: {}".format(filtered))
```

```
## Filtered: [22, 12]
```

```python
sum = reduce(lambda x, y: x+y, l)
print("Sum value: {}".format(sum))
```

```
## Sum value: 52
```


```python
l = [6, 8, 22, 4, 12]
newList = [x**2 for x in l if x >= 5 and x <= 10]
print("Squared values between 5 and 10: {}".format(newList))
```

```
## Squared values between 5 and 10: [36, 64]
```

### Control flow operations

Many operations can be written inline or using multiple lines. Let's check how to use *if* statements and *loops*. 


```python
a = 2  
if a > 1:  
    print('a is greater than 1')
elif a == 1:  
    print('a is equal to 1')
else:  
    print('a is less than 1')
```

```
## a is greater than 1
```


```python
# Inline if statement
a = 2
print('a is greater than 1' if a > 1 else 'a is lower or equal to 2')
```

```
## a is greater than 1
```

Loops:


```python
for i in range(4, 6):
    print(i)
```

```
## 4
## 5
```

```python
people_list = ['Ann', 'Bob', 'Charles']  
for person in people_list:
    print(person)
```

```
## Ann
## Bob
## Charles
```

```python
i = 1
while i <= 3:
  print(i)
  i = i + 1
```

```
## 1
## 2
## 3
```

### Functions

We organize (encapsulate) our code into logical units, so we can reuse them and reduce the amount of duplicate, boilerplate code. Below write the function *greetMe* that takes one argument (*name*) as input and prints some string. The function's code will be executed when we call the function.


```python
def greetMe(name):
  print("Hello my friend {}!".format(name))
  
greetMe("Janez")
```

```
## Hello my friend Janez!
```

Sometimes our functions will have many arguments, some of which might be optional or have a default value. In the example below we add a argument with a default value. If there are multiple optional arguments we can set their values by naming them.


```python
def greet(name, title = "Mr."):
  print("Hello {} {}!".format(title, name))
  
greet("Janez")
```

```
## Hello Mr. Janez!
```

```python
greet("Mojca", "Mrs.")
```

```
## Hello Mrs. Mojca!
```

```python
greet("Mojca", title = "Mrs.")
```

```
## Hello Mrs. Mojca!
```

A function can also call itself and return a value.


```python
def sumUpTo(value):
  if value > 0:
    return value + sumUpTo(value-1)
  else: 
    return 0
  
print("Sum of all positive integers up to 50 is: {}".format(sumUpTo(50)))
```

```
## Sum of all positive integers up to 50 is: 1275
```

Python encapsulates variables within functions - they are not accessible outside the function. When we want variables to be accessible globally, we can use the *global* keyword. This can result in some difficult to predict behaviour and interactions, so use with caution!


```python
def playWithVariables(value1, list1):
  global globVal 
  globVal = 3
  
  value1 = 10
  list1.append(22)
  print("Within function: {} and {} and {}".format(value1, list1, globVal))

value1 = 5
list1 = [3, 6, 9]
print("Before function: {} and {}".format(value1, list1))
playWithVariables(value1, list1)
print("After function: {} and {} and {}".format(value1, list1, globVal))
```

```
## Before function: 5 and [3, 6, 9]
## Within function: 10 and [3, 6, 9, 22] and 3
## After function: 5 and [3, 6, 9, 22] and 3
```

In some cases we can also define functions that accept an arbitrary number of unnamed (*args*) and/or named (*kwargs*) arguments.


```python
def paramsWriter(*args, **kwargs):
  print("Non-named arguments: {}\nNamed arguments: {}".format(args, kwargs))

paramsWriter(1, "a", [1,5,6], studentIds = [234, 451, 842], maxScore = 100.0)
```

```
## Non-named arguments: (1, 'a', [1, 5, 6])
## Named arguments: {'maxScore': 100.0, 'studentIds': [234, 451, 842]}
```

When naming functions, classes, objects, packages, etc. we need to be careful not to overwrite existing objects. Bugs such as this one can be difficult to find:


```python
def greeter():
  print("Hello to everyone!")
  
greeter()
greeter = "Mr. John Hopkins"
greeter()                     # Error - greeter is now string value
```

```
Hello to everyone!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
```

### Classes and objects

Python is also object-oriented and therefore enables us to encapsulate data and functionality into classes. Instances of classes are objects.

The class below consists of one class variable, one class method, three object methods and two object variables. All class-based variables are accessible using the class name directly without having instantiated the object. Object-based methods are accessible only through an instantiated object and can also directly modify object properties (*self.\**). All object methods accept *self* as an implicit parameter, which points to the current object.

elow we show an example of object declaration and its use. A detailed explanation can be found in the [official Python documentation](https://docs.python.org/3/tutorial/classes.html).


```python
class Classroom:
  classCounter = 0
  
  def numClasses():
    return Classroom.classCounter
  
  def __init__(self, name):
    Classroom.classCounter += 1
    self.name = "Best of Data Science class " + name
    self.students = []
    
  def enroll(self, student):
    self.students.append(student)
    
  def __str__(self):
    return "Class: '{}', students: '{}'".format(self.name, ", ".join(self.students))
```


```python
class1 = Classroom("best of millenials")
class2 = Classroom("old sports")

print("Num classes: {}".format(Classroom.classCounter))
print("Num classes: {}".format(Classroom.numClasses()))

class2.enroll("Slavko Žitnik")
class2.enroll("Erik Štrumbelj")
class2.enroll("Tomaž Curk")

print(class2)
```

```
## Num classes: 2
## Num classes: 2
## Class: 'Best of Data Science class old sports', students: 'Slavko Žitnik, Erik Štrumbelj, Tomaž Curk'
```

### Python IDE's and code editors

An IDE (Integrated Development Environment) is software dedicated to software development. As the name implies, IDEs integrate several tools specifically designed for software development. These tools usually include:

* An editor designed to handle code with features such as syntax highlighting and auto-completion.
* Build, execution, and debugging tools.
* Some form of source control support.

IDEs are generally large and take time to download and install. You may also need advanced knowledge to use them properly. In contrast, a dedicated code editor can be as simple as a text editor with syntax highlighting and code formatting capabilities. Most good code editors can execute code and control a debugger. The very best ones interact with source control systems as well. Compared to an IDE, a good dedicated code editor is usually smaller and quicker, but often less feature rich.

Below we list some popular Python IDEs/code editors that are available for major operating systems (Windows, Linux and Mac OS):

* [**IDLE**](https://docs.python.org/3/library/idle.html) - the default code editor that installs together with the Python distribution. It includes a Python shell window (interactive interpreter), auto-completion, syntax highlighting, smart indentation and a basic integrated debugger. We do not recommend it for larger projects.
* [**Sublime Text**](https://www.sublimetext.com/), [**Atom**](https://atom.io/), [**Visual Studio Code**](https://code.visualstudio.com/) - highly customizable code editors with rich features of an IDE. They support installation of additional extensions and also provide intelligent code completion, linting for potential errors, debugging, unit testing and so on. These editors are becoming quite popular among Python and web developers.
* [**PyCharm**](https://www.jetbrains.com/pycharm/) - an IDE for professional developers. There are two versions available: a free Community version and a paid Professional version which is free for students only. PyCharm provides all major features of a good IDE: code completion, code inspections, error-highlighting and fixes, debugging, version control system and code refactoring, etc..

## Python ecosystem for Data Science

The Python ecosystem of libraries, frameworks and tools is large and ever-growing. Python can be used for web scraping, machine learning, general scientific computing and many other computing and scripting uses. We list some of the most widely used libraries in the field of data science.

* [**NumPy**](https://www.numpy.org/) - NumPy is the fundamental package for scientific computing with Python. The tools that we commonly use are: a powerful N-dimensional array object, sophisticated (broadcasting) functions, tools for integrating C/C++ and Fortran code and most importantly, linear algebra, Fourier transform and random number capabilities. NumPy can also be used as an efficient multi-dimensional container of generic data, where arbitrary data-types can be defined.
* [**Matplotlib**](https://matplotlib.org/) - A 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, Python and IPython shells, Jupyter notebooks and web application servers. We can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code. It provides a MATLAB-like interface, particularly when combined with IPython. It gives users full control of line styles, font properties, axes properties, etc.
* [**SciPy**](https://www.scipy.org/) - "Sigh Pie"" is a Python-based ecosystem of open-source software for mathematics, science and engineering. In particular, it connects the following core packages: NumPy, SciPy library (fundamentals for scientific computing), Matplotlib, IPython, Sympy (symbolic mathematics) and Pandas.
* [**scikit-learn**](https://scikit-learn.org/stable/) - a Machine Learning (ML) library in Python. It provides simple and efficient tools for data analysis. It offers a framework and many algorithms for classification, regression, clustering, dimensionality reduction, model selection and preprocessing. The library is open source and build on NumPy, SciPy and matplotlib.
* [**Pandas**](https://pandas.pydata.org/) - Python Data Analysis Library (*pandas*) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Some of the library highlights are a fast and efficient DataFrame object for data manipulation with integrated indexing, tools for reading and writing data between in-memory data structures and different formats, intelligent data alignment and integrated handling of missing data, flexible reshaping and pivoting of data sets, high performance merging and joining of data sets, an intuitive way of working with high-dimensional data in a lower-dimensional data structure, time series-functionality.
* [**TensorFlow**](https://www.tensorflow.org/) - TensorFlow is an end-to-end open source platform for machine learning in the field of deep learning. It has a comprehensive and flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers to easily build and deploy ML powered applications.
* [**Keras**](https://keras.io/) - Compared with TensorFlow, Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK or Theano backends. It was developed with a focus on enabling fast experimentation, being able to go from idea to result with the least possible delay. Keras allows for easy and fast prototyping (through user friendliness, modularity and extensibility), supports both convolutional networks and recurrent networks, as well as combinations of the two and runs seamlessly on CPU and GPU.

## Further reading and references

Here is a list of more comprehensive guides to Python programming:

* [Official Python Tutorials](https://docs.python.org/3/tutorial/index.html) - Tutorial accompanying official Python documentation. See this resource for latest features.
* [Beginning Python](http://books.google.com/books?id=S0l1YFpRFVAC&dq=magnus+hetland+beginning+python&printsec=frontcover&source=bn&hl=en&ei=YYLDSvWTNJGPsAb1wNmhBA&sa=X&oi=book_result&ct=result&resnum=4&ved=0CBUQ6AEwAw#v=onepage&q=&f=false) by Magnus Hetland - The book is written for beginners but last chapters are useful also for more experienced programmers.
* [Non-Programmer's Tutorial for Python](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3) - a well organized Wikibook.
* [Think Python](https://en.wikibooks.org/wiki/Think_Python) - similar book to the previous one, but a bit more intermediate.
* [Wikibook: Programming Python] - similar to the above two with more advanced topics.
* [How to Think Like a Computer Scientist](https://runestone.academy/runestone/static/thinkcspy/index.html) - well organized sections for self-paced learning.
* [Python za programerje](https://books.google.com/books/about/Python_za_programerje.html?id=dRrelAEACAAJ) by Janez Demšar - Well known Slovene book, written by the professor at our Faculty. You can find electronic versions online, but printed version is accessible to buy at publishing house FRI (at the entrance).

## Learning outcomes

Data science students should work towards obtaining the knowledge and the skills that enable them to:

* Use the Python programming language for simple programming tasks, data manipulation and file I/0.
* Identify the Python IDE(s) that best fit their requirements.
* Find suitable Python packages for the task at hand and use them.
* Recognize when Python is and when it is not a suitable language to use.

## Practice problems

1. Install Anaconda Python, run the [provided Jupyter notebook](data/01 - Python introduction.ipynb) within a new conda environment and then export all the installed dependencies into an *environment.yml* file (see [reference](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)). Check the file, remove not needed data (location, library versions, libraries in lower dependency trees), create a new environment based on the exported file and run the notebook again (it should work without the need to install additiona packages manually).
2. Try different Python IDEs and form a personal opinion of their advantages and disadvantaged.
3. Download, explore and run some scripts from [the Keras examples repository](https://github.com/keras-team/keras/tree/master/examples).
4. Download [the CMU Seminar Announcements dataset](https://people.cs.umass.edu/~mccallum/data/sa-tagged.tar.gz) and uncompress it. The dataset consists of multiple files, whereas each file represents a seminar anncouncement. Write a program that reads every file and tries to extract the speaker, title, start-time, end-time and the location of the seminar. Help yourself with regular expressions and libraries mentioned above. Store all the extracted data into a Pandas data frame and lastly, export all the data into a single CSV file. In addition, compute your success rate in extraction of specific fields based on the manual tags from the documents.
