import pandas as pd
import sqlite3


conn1 = sqlite3.connect('planets.db')


all_planets = pd.read_sql("""SELECT * FROM planets; """, conn1)


df_no_moons = pd.read_sql("""SELECT name, rings FROM planets WHERE num_of_moons = 0;""", conn1)


df_name_seven = pd.read_sql("""SELECT name, mass FROM planets WHERE length(name) = 7;""", conn1)


df_mass = pd.read_sql("""SELECT name, mass FROM planets WHERE mass <= 1.0;""", conn1)


df_mass_moon = pd.read_sql("""SELECT * FROM planets WHERE mass <= 1.0 AND num_of_moons > 1;""", conn1)

df_blue = pd.read_sql("""SELECT name, color FROM planets WHERE color LIKE "%blue";""", conn1)

conn2 = sqlite3.connect('dogs.db')


all_dogs = pd.read_sql("SELECT * FROM dogs;", conn2)


df_hungry = pd.read_sql("SELECT name, age, breed FROM dogs WHERE hungry = 1 ORDER BY age;", conn2)


df_hungry_ages = pd.read_sql("SELECT name, age, hungry FROM dogs WHERE hungry = 1 AND age BETWEEN 2  AND 7 ORDER BY name;", conn2)


df_4_oldest = pd.read_sql("SELECT name, age, breed FROM dogs ORDER BY age DESC;", conn2).head(4)



conn3 = sqlite3.connect('babe_ruth.db')

# Select all
babe_ruth_stats_all = pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)



df_ruth_years = pd.read_sql("""
SELECT Count(*) FROM babe_ruth_stats; """, conn3)


df_hr_total = pd.read_sql("""
SELECT SUM(hr) FROM babe_ruth_stats; """, conn3)


df_teams_years =  pd.read_sql("""
SELECT team, COUNT(year) AS number_years FROM babe_ruth_stats GROUP BY team; """, conn3)



df_at_bats =  pd.read_sql("""
SELECT team, AVG(at_bats) AS average_at_bats FROM babe_ruth_stats GROUP BY team ORDER BY team DESC; """, conn3)



conn1.close()
conn2.close()
conn3.close()