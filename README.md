# Gendiff (difference calculator)
[![Actions Status](https://github.com/isbushcar/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/isbushcar/python-project-lvl2/actions)
[![pytest](https://github.com/isbushcar/python-project-lvl2/actions/workflows/pytest.yml/badge.svg)](https://github.com/isbushcar/python-project-lvl2/actions/workflows/pytest.yml)
[![wemake-python](https://github.com/isbushcar/python-project-lvl2/actions/workflows/wemake-python.yml/badge.svg)](https://github.com/isbushcar/python-project-lvl2/actions/workflows/wemake-python.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/88fbecc42c307d673118/maintainability)](https://codeclimate.com/github/isbushcar/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/88fbecc42c307d673118/test_coverage)](https://codeclimate.com/github/isbushcar/python-project-lvl2/test_coverage)
## Description
Gendiff compares two .json or .yaml files, prints and returns a difference between them.
Could be used as python package or command-line utility.
## Installing (requires Poetry)
1. Clone repository: `git clone https://github.com/isbushcar/python-project-lvl2.git`
2. Go to directory python-project-lvl2 `cd python-project-lvl2`
3. Use command `poetry build`
4. Use command `python3 -m pip install --user dist/*.whl` or `make install`
5. You are breathtaking!
## How to use
`gendiff [options] <File1> <File2>`

Available options:

`-f, --format [type]` Output format: stylish (default), plain or json

`-h, --help` output usage information
## Examples

'Flat' .json files diff:
[![asciicast](https://asciinema.org/a/Wl54v2Rjfa07tkMPjcHwlnAEf.svg)](https://asciinema.org/a/Wl54v2Rjfa07tkMPjcHwlnAEf)
'Flat' .yaml files diff:
[![asciicast](https://asciinema.org/a/5pR9klbkTrdkb7mvXHewkElTc.svg)](https://asciinema.org/a/5pR9klbkTrdkb7mvXHewkElTc)
'Recursive' files diff ('stylish'):
[![asciicast](https://asciinema.org/a/7rQzprhkmiaLYXa5ICCbsV0Jm.svg)](https://asciinema.org/a/7rQzprhkmiaLYXa5ICCbsV0Jm)
'Recursive' files diff ('plain'):
[![asciicast](https://asciinema.org/a/aKjQqiaB5zGywVKdHf39RK2cv.svg)](https://asciinema.org/a/aKjQqiaB5zGywVKdHf39RK2cv)
'Recursive' files diff (.json):
[![asciicast](https://asciinema.org/a/t8IgkXKH3DBKpVTzG7S7U8MT4.svg)](https://asciinema.org/a/t8IgkXKH3DBKpVTzG7S7U8MT4)
