# Integración de un módulo React
## Paso 1: Preparación
React es un "módulo" de javascript que podemos fácilmente implementar en nuestras páginas. Al funcionar de forma modal podemos utilizar solo el React que necesitemos, pero de querer crear una página o aplicacion completamente en este lenguaje, también podriamos.  
Para este ejempo vamos a incrustar un segmento de React en una página de prueba. Vamos para esto a crear un documento html de prueba (el cual conseguimos en internet).

    <!-- Prueba.html -->
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Page Title</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="estilos.css">
      </head>
      <body>
        <div class="header">
          <h1>My Website</h1>
        </div>
        <div class="row">
          <div class="main">
            <h2>TITLE HEADING</h2>
            <h5>Title description, Dec 7, 2017</h5>
            <div class="fakeimg" style="height:200px;">Image</div>
            <p>Some text..</p>
            <p>Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p>
          </div>
        </div>
        <div class="footer">
          <h2>Footer</h2>
        </div>
      </body>
    </html>

Crearemos también un archivo para darle estilo a la página  

    /* estilos.css */
    * {
      < box-sizing: border-box;
    }
    body {
      font-family: Arial, Helvetica, sans-serif;
      margin: 0;
    }
    .header {
      padding: 80px;
      text-align: center;
      background: #1abc9c;
      color: white;
    }
    .header h1 {
      font-size: 40px;
    }
    .row {
      display: -ms-flexbox;
      /* IE10 */
      display: flex;
      -ms-flex-wrap: wrap;
      /* IE10 */
      flex-wrap: wrap;
    }
    /* Main column */
    .main {
      -ms-flex: 70%;
      /* IE10 */
      flex: 70%;
      background-color: white;
      padding: 20px;
    }
    
    /* Fake image, just for this example */
    .fakeimg {
      background-color: #aaa;
      width: 100%;
      padding: 20px;
    }
    
    /* Footer */
    .footer {
      padding: 20px;
      text-align: center;
      background: #ddd;
    }
    @media screen and (max-width: 700px) {
      .row {
        flex-direction: column;
      }
    }

Guardamos ambos archivos en la misma carpeta y al abrir el html en nuestro navegador ya podremos ver una página con un bloque (actualmente una imagen) perfecto para reemplazar.  

## Paso 2: React
Nuestro siguiente paso será integrar React a este documento html. Lo primero que haremos será definir nuestro contenedor, y darle una ID específica; Para esto tomaremos la imagen central y editaremos su código:  

    <div class="fakeimg" id="reactDiv" style="height:200px;">Image</div>

Ahora vamos a incluir 3 etiquetas **script** antes de cerrar la etiqueta **body**  

        <div class="footer">
          <h2>Footer</h2>
        </div>
        <!-- Cargamos React -->
        <script src="https://unpkg.com/react@17/umd/react.development.js" crossorigin></script>
        <script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js" crossorigin></script>
    
        <!-- Cargamos nuestro componente de React. -->
        <script src="test_component.js"></script>
      </body>

## Paso 3: El componente
Ahora toca escribir nuestro componente React, en este ejemplo lo llamaremos ***test_component.js***

    //test_component.js
    'use strict';

    const e = React.createElement;
    
    class LikeButton extends React.Component {
      constructor(props) {
        super(props);
      }
    
      render() {
        return 'Hello World';
      }
    }
    const domContainer = document.querySelector('#reactDiv');
    ReactDOM.render(e(LikeButton), domContainer);

Incluimos este código en la misma carpeta que los otros dos y al recargar la página ya veremos como nuestro componente reemplaza el contenido.  

## Paso 4: Reacción
Nuestro ejemplo ya funcióna, ahora debemos incluir un par de conceptos más interesantes. La gracia de React es que sea "Reactivo", así que vamos a incluir un par de botones.  
Vamos a editar nuestra función de react de la siguiente forma:

    //test_component.js
    'use strict';
    const e = React.createElement;
    class SayHi extends React.Component {
      constructor(props) {
        super(props);
        this.state = { clicked: false };
      }
      render() {
        if (this.state.clicked) {
          return 'Hello World';
        }
        return e(
          'button',
          { onClick: () => this.setState({ clicked: true }),
          class:'reactBtn' },
          'Saludar'
        );
      }
    }
    const domContainer = document.querySelector('#reactDiv');
    ReactDOM.render(e(SayHi), domContainer);

De esta misma forma podemos ampiar la funcionalidad de varias formas.