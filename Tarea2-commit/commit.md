# ¿Qué es un commit?
Es una confirmación o registro de los cambios que realizas en tu proyecto dentro del sistema de control de versiones GIT.

Cada vez que hago un commit, Git guarda:
- Qué archivos cambiaron
- Qué contenido se añadió o eliminó
- Quién hizo el cambio
- Cuándo se hizo
- Un mensaje que describe lo que se hizo

## ¿Qué es un conventional commit?
Es una convención o estándar para escribir mensajes de commit de forma clara, uniforme y automatizable.

Define un estructura específica del mensaje, para que tanto las personas como las herramientas (como GitHub Actions o semantic-release) entiendan fácilmente qué tipo de cambios se hizo.

### Sintaxis:
```php-template
<tipo>(<ámbito opcional>): <descripción breve>
```

```scss
feat(login): agrega validación de correo electrónico
```

## ¿Para qué sirve un commit?
Sirve para guardar el progreso del proyecto de forma ordenada y con historial.

Con los commits se puede:
- Guardar una versión del proyecto
	- Así se puede volver atrás si algo falla más adelante.
- Revisar el historial de cambios
	- Ver qué cambió, quién lo cambió y por qué.
- Colaborar con otros desarrolladores
	- Cada persona hacer commits de sus avances, y luego todos pueden integrarlos.
- Probar nuevas ideas sin miedo
	- Si rompo algo, puedo regresar a un commit anterior.

### Ejemplo
```bash
git add index.html # Preparo el archivo para el commit
git commit -m "Agrega sección de contacto en la página principal"
``` 
### Historial de commits
```bash
git log
```
