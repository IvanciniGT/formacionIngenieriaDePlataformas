# 60 años atrás!

## Gran crisis del software

Esto ocurrió hace unos 60 años... Finales de los 60.
Esta crisis desembocó en la aparición/creación de la ingeniería de software.

En esos momentos llevábamos más de 2 décadas construyendo software.
Hubo un problemón enorme... los sistemas comenzaron a hacerse tan complejos que eran imposibles de mantener.

De esta época vienen grandes pensadores del mundo del software y grandes principios y conceptos que aún hoy en día seguimos aplicando.
- Cohesión
- Acoplamiento
- Modularidad
- Abstracción

- Constantine
- Parnas
- Dijkstra

- Structured programming

Una de las cosas que se empiezan a hacer es poner un poco de orden en la forma en la que se acometen los proyectos de software.

    "Un programa, por definición, es un producto sujeto a cambios y mantenimiento"

    Que un producto de software (programa) funcione es lo de menos! Se da por descontado.

    "Un coche es, por definición, un producto sujeto a mantenimientos"

Aparecen las metodologías clásicas de gestión de proyectos de software: Waterfall y sus variantes (V, espiral...)

    Arranca un proyecto:
    - Requisitos
      - Planificación Completa
        - Diseño
          - Implementación
            - Pruebas
              - Despliegue
                - Mantenimiento

Para resolver muchos de los problemas que comenzaron a ocurrir con estas formas de trabajar, hace + de 25 años un gruito de 17 individuos... se juntaron en una cabaña.. un finde! Al salir, llevaban bajo el brazo: EL MANIFIESTO PARA EL DESARROLLO ÁGIL DE SOFTWARE.

Una nueva forma (al menos unas nuevas ideas) acerca de cómo debía gestionarse un proyecto de software.

Las metodologías tradicionales dieron sus frutos. Empezamos a crear software mucho más mantenible.
Evidentemente no fue solo cuestión de metodologías. También: 
- Herramientas nuevas (sistemas de control de versiones)
- Arquitecturas nuevas (cliente-servidor, modularidad, ...)
- Lenguajes nuevos (orientados a objetos, ...)

Pero vinieron con sus propios problemas: 
- Burocracia excesiva
- Lentitud a la hora de entregar valor al cliente
- Proyectos que seguían siendo difíciles de mantener (menos.. pero seguían siendo difíciles)

Y los conceptos que se fijaron en el manifiesto ágil, trataron de ir un paso más allá.

Son una evolución de las metodologías tradicionales, pero con un enfoque más centrado en el cliente y en la entrega continua de valor.

# Principal característica de una metodología ágil

Entregar el producto al cliente de forma incremental para ir obteniendo feedback rápido de mi cliente.

    Sprint 1: 10 Mayo. R1, R2, R3
    Sprint 2: 10 Junio R4, R5, R6
    Sprint 3: 10 Julio R7, R8, R9

> Extraído del manifiesto ágil:
    NOTA (A):
        El software funcionando es la MEDIDA principal de progreso > Esta frase, define un indicador para un cuadro de mando!
            


                                                Atributo
                                           -------------------------
        La MEDIDA principal de progreso es el "software funcionando"
           ------
           NUCLEO DEL SUJETO
        ------------------------------- ---------------------------
        Sujeto                          Predicado Copulativo

    La forma en la que vamos a medir que tal va el proyecto (su grado de avance) es a través del concepto "software funcionando".

    Qué es eso de "software funcionando"? Un producto que hace lo que se espera de él.

    Pregunta, quién dice que el software está funcionando? 
        - ~~El cliente~~ Al cliente le tiene que llegar un producto que funcione! Cómo va a ser su responsabilidad decir si aquello funciona?
        - Las pruebas! Otra cosa es que las pruebas se diseñan contra unos requisitos.
          Y el cliente ayuda (algo... poco) con la definición de esos requisitos. 

          El cliente acepta o no el producto... pero no porque funcione o no! Debe de funcionar.
          Lo aceptará en base a si se adecua a lo que él esperaba o necesita.

          Quizás el cliente no ha fijado bien los requisitos... o yo nos los entendí bien.

    De hecho, hoy en día, para determinar cómo va un proyecto lo que hacemos es mirar el número de pruebas que pasan o no pasan, sobre el totoal de pruebas que van a hacerse en ese momento. Y eso es un indicador de si el software funciona o no.

Antiguamente el jefe de proyecto, al planificar el proyecto defínia un calendario de HITOS.

    Hito 1: 10 Mayo. **R1, R2, R3**     ---> Interno
        - Si llegado el 10 de Mayo no estaba el R3:
          - Ostias pa tos los laos!
          - Alarmas
          - Replanificación del hito1: Nueva fecha 20 de Mayo. R1, R2, R3
    Hito 2: 10 Junio R4, R5, R6
    Hito 3: 10 Julio R7, R8, R9

---
    Sprint 1: **10 Mayo**. R1, R2, R3   ---> Entrega al cliente
        - Si llegado el 10 de Mayo no está el R3:
          - Ostias pa tos los laos!
          - Alarmas
          - Vamos a pro con el R1 y R2... la fecha no se mueve ni un minuto!
          - Y el R3 pasa al siguiente sprint, con el resto de requisitos que le toquen.
    Sprint 2: 10 Junio
    Sprint 3: 10 Julio

Pero... las metodologías ágiles, si bien nos ayudaron mucho con muchos de los problemas que teníamos al usar las metodologías tradicionales, también trajeron sus propios problemas.


    Sprint 1: 10 Mayo. 5 requisitos implementados... a pro!
        Pruebas de los 5 requisitos implementados.
    Sprint 2: 10 Junio. Otros 6 requisitos... a pro!
        Pruebas de los 6 requisitos implementados + pruebas de los 5 requisitos anteriores.
    Sprint 3: 10 Julio. Otros 4 requisitos... a pro!
        Pruebas de los 4 requisitos implementados + pruebas de los 6 requisitos anteriores + pruebas de los 5 requisitos anteriores.


Resultado.. Al aplicar una metodología ágil, las pruebas se multiplican!
            Al aplicar una metodología ágil, las instalaciones se multiplican (en pre, Q&A, test, pro)

Y de dónde sale la pasta? Y el tiempo? Y los recursos para tanta prueba / instalación? AUTOMATIZAR LAS PRUEBAS Y LAS INSTALACIONES!




---

# Qué es DEVOPS?

No es un perfil... es una cultura, es una filosofía, un movimiento en pro de la automatización.
Quiero automatizar todo lo que se pueda entre el DEV -> OPS.

                                    Qué es automatizable?           Herramientas

    Plan                            poco
    Code                            cada día más (IA)
    Build                           TOTALMENTE                  JAVA: Maven, gradle
                                                                JS:   npm, yarn, webpack
                                                                .Net: MSBuild, dotnet, nuget
                                                                MAKE
                                                                ANT
    --------> Si consigo automatizar hasta aquí?                            DESARROLLO AGIL!
            Tener mi código en un repo de un Sistema de Control de Versiones (Git, SVN, Mercurial, CVS...)
            Y ser capaz de compilarlo / empaquetarlo en automático.
    Test                            OJO!
        Definición de las pruebas   cada día más (IA)
        Ejecución de las pruebas    TOTALMENTE                  
                                                                Unitarias:
                                                                Java: JUnit, TestNG
                                                                JS:   Jest, Mocha
                                                                .Net: NUnit, xUnit
                                                                Apps Web: Selenium, Cypress, Karma
                                                                Mobile: Appium
                                                                API: Postman, RestAssured, SoapUI, ReadyAPI, Karate
                                                                Performance: JMeter, Gatling, Locust
                                                                Seguridad: OWASP ZAP, Burp Suite, Nessus
                                                                Calidad de código: SonarQube, Checkstyle, PMD, ESLint

        Antes un humano hacía pruebas sobre un programa.
        Ahora un programa hace las pruebas sobre otro programa. Quién crea este programa?
            Necesitamos una versión 2.0 de los testers! 
            - La v1.0 de los testers sabía hacer pruebas manuales.... y tenían los conocimientos necesarios para hacer pruebas de calidad.
            - La v2.0 de los testers, su trabajo ya no es hacer las pruebas... sino hacer programas (o configurarlos) que hagan las pruebas por ellos.
                Las pruebas las ejecuto en la máquina del desarrollador? NO... Por qué? Por que no me fío.. la máquina del dev está MALEA!
                Las pruebas las ejecuto en la máquina del tester?        NO... Por qué? Por que no me fío.. la máquina del tester está MALEA!
                Las pruebas las ejecuto en un entorno de pruebas precreado para tal fin? 
                                                                         YA NO! Esto valía con met. tradicionales.
                    Con met tradicionales, cuñántas veces instalaba en esos entornos? 3 veces? mal contadas.
                    Pero con met. ágiles, cuántas veces tengo que instalar en esos entornos? 300 veces!
                    Y después de 10 instalaciones... una sobre otra... sabeís como va a estar ese entorno? MALEAO!!!!
                Hoy en día la tendencia es tener entornos de prueba de usar y tirar!
                    Cada vez que tengo que hacer una prueba, me creo un entorno nuevo, limpio, con la configuración que necesito para esa prueba... y después de usarlo... lo destruyo.
                    Y tengo pasta? Y recursos? Y tiempo? para crear tanto entorno y borrarlo? NO: Lo automatizo:
                        - IaC (Infrastructure as Code)
                        - Contenedores (Docker, Kubernetes)
                        - Cloud (AWS, Azure, GCP)
                        
                        Terraform, Vagrant, Cloud formation, Ansible, Chef, Puppet, SaltStack, Scripts de la bash, ps1...
                        Docker / Contenedores

                        Y quien crea programas con esas herramientas? Los desarrolladores? Los SYSADMINS de toda la vida!.. En realidad una v2.0 de los SYSADMINS, que ya no se dedican a configurar máquinas (v1.0)... sino a crear programas (o configurarlos) que creen/configuren máquinas por ellos.

                        ESTO ES LO QUE MUCHAS VECES SE MAL-LLAMA DEVOPS! Al sysadmin v2.0
                        Pero sería de absurdo llamar devops al tester2.0... también usa programas de automatización
                        O a los desarrolladores que ahora usan maven, o npm... y ya no descargan dependencias a mano... también usan programas de automatización... llamemos devops a los desarrolladores v2.0 también!

    --------------------------> CI: Integración Continua.
                        Tener CONTINUAmente en el entorno de INTEGRACION la última versión de los desarrolladores sometida a pruebas automáticas.
                        Cuál es el producto de un proceso/programa/pipeline de CI? Un INFORME DE PRUEBAS EN TIEMPO REAL! ** VER (A)
                            No es posible adoptar una metodología ágil sin abrazar una cultura devops!
                            No hay pasta, ni tiempo, ni recursos!
    Release             
        El acto de liberar el código...     TOTALMENTE AUTOMATIZABLE
        El ponerlo en manos de mi cliente.
    ---------------------------> CD: Entrega Continua. Continuous Delivery
                        
    Deploy              TOTALMENTE AUTOMATIZABLE:
                         Terraform, Vagrant, Cloud formation, Ansible, Chef, Puppet, SaltStack, Scripts de la bash, ps1...

                            Contenedores (Kubernetes, Openshift, Tanzu, Karbon, EKS, GKS...)
    ---------------------------> CD: Despliegue Continuo. Continuous Deployment.

    Operate             Kubernetes, Openshift, Tanzu, Karbon, EKS, GKS...
    Monitor             NagiOS, Prometheus, Grafana, New Relic, ELK,...


Nos falta una cosa!

He creado la lavadora... YA TENGO AUTOMATIZADO EL LAVADO DE LA ROPA? En parte... quién la carga? Quién le da al play?
Monto una persiana... la subo y bajo con cuerdita: MANUAL
Ahora... cambio la cuerdita por un motor... con un botón. TENGO AUTOMATIZADA LA SUBIDA Y BAJADA DE LA PERSINA? En parte... quién le da al botón?

Una vez que tengo hechas estas automatizaciones de PRIMER NIVEL, (poner un motor en la persiana, hacer un programa que genere una infra en AWS, hacer otro programa que ejecute pruebas de rendimiento en un sistema....), puedo dar un segundo paso.
Montar un nuevo programa que llame a esos programas... de forma orquestada!

    - Quiero un programa que:
      - Genere un entorno limpio con JAVA y maven
      - Extraiga el código de mi repo
      - Compile el código                                                       1 automatización MAVEN (desarrollo)
      - Ejecute las pruebas unitarias
      - Genere un entorno limpio con un servidor de aplicaciones                1 automatización Docker (sysadmin)
      - Monte un entorno limpio con una BBDD, prepoblada con datos de prueba
      - Despliegue el producto en el servidor de aplicaciones
      - Ejecute pruebas de integración sobre el producto desplegado trabajando contra mi servidor de aplicaciones y mi BBDD
                                                                                1 automatización SELENIUM (tester) 
      - Genere un informe de pruebas en tiempo real
      - Elimine los entornos de pruebas que he creado

Estos son los pipelines de CI/CD: son programas que orquestan otras automatizaciones para conseguir un objetivo concreto: entregar valor al cliente de forma continua, rápida y con calidad.

Esos pipelines los creamos usando herramientas específicas: Servidores de Automatización (CI/CD):
- Jenkins
- Bamboo (el Jenkins de Atlassian)
- Azure DevOps (antes TFS) (el Jenkins de Microsoft)
- GitLab CI/CD (el Jenkins de GitLab)
- TeamCity (el Jenkins de JetBrains)
- CircleCI (el Jenkins de CircleCI)
- TravisCI (el Jenkins de Travis)
- GitHub Actions (el Jenkins de GitHub)
- ArgoCD (el Jenkins de Kubernetes)
- ...

Estos productos son "nuevos" en la industria. Y quien configure estos programas debe tener conocimientos de:
- Desarrollo (al menos lo justo para se capaces de hablar con maven, gradle, npm, webpack...)
- Sysadmin (al menos lo justo para ser capaces de hablar con terraform, ansible, docker...)
- Tester (al menos lo justo para ser capaces de hablar con selenium, postman, jmeter...)

Y ESTE ME TEMO QUE ES UN PERFIL QUE NO HA EXISTIDO ANTES EN LA INDUSTRIA IT... y ahora nos hace falta.. y hay que ponerle un nombre: DEVOPS!

Lo que pasa es que lo primero que comenzó a automatizarse fue la creación de entornos... y eso lo hacían los sysadmins... y son los que empezaron a montar estos pipelines... y al final a los sysadmins que aceptaron esta labor se les llamo devops...
Y se ha malogrado el término para llamar devops a cualquier sysadmin que trabaje con terraform, ansible o clouds.

---

# Clouds

## Entornos de producción.

Qué características tiene un entorno de producción de las que adolecen el resto de entornos?
- HA: Alta disponibilidad.                  
        Tratar de garantizar que el servicio se mantendrá activo un determinado % del tiempo que debería estarlo.
        Esto se acuerda previamente.... y se mide en 9s.

            90%       Admito 36,5 días de caída al año      |   €
            99%       Admito 3,65 días de caída al año      |   €€                          Peluquería de barrio.
            99.9%     Admito 8,76 horas de caída al año     |   €€€€€€€                     Mercadona
            99.99%    Admito 52,56 minutos de caída al año  |   €€€€€€€€€€€€€€€€€€€€€€      Banco
            99.999%   Admito 5,26 minutos de caída al año   |   €€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€ Hospital   
                                                            v

        Redundancia: clusterización, replicación, balanceo de carga, ...

      Toleracia a fallos (de hw, sw, humanas!). Backups
- Escalabilidad: Capacidad de ajustar la infra a las necesidades del momento.

    App1: App departamental
        Día 1:          100 usuarios
        Día 100:        98 usuarios         No es necesario la escalabilidad
        Día 1000:       102 usuarios

    App2: 
        Día 1:          100 usuarios
        Día 100:        1.000 usuarios      Necesito escalabilidad VERTICAL: MAS MAQUINA!
        Día 1000:       10.000 usuarios 

    
    App3: ESTO ES LO NORMAL HOY EN DÍA: ESTO ES INTERNET
        Día N:          100 usuarios
        Día N+1:        1.000.000 usuarios
        Día N+2:        0 usuarios
        Día N+3:        100.000.000 usuarios       

        Pero no por días... por minutos:

        Soy la web del telepi:
            00:00          0 estoy cerrao
            07:00          0 estoy cerrao
            10:00          2 usuarios
            12:00          10 usuarios
            14:00          1.000 usuarios
            17:00          50 usuarios
            18:30          200 usuarios
            20:30 Madrid vs Barça           100.000.000 usuarios
            23:01          0 usuarios

    Quién resuelve esto? CLOUDS!
    Que me dan:
    - Modelo de pago por uso
    - Escalabilidad automática

    Este es el auge de los clouds.
    Esto junto con evitar el que tenga que hacer inversiones iniciales gigantes.

    Los clouds no son la solución a todo... De hecho muchas empresas:
    - Vuelven a on premise porque no les compensa el coste de la nube.
    - Si tengo un volumen de trabajo más constante y conocido de antemano... no me trae cuentas.
      - Si soy una telco, un banco... algo lo tendré en cloud... pero mucho lo quiero on prem... POR COSTES.


    Si me compensa... lo que si, querré AUTOMATIZAR por ejemplo la creación de mis infras! TERRAFORM (IaC)

# IaC: Infrastructure as Code

IaC NO ES SOLO que pueda ESPECIFICAR la infra en ficheros de código.
IaC es tratar la infra como si de código se tratase:
- Control de versiones
- Pruebas unitarias
- Integración continua
- Despliegue continuo


Tendré la V1.0 de mi sistema, que opera en una infra 1.0

Ahora monto la v2.0 de mi sistema, que añade un Redis para cache... pero para eso necesito una v1.1 de mi infra, con una máquina más... para el redis.

    V1.0.0 del software depende de la V1.0.0 de la infra
    V2.0.0 del software depende de la V1.1.0 de la infra

        V1.0.0 del software funcionaría con la v1.1.0 de la infra? SI.. solo que una máquina la tendría parada y sin usar... pero funcionaría.

# Versionado usando el esquema SemVer (esquéma semántico)

vA.B.C

                        ¿Cuándo suben?

    A     MAJOR         Breacking changes (cambios que rompen la compatibilidad con versiones anteriores)
    B     MINOR         Nuevas funcionalidades
                        Funcionalidades marcadas como obsoletas (deprecated)
                        + Opcionalmente pueden venir arreglos de bugs
    C     PATCH         Arreglos de bugs

---

Arquitecturas        MONOLITOS -> Arquitecturas de componentes desacoplados (Microservicios , serverless, ...) 

---

GIT

---

Las herramientas (sistemas de control de versiones,...), metodologías, arquitecturas, lenguajes, infra, todas van evolucionando en el tiempo... y van evolucionando en paralelo! Lo hacen para ir resolviendo los problemas que hay en cada momento del tiempo.

GIT <-> Arquitectura de micrsoservicios <-> Metodologías ágiles <-> Herramientas de CI/CD <-> IaC <-> Clouds    Y todo eso encaja entre si!

CVS/Subversión <-> Arquitectura monolítica <-> Metodologías tradicionales <-> Infra on prem <-> Sin automatización <-> Sin clouds
                                                                                                        Y todo eso sigue encajando entre si!

CVS/Subversión <-> Arquitectura microservicios <-> Metodologías tradicionales <-> Infra on prem <-> Sin automatización <-> Sin clouds
    ESTO YA NO ENCAJA!

CVS/Subversión <-> Arquitectura monolítica <-> Metodologías tradicionales <-> Infra on prem <-> Automatización <-> Sin clouds
    ESTO YA NO ENCAJA!





# Sistema típico de los años 2000/2010

    Sistema de animalitos Fermín!

        Frontal: Navegador WEB
        BBDD Relacional: Oracle, SQL Server, MySQL, PostgreSQL

                            App WEB JAVA
                               v
        Navegador            Tomcat         --> BBDD Relacional
                  <--- HTML ---

# Sistema típico de los años 2026

    Sistema de animalitos Fermín!

    Frontal:
    - App móvil Android
    - App móvil iOS                                     Servicios HTTP REST
    - Navegador WEB             <---- JSON ----             Veterinarios                BBDD Relacional
       React/Angular/Vue                                    Animalitos
       El HTML se genera en Navegador                       Comida    
       En base a los datos                                  Juguetes                    MongoDB
    - Asistente de voz                YAML
    - Chatbot                         XML
    - IVR


---

# Qué es Automatizar?

Crear una máquina (o cambiar el comportamiento de una mediante un programa) que haga las tareas que antes hacía un humano, con sus manitas.

Puedo automatizar el lavado de la ropa (lavadora, que incluso puedo cambiar su comportamiento con programas -de lavado-).

En el mundo IT, la máquina la tenemos COMPUTADORA. Automatizar = CREAR PROGRAMAS que hagan las tareas que antes hacía un humano, con sus manitas.

---


# Qué es eso de la Ingeniería de plataformas?

- Servicios cloud
- CI/CD
- Despliegues entre entornos
- ESTANDARIZACION de infra
- IaC (Infrastructure as Code)

---

La tendencia a día de hoy (impulsada por el manifiesto ágil) es a DESCENTRALIZAR TODO!
No quiero a mi equipo haciendo uetición al CAU para que le monten un Servidor de BBDD mongo...
No acabo el proyecto en la vida!
Y Ahora otro ticket para que ....

Quiero tener equipos autogestionados.

Los clouds me llevan a eso.
Agile me lleva a eso.
Devops me lleva a eso.


Y ... PROBLEMON DE NARICES!

Tengo 500 reinos de taifas.
500 proyectos donde en cada uno se hacen las cosas de una forma diferente!
Y QUIEN COJONES GOBIERNA ESO?
Y como se mantiene?
Y cómo muevo gente de un proyecto a otro?
Y como reaprovecho trabajo entre proyectos?

Y Agile+DEVOPS+CLOUDS han traido cosas GUAYS!
Pero han venido con sus propios problemas... Entre ellos, el más gordo: LA FALTA DE ESTANDARIZACIÓN

Y ahí es donde entra: LA INGENIERIA DE PLATAFORMAS!