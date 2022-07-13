# Generate diff
[![Actions Status](https://github.com/spikers-dev/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/spikers-dev/python-project-lvl2/actions)
[![githab-actions](https://github.com/spikers-dev/python-project-lvl2/actions/workflows/githab-actions.yml/badge.svg)](https://github.com/spikers-dev/python-project-lvl2/actions/workflows/githab-actions.yml)
<a href="https://codeclimate.com/github/spikers-dev/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/74cccfb87108bb373e9a/maintainability" /></a>
<a href="https://codeclimate.com/github/spikers-dev/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/74cccfb87108bb373e9a/test_coverage" /></a>

Gendiff is a CLI utility for finding differences between configuration files.

## Features

- Suppported formats: YAML, JSON
- Report generation as plain text, structured text or JSON
- Can be used as CLI tool or external library

gendiff --help
usage: gendiff [-h] [-f FORMAT] first_file second_file
<a href="https://asciinema.org/a/ReLvLxZwXWADSWvHicrvXNlVv" target="_blank"><img src="https://asciinema.org/a/ReLvLxZwXWADSWvHicrvXNlVv.svg" /></a>

## Comparing flat JSON files

```bash
gendiff simple_before.json simple_after.json
```
<a href="https://asciinema.org/a/0tTIzalLSCeqshJA5YbGpvPzK" target="_blank"><img src="https://asciinema.org/a/0tTIzalLSCeqshJA5YbGpvPzK.svg" /></a>
