# Git y Github

[**<-- VOLVER AL INICIO**](/README.md)

![Alt Text](https://git-scm.com/downloads/logos)

## 1: Instalar Git localmente

Instalar Git en tu computadora.

Puedes descargarlo desde el [sitio oficial de Git](https://git-scm.com/) y seguir las [instrucciones de instalación](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git) para tu sistema operativo.

**Tip:** _[Cómo instalar Git en Windows - Tutorial 2023](https://kinsta.com/es/base-de-conocimiento/instalar-git/)_

## 2: Configurar Git

Después de instalar Git, necesitas configurar tu nombre de usuario y tu dirección de correo electrónico. Abre tu terminal y ejecuta los siguientes comandos, sustituyendo "TuNombre" y "tu@email.com" con tus propias credenciales:

```bash
git config --global user.name "TuNombre"
git config --global user.email "tu@email.com"
```

## 3: Crear un repositorio local

Abre tu terminal y navega al directorio donde deseas crear tu nuevo proyecto.

Ejecuta el siguiente comando para iniciar un nuevo repositorio Git:

`git init`

**Tip:** _Para acceder a un directorio utilizando la terminal Bash, puedes utilizar el comando cd (change directory). Aquí tienes un ejemplo básico:_

```bash
cd ruta/del/directorio
``` 

## 4: Agregar archivos al repositorio (stage)

Coloca tus archivos en el directorio del proyecto.

Usa el siguiente comando para añadir todos los archivos al área de preparación:

`git add .`

## 5: Realizar un commit

Después de agregar archivos, ejecuta el siguiente comando para realizar un commit:

`git commit -m "Mensaje descriptivo del commit"`

## 6: Crear un repositorio en GitHub

Visita GitHub e inicia sesión en tu cuenta.

Haz clic en el botón "+" en la esquina superior derecha y selecciona "New repository".

Dale un nombre a tu repositorio, añade una descripción opcional y haz clic en "Create repository".

## 7: Conectar el repositorio local con GitHub

En tu terminal, ejecuta el siguiente comando, sustituyendo nombreusuario y nuevorepositorio con tu nombre de usuario y el nombre del repositorio en GitHub:

```bash
git remote add origin https://github.com/nombreusuario/nuevorepositorio.git
```

Luego, sube tus cambios al repositorio remoto:

`git push -u origin master`

## Referencias

[Pro Git (Chacon & Straub) *online*](https://git-scm.com/book/es/v2)
