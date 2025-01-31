# EDA Example Notebooks

This repository is designed to serve as an introduction to the EarthDaily Platform. 

> **_NOTE:_** To gain access to the Earth Data Store data referenced in this repo, please [create an EarthDaily account](https://console.earthdaily.com/mosaics/signup)

## Installation

The majority of the examples located in this repo rely on the [EarthDaily Python client](https://earthdaily.github.io/earthdaily-python-client/). Each notebook series contains a `requirements.txt` file containing packages which must be installed ahead of time. 

To begin, create a new Python virtual environment >3.10 and activate it, we recommend using [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Once your environment is activated, install the dependencies contained in this repository with the following:

    pip install -r requirements.txt

> **_NOTE:_**  For detailed environment management instructions, refer to the [Virtual Environment Setup Instructions](#virtual-environment-setup-instructions)

## Authentication

In each notebook directory there is a sample `template.env` file which should be updated with your credentials. This file can be downloaded from the [EarthDaily Account Management](https://console.earthdaily.com/account) page.

    EDS_AUTH_URL="<EDS AUTH URL>"
    EDS_API_URL="https://api.earthdaily.com/platform/v1/stac"
    EDS_SECRET="<EDS SECRET>"
    EDS_CLIENT_ID="<EDS CLIENT ID>"

## Overview

A general outline of the tutorial notebooks contained in this repo is as follows:

### Basic Examples

* [Getting Started with EarthDaily.ipynb](Getting%20Started%20with%20EarthDaily/Getting%20Started%20with%20EarthDaily.ipynb)

### EarthMosaics

* [Introduction to EDA EarthMosaics.ipynb](Introduction%20to%20EDA%20EarthMosaics/Introduction%20to%20EDA%20EarthMosaics.ipynb)
* [EDA Mosaics - EarthMosaics vs Sentinel-2 NDVI.ipynb](EDA%20Mosaics%20-%20EarthMosaics%20vs%20Sentinel-2%20NDVI/EDA%20Mosaics%20-%20EarthMosaics%20vs%20Sentinel-2%20NDVI.ipynb)
* [EDA Mosaics - Dixie Fire Burn Extent.ipynb](EDA%20Mosaics%20-%20Dixie%20Fire%20Burn%20Extent/EDA%20Mosaics%20-%20Dixie%20Fire%20Burn%20Extent.ipynb)
* [EDA Mosaics - Rio Grande do Sul Flood Extent.ipynb](EDA%20Mosaics%20-%20Rio%20Grande%20do%20Sul%20Flood%20Extent/EDA%20Mosaics%20-%20Rio%20Grande%20do%20Sul%20Flood%20Extent.ipynb)

## Appendix

### Virtual Environment Setup Instructions
#### Windows - Anaconda and Miniconda
The following are steps to set up a new Conda environment and set up the EarthDaily Python Client:
1. Download and run the .exe located at the [Anaconda Downloads page](https://www.anaconda.com/download/success)
2. Open the Anaconda Prompt
3. Create a new virtual environment by running the following in your Terminal:

        conda create -n earthdaily jupyter

4. Active your new virtual environment by running the following in your Terminal:

        conda activate earthdaily

5. Install [earthdaily](https://pypi.org/project/earthdaily/) by running the following in your Terminal:

        pip install earthdaily

6. Install the [EarthDaily Example Notebooks](https://github.com/earthdaily/Example-Notebooks) by running the following in your Terminal:

        git clone https://github.com/earthdaily/Example-Notebooks.git

7. Initialize the Jupyter Lab client by running the following in your Terminal:

        jupyter lab

8. Navigate to the newly cloned Example Notebooks folder
