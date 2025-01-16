# EDA Example Notebooks

This repository is designed to serve as an introduction to the EarthDaily Platform. 

## Installation

The majority of the examples located in this repo rely on the [EarthDaily Python client](https://earthdaily.github.io/earthdaily-python-client/). Each notebook series contains a `requirements.txt` file containing packages which must be installed ahead of time. 

To begin, create a new Python virtual environment (>3.10). Once your environment is activated, install the dependencies contained in this repository with the following:

    pip install -r requirements.txt

## Authentication

In each notebook directory there is a sample `template.env` file which should be updated with your credentials. This file can be downloaded from the [EarthDaily Account Management](https://console.earthdaily.com/account) page.

    EDS_AUTH_URL="<EDS AUTH URL>"
    EDS_API_URL="https://api.earthdaily.com/platform/v1/stac"
    EDS_SECRET="<EDS SECRET>"
    EDS_CLIENT_ID="<EDS CLIENT ID>"

## Overview

A general outline of the tutorial notebooks contained in this repo is as follows:

### Basic Examples

#### EarthMosaics

* [EDA Mosaics - EarthMosaics vs Sentinel-2 NDVI.ipynb](EDA%20Mosaics%20-%20EarthMosaics%20vs%20Sentinel-2%20NDVI/EDA%20Mosaics%20-%20EarthMosaics%20vs%20Sentinel-2%20NDVI.ipynb)
* [EDA Mosaics - Dixie Fire Burn Extent.ipynb](EDA%20Mosaics%20-%20Dixie%20Fire%20Burn%20Extent/EDA%20Mosaics%20-%20Dixie%20Fire%20Burn%20Extent.ipynb)
* [EDA Mosaics - Rio Grande do Sul Flood Extent.ipynb](EDA%20Mosaics%20-%20Rio%20Grande%20do%20Sul%20Flood%20Extent/EDA%20Mosaics%20-%20Rio%20Grande%20do%20Sul%20Flood%20Extent.ipynb)