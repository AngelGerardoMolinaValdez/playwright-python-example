# Guía de inicio: Playwright con Python 🚀

## Introducción 📚

### ¿Qué es? 🤔

Playwright es un framework de automatización de pruebas para aplicaciones web. Es de código abierto y está desarrollado por Microsoft.

Utiliza un plugin oficial para pruebas de extremo a extremo desarrollado por ellos mismos llamado *Playwright Pytest*. Si bien se recomienda usar este plugin, es posible utilizar una biblioteca alternativa de testing.

### ¿Para qué sirve? 🛠️

Sirve para probar aplicaciones web en distintos navegadores y dispositivos. Automatiza interacciones de navegador y permite pruebas end-to-end, captura de pantalla, y pruebas de rendimiento.

### ¿Dónde se utiliza? 🌐

Se utiliza en el desarrollo de software, especialmente en el desarrollo web, para asegurar la calidad y funcionalidad de las aplicaciones en diferentes entornos de navegadores y dispositivos.

### ¿Por qué Playwright? 🌟

Ofrece soporte multi-navegador (Chrome, Firefox, Safari, WebKit), pruebas en distintos dispositivos y sistemas operativos. Permite pruebas en entornos headless (sin interfaz gráfica) y headful (con interfaz gráfica).

Además, permite integración con sistemas de CI/CD como Jenkins, GitLab CI, etc.

#### Ventajas 🔥

- Multi-navegador y multiplataforma.
- Pruebas en paralelo para mayor eficiencia.
- Soporte para lenguajes como JavaScript, TypeScript, Python, .NET, y Java.
- Captura automática de artefactos de prueba (screenshots, videos).

### Comparación 📊

| Característica            | Playwright                                 | Cypress                        | Robot Framework             | Puppeteer                    | Selenium                         |
|---------------------------|-------------------------------------------|--------------------------------|-----------------------------|------------------------------|----------------------------------|
| Lenguaje Principal        | JavaScript/TypeScript, Python, Java, .Net | JavaScript                     | Python                      | JavaScript                   | Varios (Java, C#, Python)        |
| Multi-Navegador           | Sí (Chrome, Firefox, Safari)               | Sí (Chrome, Firefox, Edge)     | Sí (con librerías)          | No (Solo Chrome, Chromium)   | Sí (Todos los principales)       |
| Pruebas en Paralelo       | Sí                                         | No (En su versión gratuita)    | Sí                          | Sí                           | Sí                              |
| Soporte Móvil             | Sí                                         | Limitado                       | Depende de la librería      | No                           | Sí                              |
| Captura Automática        | Sí (Screenshots, Videos)                   | Sí (Screenshots, Videos)       | Sí                          | Sí (Screenshots, Videos)     | Sí (Con herramientas adicionales)|
| Comunidad y Soporte       | En crecimiento                            | Fuerte                         | Establecida                 | Fuerte                       | Muy fuerte                      |
| Lanzamiento               | 2020                                      | 2017                           | 2005                        | 2017                         | 2004                            |

## Instalación 📦

Es necesario tener instalado [Python](https://www.python.org/downloads/) en tu sistema para continuar con los siguientes pasos.

Una vez instalado python debemos instalar la extensión de Playwright:

`pip install pytest-playwright`

Ya instalado, hay que instalar las dependencias de los navegadores necesarios con el comando:

`playwright install`

[Consulta la información aquí](https://playwright.dev/python/docs/intro#installing-playwright)

## Ejecución 🏃

Una ejecución simple se puede hacer con el comando:

`pytest`

Al no especificar navegador, Playwright tomará por defecto Chrome.

Es posible configurar el comportamiento de ejecución a través de los argumentos de consola. [Vea cómo ejecutar las pruebas aquí](https://playwright.dev/python/docs/running-tests). [Aquí encontrarás los argumentos de consola para configurar tus ejecuciones](https://playwright.dev/python/docs/test-runners).

## Referencias 📚

- [Documentación oficial](https://playwright.dev/)
- [Documentación oficial con Python](https://playwright.dev/python/)
- [GitHub Playwright](https://github.com/microsoft/playwright)
- [GitHub Playwright con Python](https://github.com/microsoft/playwright-python)
