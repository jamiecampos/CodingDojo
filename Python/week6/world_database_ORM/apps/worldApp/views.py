from django.shortcuts import render
from . import models
from django.db.models import Count
# Create your views here.
def index(req):

# 1. What query would you run to get all the countries that speak Slovene? Your
# query should return the name of the country, language and language percentage.
# Your query should arrange the result by language percentage in descending order.
    countries = models.Countries.objects.filter(languagetocountry__language='slovene')

# 2. What query would you run to display the total number of cities for each country?
# Your query should return the name of the country and the total number of cities.
# You query should arrange the result by the number of cities in descending order.
    # countries = models.Cities.objects.raw('SELECT cities.id, countries.name, COUNT(cities.id) AS count FROM cities JOIN countries ON country_code = countries.code GROUP BY countries.name ORDER BY count DESC')

# 3. What query would you run to get all the cities in Mexico with a population of greater
# than 500,000? Your query should arrange the result by population in descending order.
    # cities = models.Cities.objects.filter(country__name='Mexico').filter(population__gt=500000).order_by('-population')

# 4. What query would you run to get all languages in each country with a percentage greater
# than 89%? Your query should arrange the result by percentage in descending order.
    # languages = models.Languages.objects.filter(percentage__gt=89).order_by('-percentage')

# 5. What query would you run to get all the countries with Surface Area below 501 and
# Population greater than 100,000?
    # countries = models.Countries.objects.filter(surface_area__lte=501).filter(population__gte=100000)

# 6. What query would you run to get countries with only Constitutional Monarchy with a
# capital greater than 200 and a life expectancy greater than 75 years?
    # countries = models.Countries.objects.filter(government_form='Constitutional Monarchy').filter(capital__gt=200).filter(life_expectancy__gt=75)

# 7. What query would you run to get all the cities of Argentina inside the Buenos Aires
# district and have the population greater than 500,000? The query should return the
# Country Name, City Name, District and Population.
    # cities = models.Cities.objects.filter(country__name='Argentina').filter(district="Buenos Aires").filter(population__gt=500000)

# 8. What query would you run to summarize the number of countries in each region? The
# query should display the name of the region and the number of countries. Also, the
# query should arrange the result by the number of countries in descending order.
    # regions = models.Countries.objects.raw('SELECT id, region, COUNT(id) AS count FROM countries GROUP BY region ORDER BY count DESC')

    # For questions 1, 2, 5, 6
    return render(req, 'worldApp/index.html', context={'countries':countries})

    # For question 2, 3, 7
    # return render(req, 'worldApp/index.html', context={'cities':cities})

    # For question 4
    # return render(req, 'worldApp/index.html', context={'languages':languages})

    # # For question 8
    # return render(req, 'worldApp/index.html', context={'regions':regions})
