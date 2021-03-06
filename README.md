# Get Fedora Releases action

This action queries Fedora for the list of stable and in-development release versions and sets the output variables
`stable` and `development` with the provided list.

## Inputs

This action takes no input

## Outputs

### `stable`

A list of Fedora release numbers that are currently receiving updates.

### `development`
A list of Fedora release numbers that are currently in-development and may be unstable.

### `active`
The combined list of both `stable` and `development` releases.

## Example usage
```
name: Continuous Integration

on: [push, pull_request]

jobs:
  get_fedora_releases:
    name: Get Fedora Releases
    runs-on: ubuntu-latest
    steps:
      - name: Query Fedora
        id: releases
        uses: sgallagher/get-fedora-releases-action@v1
    outputs:
      stable: ${{ steps.releases.outputs.stable }}
      development: ${{ steps.releases.outputs.development }}
      active: ${{ steps.releases.outputs.active }}

  unit_tests_fedora_stable:
    name: Unit Tests (Stable Fedora)
    needs: get_fedora_releases
    runs-on: ubuntu-latest
    continue-on-error: false
    strategy:
      matrix:
        release: ${{ fromJson(needs.get_fedora_releases.outputs.stable) }}
    container:
      image: quay.io/fedora/fedora:${{ matrix.release }}-x86_64
     steps:
       - name: Run the tests
         run: echo "running tests"

  unit_tests_fedora_devel:
    name: Unit Tests (Devel Fedora)
    needs: get_fedora_releases
    runs-on: ubuntu-latest
    continue-on-error: false
    strategy:
      matrix:
        release: ${{ fromJson(needs.get_fedora_releases.outputs.development) }}
    container:
      image: quay.io/fedora/fedora:${{ matrix.release }}-x86_64
     steps:
       - name: Run the tests
         run: echo "running tests"

  unit_tests_fedora_all:
    name: Unit Tests (Active Fedora)
    needs: get_fedora_releases
    runs-on: ubuntu-latest
    continue-on-error: false
    strategy:
      matrix:
        release: ${{ fromJson(needs.get_fedora_releases.outputs.active) }}
    container:
      image: quay.io/fedora/fedora:${{ matrix.release }}-x86_64
     steps:
       - name: Run the tests
         run: echo "running tests"
```
