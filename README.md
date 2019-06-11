Doing this https://machinelearningmastery.com/linear-algebra-machine-learning-7-day-mini-course/

For more material

- https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/syllabus/
  - https://www.youtube.com/watch?v=hNDFwVVKVk0&list=PL221E2BBF13BECF6C
  - https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/ax-b-and-the-four-subspaces/the-geometry-of-linear-equations/2
    - fundamental problem of linear algebra is to solve a system of linear equations
    - linear combination is the most fundamental in thw whole course
    - https://en.m.wikipedia.org/wiki/Coefficient_matrix
    - singular - if not vectors are not independent - they are combinations of others?
  - https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/ax-b-and-the-four-subspaces/an-overview-of-key-ideas/
    - anybody who computes, who's living in the real world, is using linear algebra. You're taking a
differential equation, you're taking your model, making it discrete and computing with matrices.
The world's digital now, not analog.
- https://www.khanacademy.org/math/linear-algebra/
  - https://pl.khanacademy.org/math/algebra-home
- https://www.khanacademy.org/math/algebra-home/alg-vectors
- https://www.khanacademy.org/math/algebra-home/alg-matrices
- https://www.khanacademy.org/math/algebra-home/alg-matrices/alg-matrices-as-transformations/a/matrices-as-transformations
  - College (University) age 18-22 https://en.m.wikipedia.org/wiki/Education_in_the_United_States#Educational_stages


## Anaconda vs PyPi vs Docker

For now I am just doing:

`pip3 install scipy numpy matplotlib pandas statsmodels sklearn`

- https://machinelearningmastery.com/setup-python-environment-machine-learning-deep-learning-anaconda/

>I'm really pleased that PyPI is satisfying your needs now but your numpy and scipy would run faster if you installed our packages due to using MKL. (Intel Math Kernel Library)
>
>Do you mean relative to PyPI? Well, those packages are uploaded in an ad-hoc basis by the maintainers and many packages are not available for Python 3.7 yet whereas every package in Anaconda Distribution is availble for Python 3.7.
>
>Anaconda Distribution packages are often also a *lot* less resource hungry (memory, disk space) than those from PyPI because on PyPI if you want to use modern C++ in your extension module you end up statically linking to libstdc++ (or else you run into ABI issues). This means every C++ extension module you have will be pull in parts of the static code in libstdc++ leading to a large amount of duplication. We share a single libstdc++ with all packages so the text (code segments) get loaded in only once.
>
>conda's dynamic environment feature (far superior to venv) isn't a good fit for a *single file association*.
>- https://www.reddit.com/r/Python/comments/9q1nxp/anaconda_worth_it/

>These days I just use normal Python for Linux inside a Docker container - everything works easily regardless of what the host OS is. Normal Pip + Pypi is good enough.
>- https://www.reddit.com/r/Python/comments/aima0t/are_there_any_advantages_to_installing_anaconda/eeq6wfe/
>- https://towardsdatascience.com/a-short-guide-to-using-docker-for-your-data-science-environment-912617b3603e

>it has upto 720 open source packages, most of which are not in the pip repo?
>- https://www.quora.com/Why-should-I-use-anaconda-instead-of-traditional-Python-distributions-for-data-science/answer/Nwoko-Uzoma-Jerem

- https://askubuntu.com/questions/505919/how-to-install-anaconda-on-ubuntu
- https://stackoverflow.com/questions/42096280/how-is-anaconda-related-to-python

## Anaconda vs Miniconda

>If you want to used Anaconda Distribution in a non-learner scenario, use Miniconda and minimal, isolated environments. You'll find Python spending a lot less time scanning site-packages that way.
>- https://www.reddit.com/r/Python/comments/9q1nxp/anaconda_worth_it/

- https://stackoverflow.com/questions/45421163/anaconda-vs-miniconda

## venv

>Personally, I prefer to keep strict control of my environments, so use Python venv for each project and install only the packages I need. https://realpython.com/python-virtual-environments-a-primer/
>- https://www.reddit.com/r/learnpython/comments/ayjg0m/anaconda_or_plain_python/

## Python and packages usage

- https://www.tutorialspoint.com/python/python_functions.htm
- https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
- https://docs.python.org/3/tutorial/datastructures.html
- https://stackoverflow.com/questions/52450877/python-for-loop-iterate-array
- https://likegeeks.com/numpy-array-tutorial/
- https://stackoverflow.com/questions/5064822/how-to-add-items-into-a-numpy-array
- https://stackoverflow.com/questions/45123559/printing-return-value-in-function
- https://stackoverflow.com/questions/6967463/iterating-over-a-numpy-array/6967491#6967491
  - https://stackoverflow.com/questions/42082607/iterate-over-numpy-with-index-numpy-equivalent-of-python-enumerate/42082685#42082685
  - https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndenumerate.html
- https://stackoverflow.com/questions/25129195/how-to-access-an-element-in-a-numpy-array/25230173#25230173

## vector dot product

- https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/dot-cross-products/v/vector-dot-product-and-vector-length
- https://www.mathsisfun.com/algebra/vectors-dot-product.html
