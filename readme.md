# Data
A tool that examines price evolution of real estate in the city of Lyon from 2014 to 2018
### Collectig Data :
Fetching data from https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/
### Cleaning Data :
Deleting extreme value corresponding to lots 
### Analyzing Data :
Create a new dataset with relevant to study price evolution
### Adding new features :
API for price

# Folium
- import Folium
- create a base map by adding the starting coordinates
- save *index.html*


# The Project
## the context and objectifs :
- Using real estate values from an open data ressource
- Visualisation of the data
- Understanding the results
- Creating an API

## Goal :
- Visualizing the evolution of Real Estate prices by borough from 2014 through 2018
- Using markers to showcase yearly data for each borough

### Using open data, step-by-step :
- Sorting through the csv file and keeping only the necessary info
- Deleting unused data
- Calculating the prices by square meter for each borough

### DataViz :
- Use of Folium library
- Dividing each borough 
- Color to show case price evolution

### Understanding the results :
- The buroughs that were "pricier" before continued to get pricier

### The API :
- Input : Lattitude and Longitude of a specific place
- Output : borough + evolution of prices in %  by sqaure meter (2014-2018)
