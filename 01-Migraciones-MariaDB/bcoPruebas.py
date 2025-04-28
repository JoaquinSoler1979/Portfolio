import FachadaPersistencia as fp

consulta = "SELECT fullname FROM persons WHERE person_id = 1"
resultado = fp.ejecutarConsultaConResultado(consulta)
print(len(resultado))
# resultado = fp.ejecutarConsultaConResultado(consulta)

# for r in resultado:
#     print(r[1])




# # consulta = """CREATE DATABASE db"""
# # ejecutarConsultaSinResultado(consulta)

# print("creación de tablas iniciada")

# # crear tabla personas para directores
# consulta = """CREATE TABLE persons (person_id INT PRIMARY KEY AUTO_INCREMENT,
#                                     fullname VARCHAR(35)
#                                     )"""
# ejecutarConsultaSinResultado(consulta)

# # crear tabla pelicula
# # atributos: Title,	Movie Link,	Year, Duration,	MPA, Rating, Votes, budget, grossWorldWide, gross_US_Canada, opening_weekend_Gross,	nominations, oscars, release_date

# consulta = """CREATE TABLE movies (movie_id INT PRIMARY KEY AUTO_INCREMENT,
#                                     title VARCHAR(275),
#                                     movie_link VARCHAR(75),
#                                     year INT,
#                                     duration VARCHAR(8),
#                                     mpa VARCHAR(8),
#                                     rating VARCHAR(4),
#                                     votes VARCHAR(5),
#                                     budget BIGINT,
#                                     gross_World_Wide BIGINT,
#                                     gross_US_Canada BIGINT,
#                                     opening_weekend_Gross BIGINT,
#                                     nominatios SMALLINT,
#                                     oscars SMALLINT,
#                                     release_date SMALLINT
#                                     )"""
# ejecutarConsultaSinResultado(consulta)

# # creación de tabla intermedia para vincular películas con directores
# consulta = """CREATE TABLE directors (movie_id INT,
#                                     person_id INT,                                    
#                                     FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
#                                     FOREIGN KEY (person_id) REFERENCES persons(person_id)
#                                     )"""
# ejecutarConsultaSinResultado(consulta)
# print("creación de tablas finalizada")



"""
0 Title
1 Movie Link
2 Year
3 Duration
4 MPA
5 Rating
6 Votes
7 budget
8 grossWorldWide
9 gross_US_Canada
10 opening_weekend_Gross
11 directors
12 writers
13 stars
14 genres
15 countries_origin
16 filming_locations
17 production_companies
18 Languages
19 wins
20 nominations
21 oscars
22 release_date


"""