![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300&section=header&text=LMZ%20Data%20Analyzer&fontSize=90&animation=fadeIn&fontAlignY=43&desc=PE02%20TEAM%20A3&descAlignY=55&descAlign=62)
# A3TW
***
## INDEX
- [Description](#description)
- [Prerequisite](#prerequisite)
- [Environment](#environment)
- [Files](#files)
- [Usage](#usage)
- [Contributing](#contributing)

## Description
***
We created a module for extracting and analyzing data provided by customers. A project was created to display and store data results in graphs and csv files.

## Prerequisite
***
* Install pandas to process data. It is known as an essential library for tasks such as data analysis using Python.http://pandas.pydata.org/pandas-docs/stable/
Install xml.etree.elemenTree. The module implements a simple and efficient API for parsing and creating XML data.
Install numpy. Numpy is Python package that deals with numerical data. It is mainly used in linear algebra calculations using vectors and matrices via ndarray, a multidimensional matrix data structure called the core of Numpy.
Install matplotlib.pyplot. Used to vissualize data understanding prior to data analysis, or to visualize results after data analysis.
Install lmfit. Lmfit provides a high-level interface to non-linear optimization and curve fitting problems for Python. https://lmfit.github.io/lmfit-py/

If you want install all prerequisite, Write 'pip install -r requirements.txt'.

## Environment
***
* Python 3.8
* PyCharm Community Edition 2021.2.2
* Windows 11 Home 21H2

## Files
***
* ### src
  * #### csv_maker.py - The analysis result is made into a csv file, and the contents of the error occurrence according to the rsq value are included.
  * #### filter.py - Find the file in the dat file by combining the entered file names.
  * #### fitting.py - It is about a function for data fitting.
  * #### get_start.py - It deals with the contents of what you will see when you run the run file.
  * #### graph.py - The analysis results (basic, fitting, rsq) are graphically shown using matplotlib.
  * #### parsing.py - It is a file that parsing the elements necessary to draw a graph from the data.
  * #### rsq.py - It is a file that calculates the r square values of IV and ref fitting functions.
* #### .gitignore - We used the .gitignore file to prevent uploading files that the project does not need to manage or release.
* #### Run.py - It is the code that executes the projects, and it receives several options to execute the src folder.

## Usage
***
1. We carried out this project using Pycharm. In order to run this program, the user must install the pycham.
2. Open the Run.py file in the PyCharm. 
3. Write wafer or coordinates you want to analyze afterwards.
4. Choose whether to save graph or show graph.
5. The results of the analysis are in the results folder.

If you don't write down the file to analyze properly, we'll let you know with an error mark.

## Contributing
***
If you have any errors or questions while using the code.
- gowldytjq98@hanyang.ac.kr
- glen0504@hanyang.ac.kr
- realhr0805@hanyang.ac.kr