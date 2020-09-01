<<<<<<< HEAD
# Python Regex

¿Qué son?:  (Python Regular expresions) Las expresiones regulares son patrones de coincidencia de texto descritos con una sintaxis formal, lenguajes de programación como python admiten expresiones regulares a través de bibliotecas de extensión como por ejemplo la biblioteca re de python


¿Cómo se usan?: Las expresiones regulares se usan normalmente en aplicaciones que implican procesamiento de una gran cantidad de texto por ejemplo se usan comunmente como patrones de búsqueda. 

### Cuáles son sus principales funciones y métodos?: 
* La función search() toma un patrón y el texto a escanear y devuelve un objeto match los métodos start() y end() dan los índices a la cadena que muestra dónde se produce el texto que coincide con el patrón. 
* La función compile() convierte una cadena de expresión en un RegexObject
* La función findall()  devuelve todas las subcadenas de la entrada que coinciden con el patrón sin superposición 
* La función finditer() devuelve in iterador que produce instancias Match en lugar de las cadenas devueltas por findall()


### Listado de las reglas de utilizaión(+,^,etc):    
* "." Se interpreta como cualquier carácter sin incluir el salto de línea 
* "^" Hace match con el inicio de un string inmediatamente después una nueva línea
* "$" Hace match con el final de de una línea inmediatamente después de una nueva línea
* "*" Significa  0 o muchas veces
* "+" Significa 1 o muchas veces
* "?" Significa 0 o 1 vez
* "|" significa o y da la opción d ehacer match con dos opciones 
=======
#Python Regex
¿Qué son?:  (Python Regular expresions) Las expresiones regulares son patrones de coincidencia de texto descritos con una sintaxis formal, lenguajes de programación como python admiten expresiones regulares a través de bibliotecas de extensión como por ejemplo la biblioteca re de python
¿Cómo se usan?: Las expresiones regulares se usan normalmente en aplicaciones que implican procesamiento de una gran cantidad de texto por ejemplo se usan comunmente como patrones de búsqueda. 
Cuáles son sus principales funciones y métodos?: 
La función search() toma un patrón y el texto a escanear y devuelve un objeto match los métodos start() y end() dan los índices a la cadena que muestra dónde se produce el texto que coincide con el patrón. 
La función compile() convierte una cadena de expresión en un RegexObject
La función findall()  devuelve todas las subcadenas de la entrada que coinciden con el patrón sin superposición 
La función finditer() devuelve in iterador que produce instancias Match en lugar de las cadenas devueltas por findall()
Listado de las reglas de utilizaión(+,^,etc):    
"." Se interpreta como cualquier carácter sin incluir el salto de línea 
"^" Hace match con el inicio de un string inmediatamente después una nueva línea
"$" Hace match con el final de de una línea inmediatamente después de una nueva línea
"*" Significa  0 o muchas veces
"+" Significa 1 o muchas veces
"?" Significa 0 o 1 vez
"|" significa o y da la opción d ehacer match con dos opciones 
>>>>>>> 05d9b19493aba2ea8be0313d49e779f5199699db
