# Generate diff
[![Actions Status](https://github.com/spikers-dev/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/spikers-dev/python-project-lvl2/actions)
[![githab-actions](https://github.com/spikers-dev/python-project-lvl2/actions/workflows/githab-actions.yml/badge.svg)](https://github.com/spikers-dev/python-project-lvl2/actions/workflows/githab-actions.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/74cccfb87108bb373e9a/maintainability)](https://codeclimate.com/github/spikers-dev/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/74cccfb87108bb373e9a/test_coverage)](https://codeclimate.com/github/spikers-dev/python-project-lvl2/test_coverage)

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
gendiff file1.json file2.json
```
<a href="https://asciinema.org/a/0tTIzalLSCeqshJA5YbGpvPzK" target="_blank"><img src="https://asciinema.org/a/0tTIzalLSCeqshJA5YbGpvPzK.svg" /></a>

## Comparing flat YAML files

```bash
gendiff file1.yaml file2.yaml
```
<a href="https://asciinema.org/a/Bcv7NGDCBeVrpuaE7dbfaInrF" target="_blank"><img src="https://asciinema.org/a/Bcv7NGDCBeVrpuaE7dbfaInrF.svg" /></a>