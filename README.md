<div align="center">

<h1>FilmCurve · CLI</h1>
    
<p>
<strong>Finds zone number for a given film density value (or vice versa).<br>
EARLY EXPERIMENTAL</strong>
</p>

</div>



## Installation · Linux

Just clone the repo and symlink it into your *bin/* directory. Make sure to have Python 2.7, [matplotlib](https://matplotlib.org/) and [numpy](http://www.numpy.org/) on your system.

```bash
$ git clone https://github.com/filmtools/filmcurve
$ ln -s ~/path/to/filmcurve/bin/filmcurve ~/bin/filmcurve
```


## Homebrew Installation · MacOS

The *curvefit* executable can be installed by a [Homebrew](https://brew.sh/) formula, which itself is part of the [filmtools/homebrew-filmtools](https://github.com/filmtools/homebrew-filmtools) tap.

```bash
# Variant 1: Install tap first, formula second
$ brew tap filmtools/filmtools
$ brew install filmcurve
```

As “tapping” first is not neccessarily needed, you can install the formula directly:

```bash
# Variant 2: Install directly
$ brew install filmtools/filmtools/filmcurve
```


## Usage · Command-line API

```bash
$ filmcurve -z Z [Z ...] -d D [D ...]
            [--density logD | --zone Zone]
            [-p P]
            [--plot file]
            [-h] 
           
# Print help text
$ filmcurve
$ filmcurve -h
$ filmcurve --help           
```

### Required Arguments

Option | Argument | Description
:------|:---------|:-----------
`-z` | list of *float* | Zone numbers (space separated), usually from 0.00 to 10.00 in 0.33 steps (1/3 f-stops)
`-d` | list of *float* | Density values (space separated), usually measured densities 'above fog'


### Mutually exclusive options

If neither *density option* nor *zone option* are passed, the script prints the polynomial coefficients and residuals.

Option | Argument | Description
:------|:-----|:-----------
`--density` | Density value *float* | Calculate *zone number* value for given density
`--zone` | Zone number *float* | Calculate *density* value for given zone number



### Other options

Option | Argument | Description
:------|:-----|:-----------
`-h` `--help`       |                 | Display help
`-p` `--precision`  | *integer* | Goal seek precision. 3=fast/fuzzy, 16=too slow and overdone. An appropriate value is 12 (default).
`--plot` | filename.png | Plot graph and save PNG to *filename*






## Examples

#### Calculate density value for given zone


```bash
$ filmcurve -z 0.00 1.00 2.00 3.00 4.00 5.00 6.00 7.00 8.00 9.00 10.00 \
            -d 0.02 0.10 0.21 0.38 0.53 0.74 0.97 1.20 1.40 1.55 1.66 \
            --zone 2.00

# Calculated density is roughly
0.215413...
```

#### Calculate zone number for given density:

```bash
$ filmcurve -z 0.00 1.00 2.00 3.00 4.00 5.00 6.00 7.00 8.00 9.00 10.00 \
            -d 0.02 0.10 0.21 0.38 0.53 0.74 0.97 1.20 1.40 1.55 1.66 \
            --density 0.38

# Calculated zone is roughly
3.119267
```

#### Display polynomial model:

```bash
$ filmcurve \
-z -0.67 -0.33 0.00 0.33 0.67 1.00 1.33 2.33 3.33 4.33 5.33 6.33 7.33 8.33 9.33 \
-d  0.00  0.01 0.02 0.03 0.02 0.10 0.12 0.28 0.49 0.73 0.99 1.22 1.43 1.62 1.75

# Output:

Coefficients:
[ 0.00002172 -0.0004268  -0.00021636  0.03797541  0.03311455  0.011047  ]
Residuals:
[ 0.00157251]

```


## Testing

Go to project directory and run `pytest`. 

```bash
$ pytest -v
```

Output should look like this:

```
=============================== test session starts ================================
platform darwin -- Python 2.7.14, pytest-3.3.1, py-1.5.2, pluggy-0.6.0 -- /usr/local/opt/python/bin/python2.7
cachedir: .cache
rootdir: /path/to/filmcurve, inifile:
collected 3 items

tests/test_filmcurve.py::TestFilmCurve::test_findOffset[8-1.29--1.63] PASSED [ 33%]
tests/test_filmcurve.py::TestFilmCurve::test_FindZone[1.29-9.63] PASSED      [ 66%]
tests/test_filmcurve.py::TestFilmCurve::test_findDensity[4.0-0.44] PASSED    [100%]

============================= 3 passed in 0.18 seconds =============================
```




## Requirements

This application requires Python's  **[matplotlib](https://matplotlib.org/)** and **[numpy](http://www.numpy.org/)** library.


## Issues + Development

Being a Python beginner, I assume the script structure can (and surely should) be improved. Any help with this will be appreciated. Feel free to PR or open an issue – head over to the [issues page.](https://github.com/filmtools/filmcurve/issues)

```bash
$ git clone https://github.com/filmtools/filmcurve
```


