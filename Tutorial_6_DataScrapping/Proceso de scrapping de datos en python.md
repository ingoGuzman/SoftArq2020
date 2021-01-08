# Proceso de scrapping de datos en python
Utilizando python 3 crearemos un programa que pueda obtener datos de una página en linea (Wikipedia) y luego los almacene de manera ordenada.  
## Parte 1: Requests
Vamos a utilizar python 3, y para generar nuestras __Http requests__ vamos a utilizar la librería Requests  

    $ pip3 install requests
    $ touch mockup.py

Dentro de nuestro *mockup.py* intentaremos enviar nuestra request (e imprimir el resultado para comprobar)  

    import requests
    
    response = requests.get(
    	url="https://es.wikipedia.org/wiki/Python",
    )
    
    print(response.status_code)

Si al ejecutar nuestro código nos retorna un valor de "200" sabremos que el servidor recive nuestra petición y la responde de manera correcta.  

## Parte 2: Manejo de datos  
Ya teniendo una respuesta postiva ahora debemos tener claro como son recibidos nuestros datos, para poder trabajarlo de forma cómoda. Si editamos nuestro código e imprimimos 

    print(response.content)

Podemos observar que el contenido es html, esta sopa de datos sería muy dificil de manejar. Para alivianar el proceso vamos a recurrir a BeutifulSoup:  

    $pip3 install beautifulsoup4

Esta libreria nos permite crear un objeto el cual podemos manejar de manera más cómoda (principalmente, nos permite buscar elementos por su _id_ de html). Juntando las partes nuestro código se vería así

    import requests
    from bs4 import BeautifulSoup
    
    response = requests.get(
    	url="https://es.wikipedia.org/wiki/Python",
    )
    content = BeautifulSoup(response.content, 'html.parser')
    
    title = content.find(id="firstHeading")
    print(title.string)

Ya tenemos listo nuestro código para navegar wikipedia y conseguir el titulo de nuestro articulo. Uno de los usos más comunes del scrapping es la obtención de enlaces. Vamos a modificar el código para obtener todos los articulos de wikipedia que estén enlazados en el articulo base. (Nota: cada sitio organiza su información de manera distinta y es nuestra labor configurar la lógica de manera acorde)  

    links=[]
    for link in content.find(id="bodyContent").find_all('a'):
    	if not (link.has_attr('class')):
    		if (link.has_attr('title')):
    			links.append(link)
    
    for link in links:
    	print(link['title'])

De esta forma obtenemos una lista de links, mostrando sus titulos en pantalla, que están relacionados a nuestro artículo. Vamos entonces a modificar nuestro código en preparación para el proximo paso:

    import requests
    from bs4 import BeautifulSoup
    
    response = requests.get(
    	url="https://es.wikipedia.org/wiki/Python",
    )
    content = BeautifulSoup(response.content, 'html.parser')
    
    title = content.find(id="firstHeading")
    
    links=[]
    for link in content.find(id="bodyContent").find_all('a'):
    	if not (link.has_attr('class')):
    		if (link.has_attr('title')):
    			links.append(link)
    
    ##for link in links:
    ##	print(link['title'])
    
    print(title.string+": "+content.find(id="mw-content-text").p.text)

## Parte 3: Autonomous scrapping
Podemos obtener información de wikipedia, y podemos obtener más links para explorar: es momento de juntar las partes y hacer un poco de _scrapping autonomo_; Ya que nuestro código está recibiendo esta información como texto incluirla en una base de datos es, en teoría, relativamente simple. En honor al espacio no lo implementaremos aún.  
Nuestro primer paso será mover el código a funciones que se puedan utilizar más facilmente desde programas externos.  

    import requests
    from bs4 import BeautifulSoup
    import time
    
    def wikiScrap(url):
    	response = requests.get(url)
    	content = BeautifulSoup(response.content, 'html.parser')
    
    	title = content.find(id="firstHeading")
    
    	links=[]
    	for link in content.find(id="bodyContent").find_all('a'):
    		if not (link.has_attr('class')):
    			if (link.has_attr('title')):
    				links.append(link)
    
    	print(title.string+": "+content.find(id="mw-content-text").p.text)
    
    	time.sleep(20)
    	print(links[0]['title'])
    	wikiScrap("https://es.wikipedia.org"+links[0]['href'])
    
    wikiScrap("https://es.wikipedia.org/wiki/Python")

Aqui hemos tomado siempre el primer enlace y hemos vuelto a correr la función entregandolo como argumento. Con solo correr el código unos minutos podemos ver que los enlaces se desvian de artículos a otro tipo de enlaces (lo cuál nos indica la imprecisión de nuestra lógica para seleccionarlos), pero por otro lado, nos indica que nuestro método autónomo funciona.
## Parte 4: Integraciones
Ahora vamos a modificar el código en función de nuetros output esperados. También moveremos el scrapping autonomo a su propia sección.

    import requests
    from bs4 import BeautifulSoup
    import time
    
    def wikiSet(url):
    	response = requests.get(url)
    	content = BeautifulSoup(response.content, 'html.parser')
    	return (content)
    
    def wikiLinks(url):
    	soup = wikiSet(url)
    	links=[]
    	for link in soup.find(id="bodyContent").find_all(linkLogic):
    		links.append(link)
    	return(links)
    
    def linkLogic(tag):
    	return tag.has_attr('title') and not tag.has_attr('class')
    
    def wikiDef(url,n):
    	soup = wikiSet(url)
    	title = soup.find(id="firstHeading")
    	text = soup.find(id="mw-content-text").find_all("p",limit=n)
    	fullText = ""
    	for p in text:
    		fullText = fullText + "\n"+p.text
    	print(title.string+": "+ fullText)
    	return(True)
    
    def autoScrap(url):
    	links = wikiLinks(url)
    	print(links[0]['title'])
    	time.sleep(5)
    	autoScrap("https://es.wikipedia.org"+links[0]['href'])
    
    wikiDef("https://es.wikipedia.org/wiki/Python",2)
    autoScrap("https://es.wikipedia.org/wiki/Python")

En este código de ejemplo nuestro autoScrap solo colecta links para moverse por el primero que vaya encontrando, pero es escalable a cualquiera sea nuestra necesidad.