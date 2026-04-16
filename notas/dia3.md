
Ingeniería de plataformas es el punto en el que nos encontramos hoy en día para paliar las dificultades que nos hemos encontrado cuando hemos adoptado intensivamente las:
- Prácticas de DevOps
- Metodologías ágiles
- Cloud
- Contenedores
- Microservicios 

Problemas que nos hemos encontrado:
- Mucha carga de trabajo el comenzar un proyecto nuevo. Al medio plazo se justifica... pero al principio es un gran esfuerzo.
- Necesito mucha gente que sepa de muchas cosas (por la descentralización y los equipos con autonomía)
- Falta enorme de estandarización... como mucho ... distintos equipos juegan con las mismas herramientas.
- Nula reutilización... cada equipo monta su pipeline, su infraestructura, su monitorización, flujos de trabajo con git, etc... y no se aprovecha el trabajo de otros equipos.

Lo que buscamos conseguir con la ingeniería de plataformas:
- Estandarización de herramientas, procesos, plantillas, etc.
- Reutilización del trabajo de otros equipos.
- Que los equipos puedan tener soporte en el uso de los sistemas de DEVOPS (Jenkins...) en los despliegues (cloud, kubernetes)
- Autonomía de los equipos y autoservicio.
- Minimizar la carga de trabajo de los equipos, y que puedan centrarse en lo que realmente aporta valor a su negocio (el desarrollo de su aplicación) y no en el mantenimiento de sus pipelines, infraestructura, monitorización, etc...
- Minimizar el esfuerzo de comenzar un proyecto nuevo
- Reducir la carga cognitiva de los equipos, que no necesiten tener tanto conocimiento de todas las herramientas


Pero claro... esto no es una solución! Hay ideas... prácticas.. formas de trabajo (muy genéricas) que hay que aterrizar a cada caso concreto, a cada empresa, a cada equipo... 

Eso es la labor de un ingeniero de plataformas... ayudar a aterrizar esas ideas, prácticas, formas de trabajo a cada caso concreto, a cada empresa.

Debemos tener en cuenta:
- Herramientas que se usan en la empresa (Jenkins?, Gitlab, Azure DevOps...)
- El tipo de proyectos que se desarrollan (aplicaciones monolíticas, microservicios, etc...)
- El tipo de infraestructura que se usa (cloud, on-premise, etc...)
- Los lenguajes de programación que se usan (Java, .NET, Python, etc...)
- El tipo de equipos que tenemos (tamaño, experiencia, etc...)

Hay soluciones muy enlatadas (Openshift - Redhat)

- El problema de estas soluciones tan enlatadas es que no se adaptan a las necesidades de la empresa
- Es la empresa la que tiene que adaptarse a la solución, a las formas de trabajo
- Además no cubren toda la casuística que tenemos en la empresa
- En paralelo son baratas y de rápida implantación

Hay soluciones un poco menos enlatadas... que cubren más casos.... pero muy orientadas a nichos concretos.
CoE (Center of Excellence) de Microsoft -> Power Platform  [NOCODE]

Soluciones totalmente a medida: Backstage me permite montar un ipd (internal developer portal).
Cuidado que backstage no es un idp que configuro... Es un framework para montar un idp... y tengo que desarrollar el idp con backstage... lo que me da mucha flexibilidad, pero también mucho trabajo.
Y no solo eso... una vez tengo el IDP... métele plantillas.
Cada plantilla van a ser semanas de trabajo.... y me resuelve un caso concreto... del que espero tener muchas ocurrencias.
    Plantilla: Microservicio Springboot/Java/BBDD Relacional...


---

# Openshift

---

# Contenedores

Un contenedor es un entorno aislado dentro de un kernel linux donde puedo ejecutar procesos.
Aislado:
- Tiene su propio filesystem (~HDD)
- Tiene sus propias variables de entorno
- Tiene su propia configuración de red (y por ende, su propia IP)
- Puede tener limitación de acceso a los recursos del host (CPU, RAM, etc...)

Son una alternativa a la hora de instalar/desplegar software.


## INSTALACION TRADICIONAL

        App1 + App2 + App3          Problemas de esta forma de instalar:
    --------------------------          - Incompatibilidades entre aplicaciones (versiones de librerías, etc...)
        Sistema Operativo               - Necesidades específicas de configuración de SO
    --------------------------          - Si App1 tiene un Bug y pone la CPU 100%; App1 -> OFFLINE
             HIERRO                                                                App2 -> OFFLINE
                                                                                   App3 -> OFFLINE

## INSTALACION BASADA EN VMs

        App1    |  App2 + App3      Si bien resuelve todos esos problemas, vienen con los suyos:
    --------------------------          - Merma en el rendimiento
        SO 1    |   SO 2                - Merma de recursos (CPU, RAM, etc...)
    --------------------------          - Complejidad de instalación / mantenimiento
        MV 1    |   MV 2
    --------------------------      
            Hipervisor           
        KVM, HyperV, VMWare, 
        VirtualBox, etc...
    --------------------------      
        Sistema Operativo           
    --------------------------      
             HIERRO                 
                                    

## INSTALACION BASADA EN CONTENEDORES

        App1    |  App2 + App3      
    --------------------------      
        C 1     |   C 2
    --------------------------      
        Gestor de contenedores      
        Podman, Docker, Crio, Containerd
        (Openshift, Kubernetes... NO SON GESTORES DE CONTENEDORES)
    --------------------------      
      Sistema Operativo Linux          
    --------------------------      
             HIERRO                 
                                    

Los contenedores se crean desde IMAGENES DE CONTENEDOR:

Una imagen de contenedor es un triste fichero comprimido (tar) con:
- Una estructura de carpetas compatible con POSIX, poblada con programas y configuraciones... Un huevo de ellos.
    bin/
        ls
        cp
        bash
        yum
    etc/
        nginx/
            nginx.conf
    lib/
    usr/
    var/
    opt/
        nginx/
            nginx

Las imágenes de contenedor las descargamos de registros de repositorios de imágenes de contenedor:
- Dockerhub
- Microsoft Artifact  Registry
- Oracle Container Registry


Todo el software empresarial hoy en día se distribuye en forma de imágenes de contenedor. Y se despliega en forma de contenedores.


# Qué era Unix?

Unix era un SO que hacía un dpto de la americana de telecomuncaciones AT&T (Lab. bell) en los años 70.  Dejaron de hacerlo a principios de los 2000.
Este UNIX no se licencia como se licencia hoy en día los SO (EULA: End User License Agreement).
AT&T licenciaba Unix a empresas productoras de hardware, universidades y grandes corporaciones.
Éstas adaptaban el código de UNIX a sus equipos. Y si lo revendían, daban una nueva licencia.

Llegó a haber más de 400 versiones distintas. Y empezaron a dejar de ser compatibles entre si.
PROBLEMON. Los programas que hacía para una versión de UNIX no funcionaban en otra versión de UNIX.

Solución: Crear 2 estándares para controlar las evoluciones del SO:
- POSIX: Portable Operating System Interface. Estándar de la IEEE (Institute of Electrical and Electronics Engineers). 
- SUS: Single UNIX Specification. Estándar de The Open Group.

Unix dejó de hacerse... pero los estándares siguieron vivos... y siguen evolucionando.
Hay fabricantes que crean SO cumpliendo con esos estándares a día de hoy.

# Qué es Unix?

No es un SO. UNIX son esos 2 estándares. Y decímos que un SO es UNIX® cuando cumple con esos estándares.

IBM    - AiX UNIX®
HP     - HP-UX UNIX®
Oracle - Solaris UNIX®
Apple  - MacOS UNIX®

---

Hay gente que intentó montar un SO basado en esos estándares... pero no querían certificarlo (CUESTA MUCHA PASTA!)
Y no hubo 1 ni 2... hubo un huevo.

- Universidad de Berkeley en california: 386-BSD (Berkeley Software Distribution)
  Lo consigueron y la cagaron.... Se les ocurrió decir que TENIAN UN SO QUE CUMPLIA CON UNIX...
  Y llegó AT&T y ... denuncia al canto! Años de litigios. Al final ganó la Universidad de Berkeley... pero para entonces ya no usábamos la arquitectura de microprocesadores 80386
  No pudo llegar a usarse.... no obstante, grupos por ahñi usaron ese código como base para montar otros SO que si seguirmos usando a día de hoy:
  - NetBSD
  - FreeBSD
  - OpenBSD
  - MacOS

- GNU (Richard Stallman): 
  GNU's Not Unix. Señores de AT&T no se les ocurra denunciarnos, por que lo dejamos claro hasta en el nombre: NOSOTROS NO SOMOS UNIX!
  Lo intentaron... No llegaron.
  Hicieron casi todo lo necesasrio para tener un SO:
  - Cargadores de arranque
  - Shell de linea de comandos: bash
  - Interfaz gráfica: Gnome
  - Editores de texto: Emacs, gedit, etc...
  - Compiladores: GCC
  - Juegos: Chess, etc...
  - No valieron para montar el KERNEL!
  
- Linus Torvalds... parió un kernel de SO (preseuntamente compatible EN ORIGEN con los estándares UNIX): Linux

- Linux + GNU = GNU/Linux

GNU Linux se distribuye mediante compendios de software llamados distribuciones. O no.
Debian -> Ubuntu -> Mint
RedHat -> CentOS , RHEL, Fedora, Oracle Linux
Suse -> OpenSUSE, SLE (Suse Linux Enterprise)

Pero hay muchos otros SO que corren Linux. De hecho Linux es hoy en día el KERNEL DE SO más usado del mundo!
Muy por encima del de microsoft Windows (NT):
- Android (Kernel Linux + herramientas y librerias de GOOGLE)
- ChromeOS (Kernel Linux + herramientas y librerias de GOOGLE)
- Windows 10, Windows 11, los Windows Servers son capaces nativamente de ejecutar el kernel Linux (Windows Subsystem for Linux). No hay que instalar nada... Viene de serie con Microsoft. Está en características de Windows.

# Qué es Linux?

Es un kernel de SO.
Un SO no es un programa... son cientos/miles de progframas juntitos. Programas con distintas responsabilidades:
- Cargador de arranque (bootloader)
- Kernel (controla el hw, controla los procesos, proporciona seguridad, planificación de discos)
- Shell de linea de comandos: cli: bash, cmd.exe, powershell...
- Interfaz gráfica: GUI: FluentDesign, Aqua, Gnome, KDE, etc...
- Gestor de paquetes: apt, yum, brew, chocolatey, tienda de windows, etc...
- Drivers, librerías
- Bloc de notas
- Herramienats para formatear un disco
- Para ver los procesos que tengo corriendo (administrador de tareas, top, ps)

NOTA: Hoy en día, el desarrollo de LINUX va totalmente independiente de los estándares UNIX. 
Lo que pasa es que como en sus orígenes era compatible con esos estándares... pues sigue habiendo grandes similitudes entre los SO que usan Linux como kernel y los SO certificados como UNIX®.

# Windows

Windows tampoco es un SO...
Windows es una FAMILIA de SO:
- Windows 2019 server
- Windows 11
- Windows 3.1

# Microsoft

Microsoft en su historia ha creado 2 kernel... con ellos ha montado todos sus SO
- DOS: MSDOS, Windows 3, Windows 95, Windows 98, Windows Millenium
- NT (New Technology): Windows NT, Windows 2000, Windows XP, Windows Vista, Windows 7, Windows 8, Windows 10, Windows 11, Windows server

---


# Kubernetes

Es una herramienta para el diseño y operación de entornos de producción basados en contenedores, usando lenguaje declarativo.

Docker, containerd, podman NO VALEN PARA ENTORNOS PRODUCTIVOS.
En un entorno productivo NECESITO UN CLUSTER DE MAQUINAS... para tener HA y ESCALABILIDAD.
Docker, containerd, podman se instalan en 1 máquina... no vale.


    Cluster:

        Nodo Maestro 1
            crio | containerd
                Kubernetes
        Nodo Maestro 2
            crio | containerd
                Kubernetes
        Nodo Maestro 3
            crio | containerd
                Kubernetes

        Nodo 1
            crio | containerd
        Nodo 2
            crio | containerd
        Nodo 3
            crio | containerd
        Nodo N
            crio | containerd

Kubernetes me permite montar un entorno de producción con:
- Contenedores (aunque los pone en paquetes/grupos) que llama pods
- Balanceador de carga (service)
- Almacenamiento persistente HA (volumes)
- Reglas de proxy reverso (ingress)
- Escalabilidad automática (horizontal pod autoscaler, vertical pod autoscaler)
- Reglas de firewall (network policies)
- Las cosas de las que consta un entorno normal de producción.

Luego hay distros de kubernetes que añaden cosas a kubernetes:
- Escalado de máquinas (machine autoscaler)
- Gestión integral de certifcacodos ssl (cert manager)
- Gestión de secretos (vault)
- ...

Esas cosas son las que puedo instalar yo a pelo en un kubernetes pelao...
O puedo coger una distro de kubernetes que ya las tenga integradas... 
- Openshift  <- Redhat
- Tanzu      <- VMware
- Karbon     <- Nutanix
- EKS        <- Amazon
- GKS        <- Google
- AKS        <- Microsoft
- K3s        <- Vainilla

Docker es un gestor de contenedores
Kubernetes lo podrías ver como un orquestador de gestores de contenedores... 

La distro de kubernetes posiblemente más usada y de las mejor valoradas es Openshift de Redhat.

Y Openshift ha montado un huevo de cosas encima de kubernetes
Entre ellas ha puesto un empeño enorme en el autoservicio para equipos de desarrollo mediante plantillas.
Y esta es la parte que nos interesa a nosotros como ingenieros de plataformas.

---

Cuando trabajamos en un cluster de kubernetes, un equipo tiene lo que se llama un namespace. Uno o varios:
- Namespace de la app1 - desarrollo
- Namespace de la app1 - preproducción
- Namespace de la app1 - producción

Es como un área de trabajo dentro de un cluster.

Al equipo le doy un usuario (o varios) con permisos para operar en ese namespace.
Limito el ns:
- Total de RAM que pueden usar las aplicaciones que se despliegan en ese namespace
- Total de CPU que pueden usar las aplicaciones que se despliegan en ese namespace
- Total de almacenamiento que pueden usar las aplicaciones que se despliegan en ese namespace
- ...

Y ya que el equipo haga lo que quiera dentro de ese namespace... 

Con esto consigo provisionamiento de INFRA!
Lo que antes conseguía haciendo un ticket al cau... para el equipo de infra.

---

Microsoft CoE (Center of Excellence) -> Power Platform  [NOCODE]

Power Platform es la plataforma de desarrollo NoCode (LowCode) de Microsoft.
Sería equivalente a herramientas como OutSystems, Mendix, Appian, etc...

La power platform tiene 5 grandes herramientas de primer nivel:
- Power Apps:               para crear aplicaciones web y móviles sin código.     (Frontend)
- Power Automate:           para crear flujos de trabajo automatizados sin código (Backend)
- Copilot Builder:          para crear chatbots y conectarme con IAs sin código. (Chatbots)
- Power BI:                 para crear cuadros de mando e informes sin código.       (Cuadros de mando)
- Power pages:              para crear sitios web sin código.                            (Web)

Además incluye una herramienta llamada Dataverse, que es una base de datos relacional en la nube, con la que se pueden conectar las otras herramientas de la plataforma.

Cómo empezó vendiéndola microsoft:

Herramienta para empoderar a los usuarios de negocio a crear sus propias aplicaciones sin necesidad de depender del departamento de IT. Democratización del desarrollo de software.

El desarrollo de software va muchísimo más allá de la creación de código.
Desarrollar software no es conocer un lenguaje de programación... al menos no es solo eso.

Arquitectura de la información
Seguridad / Gobernanza del dato
Integración con otros sistemas
Procotolos
Algoritmia
Refactorización
Modularización
Principios de desarrollo
Arquitecturas de software
...

Microsoft tuvo que recular... pero sin desdecirse.

Bueno... si vale para eso... pero... hay que poner orden.
Vamos a montar un CoE en las empresas.
CoE = Center of Excellence. 

Es un equipo de personas con conocimientos técnicos y de negocio, que se encargan de ayudar a los usuarios de negocio a crear sus propias aplicaciones sin necesidad de depender del departamento de IT.

La misión del CoE es:
- Ayudar a los usuarios de negocio a crear sus propias aplicaciones sin necesidad de depender del departamento de IT.
- Para ello proporcionan formación, soporte, plantillas, etc... para que los usuarios de negocio puedan crear sus propias aplicaciones sin necesidad de depender del departamento de IT.
- Revisar las aplicaciones creadas por los usuarios de negocio para asegurarse de que cumplen con los estándares de calidad, seguridad, etc... de la empresa.
- Proporcionar mecanismos para el despliegue de apps entre entornos (desarrollo, preproducción, producción)

El dpto IT eran 300 programadores... y luego nuso cuantos sysadmins... y tester...

CoE -> 10 personas que sepan un HUEVO! Mucho más que todos esos 300 programadores juntos... 
Que monten plantillas
Que revisen
Que estandaricen
Que centralicen ciertas gestiones.
Que tengan VISIBILIDAD!

Esta es la visión de Microsoft para la Power Platform de la Ingeniería de Plataformas.

---

Backstage (proyecto de código abierto de Spotify) es un framework JS para montar un IDP (Internal Developer Portal).

Es un follón montar un IDP... pero es una herramienta que me da mucha flexibilidad para montarlo a medida de mis necesidades.

Hay 2 partes importantes en un IDP:
    - El portal en sí mismo, con su interfaz gráfica, sus menús, etc... para que los desarrolladores puedan interactuar con él.
    - Plantillas para que los desarrolladores puedan crear sus aplicaciones, pipelines, infraestructura, monitorización, etc... sin necesidad de depender del departamento de IT.

Una plantilla de un proyecto es infumable:
- Crea repo en git
- Crea ficheros de ejemplo (pom.xml, package.json, etc...)
- Crea pipeline de CI con Jenkins, Gitlab, Azure DevOps, etc...
- Registra esos pipelines en Jenkins...
- Genera entornos de desarrollo, preproducción, producción en kubernetes o en cloud u on premise...
- Configura monitorización con Prometheus, Grafana, New Relic, ELK, etc...
- Configura alertas con Prometheus, Grafana, New Relic, ELK, etc...
- Configura entrega continua contra un nexus, artifactory, etc...
- Configura pipelines de despliegue contra kubernetes, cloud, on premise, etc...
- Genera vault de secretos para la aplicación... para cada entorno (desarrollo, preproducción, producción)
- Un huevo de cosas

Pero el portal no se queda atrás!
- Necesito de entrada autenticación de usuarios (conectate a un IaM de Microsoft, Amazon, Google, Github, Gitlab, etc...)
- La herramienta (el portal) necesita integrarse con 500 herramientas distintas (git, Jenkins, Nexus, Artifactory, Kubernetes, cloud, monitorización, etc...)
  - Trabajas con gitlab, github, bitbucket? -> Integración con esa herramienta concreta
  - Trabajas con Jenkins, Gitlab, Azure DevOps? -> Integración con esa herramienta concreta
  - Trabajas con kubernetes, cloud, on premise? -> Integración con esa herramienta concreta
  - ...

Backstage da una base... y 500 módulos qque tienes que ir configurando.
Pero no penséis que es sencillo... que no es apretar botones en una pantalla...Que 
si quiero meter un módulo es:- 
Vete al fichero de la aplicación de frontal JS y en el fichero de plugins.js metes estas 4 lineas de código 
Y en el otro...

El implantar una herramienta como backstage son meses/años de trabajo hasta que tengo un idp mínimo viable.

Esto está encima de todo! Es la capa de arriba.
- Si no tengo automatizado la creación de entornos... Backstage no vale de nada
- Si no tengo plantillas para crear proyectos... Backstage no vale de nada
- Si no tengo pipelines de CI... Backstage no vale de nada
- Si no tengo pipelines de CD... Backstage no vale de nada

Es decir... que lo primero es montar todas esas cosas.
Es lo mismo que lo de la persiana y el motor.

Paso 1: Cambio en la persiana la cuerdita por un motor y le pongo un botón
        mvn test
Paso 2: Me comunico de alguna forma con el motor para que suba y baje la persiana automáticamente en base a eventos.
        pipeline de CI
Paso 3: Convierto eso en una plantilla, para poder desplegar persinas con motor a tutiplen!
        plantilla de proyecto (scaffolding de Backstage)


Además, hay cosas adicionales que me venden mucho con Backstage:
- Documentación de los proyectos: Queremos estandarizar la documentación de los proyectos... y que esté disponible en un mismo sitio: En el portal
  - Para eso me ofrece un módulo de documentación... pero claro... tengo que meter la documentación de cada proyecto en el formato que espera ese módulo (markdown... pero en una determinada estructura de carpetas... con un fichero de configuración con metadatos... etc...)
  > Es decir.. que luego hay que formar a la gente en el uso de aquello.


  