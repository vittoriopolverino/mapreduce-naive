## MapReduce Word Count
A naive implementation to better understand the **MapReduce** paradigm.

<br />

## 📜 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

<br />

## 🧐 About <a name = "about"></a>
MapReduce is a programming model for processing and generating big data sets with a parallel, distributed algorithm on a cluster.
The "MapReduce System" is usually composed of three functions (or steps):
- **Map**: The map function, also referred to as the map task, processes a single key/value input pair and produces a set of intermediate key/value pairs.
- **Shuffle**: The shuffle function transfer data from Mapper to Reducer. It is a mandatory operation for reducers to proceed their jobs further as the shuffling process serves as input for the reduce tasks.
- **Reduce**: The reduce function, also referred to as the reduce task, consists of taking all key/value pairs produced in the map phase that share the same intermediate key and producing zero, one, or more data items.

<br />

## 🏁 Getting Started <a name = "getting_started"></a>

Use the Pipfile to install packages in the virtualenv:

```
pipenv install
pipenv install --dev
```

<br />

## 💻 Usage <a name="usage"></a>
Run the MapReduce example:
```
pipenv run wordcount
```

<br />

## 🐛 Test <a name = "deployment"></a>
Run Unit and Integration tests
```
pipenv run test
```

<br />

## ⛏️ Built Using <a name = "built_using"></a>
- [Python](https://www.python.org/) | Programming language
- [Pipenv](https://pipenv.pypa.io/en/latest/) | Virtualenv and  packaging
- [Pytest](https://docs.pytest.org/en/7.1.x/) | Testing
- [Pre-Commit]() | Managing and maintaining hooks
- [Github Actions](https://github.com/features/actions) | CI/CD
- [clean-text](https://github.com/jfilter/clean-text) | Text data cleaning

<br />

## ✏️ Authors <a name = "authors"></a>
- Made with ❤️  by [@vittoriopolverino](https://github.com/vittoriopolverino)
️ 