# joaquin.soler.1979@gmail.com
# Experto responsable de generar las consultas específicas para guardar los datos en la base de datos

import FachadaPersistencia as fp
import math

def guardarDF(df):

    # guardarPersonas(df.loc[:,"directors"])
    # guardarPeliculas(df)
    guardarDirectores(df)
    
    # for i, elemento in df.iterrows():
    #     consulta = getConsulta(elemento)
    #     print(consulta)

def guardarPersonas(dfPersonas):

    contador = 0
    total = len(dfPersonas)

    for persona in dfPersonas:
        print(f"Avance: {round(contador/total*100,2)} %")
        contador += 1
        listaPersonas = getRegistroLimpio(persona)
        for per in listaPersonas:
            
            if(existe(per)):
                consulta = f"INSERT INTO persons (fullname) VALUES('{per}')"                
                fp.ejecutarConsultaSinResultado(consulta)
        
def guardarPeliculas(df):

    for i, pelicula in df.iterrows():               
        
        title = pelicula.iloc[0] #title
        movie_link = pelicula.iloc[1] #movie_link
        year = pelicula.iloc[2] #year
        duration = pelicula.iloc[3] #duration
        mpa = pelicula.iloc[4] #MPA
        rating = pelicula.iloc[5] #rating
        votes = pelicula.iloc[6] #votes

        if(math.isnan(pelicula.iloc[7])):
            budget = 0
        else:
            budget = pelicula.iloc[7] #budget
        
        if(math.isnan(pelicula.iloc[8])):
            grossWorldWide = 0
        else:
            grossWorldWide = pelicula.iloc[8] #grossWordlWide
        
        if(math.isnan(pelicula.iloc[9])):
            grossUSCanada = 0
        else:
            grossUSCanada = pelicula.iloc[9] #grossUSCanada

        if(math.isnan(pelicula.iloc[10])):
            openingGrossWeek = 0
        else:
            openingGrossWeek = pelicula.iloc[10]#openingWeekGross                                                          
        
        nominations = pelicula.iloc[20] #nominations
        oscars = pelicula.iloc[21] #oscars

        consulta = getInsertPelicula(title, movie_link, year, duration, mpa, rating, votes, budget, 
                                     grossWorldWide, grossUSCanada, openingGrossWeek, nominations, oscars)              
        
        fp.ejecutarConsultaSinResultado(consulta)

def guardarDirectores(df):
    
    for i, registro in df.iterrows():
        
        tituloPelicula = registro.iloc[0] # title
        directores = getRegistroLimpio(registro.iloc[11]) # directors
        
        idPelicula = int(str(getID('movies', 'movie_id', 'title', tituloPelicula)).replace(",","").replace("[(","").replace(")]",""))
        
        for d in directores:
            idDirector = int(str(getID('persons','person_id','fullname',d)).replace(",","").replace("[(","").replace(")]",""))
            consulta = f"INSERT INTO directors (movie_id, person_id) VALUES ({idPelicula},{idDirector})"
            
            fp.ejecutarConsultaSinResultado(consulta)


def getRegistroLimpio(registro):
    return str(registro).replace("[","").replace("]","").replace("'","").split(",")

def existe(persona):
    bandera = False
    consulta = f"SELECT person_id FROM persons WHERE fullname = '{persona}'"    
    resultado = fp.ejecutarConsultaConResultado(consulta)
    if (len(resultado) == 0):
        bandera = True

    return bandera

def getID(tabla, atributoID, atributoBusqeda, valor):
    
    consulta = f"SELECT {atributoID} FROM {tabla} WHERE {atributoBusqeda} = '{valor}'"    
    
    return fp.ejecutarConsultaConResultado(consulta)

def getInsertPelicula(title, movie_link, year, duration, mpa, rating, votes, budget, gross_World_Wide, 
                      gross_US_Canada, opening_weekend_Gross, nominations, oscars):

    consulta = f"""INSERT INTO movies (title,
                                        movie_link,
                                        year,
                                        duration,
                                        mpa,
                                        rating,
                                        votes,
                                        budget,
                                        gross_World_wide,
                                        gross_US_Canada,
                                        opening_weekend_Gross,
                                        nominations,
                                        oscars
                                        )
                                        VALUES('{title}',
                                                '{movie_link}',
                                                {year},
                                                '{duration}',
                                                '{mpa}',
                                                '{rating}',
                                                '{votes}',
                                                {budget},
                                                {gross_World_Wide},
                                                {gross_US_Canada},
                                                {opening_weekend_Gross},
                                                {nominations},
                                                {oscars}
                                        )"""

    return consulta
