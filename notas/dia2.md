# Años 60

Mucha improvisación, poca disciplina... poco conocimiento.
Poco a poco los proyectos se fueron haciendo más complejos.

> Vivíamos en una anarquía absoluta!

Empezamos a tener problemas graves de evolución de los productos de software -> Gran crisis del software.

Consecuencia: Impulsamos la ingeniería de software

# Años 75-> 2000

Empezamos a centralizar y procedimientar TODO!

Surgen departamentos IT centrales en las empresas, con sus procesos, procedimientos, metodologías, herramientas, etc... para controlar el caos.

- Metodologías de desarrollo: Waterfall, V, RUP, etc... MUY RIGIDAS!
- Herramientas de gestión de proyectos: MS Project, etc... MUY RIGIDAS!
- Herramientas de ticketing: Jira, etc... MUY RIGIDAS!

Surgen cosas como ITIL, COBIT, CMMI, etc... para controlar el caos.

Todo esto dio lugar:
- PURA BUROCRACIA!
- Cambios lentos, costosos
- Poca innovación

# Años 2000 -> ahora

Como reacción a todo lo anterior, surge el movimiento ágil.
- Flexibilidad, adaptabilidad, rapidez, innovación, etc...
- Descentralizar, empoderar a los equipos, eliminar burocracia, eliminar documentación innecesaria, etc...

Empezamos a tener necesidad / herramientas de automatización, integración continua, entrega continua, despliegue continuo, etc... para soportar el movimiento ágil -> Nace DevOps.

En paralelo, nos surgen los Clouds:
- Modelo de pago por uso
- Escalabilidad
- Autoservicio
- etc...

Todo eso empieza a cocinarse junto, y se retroalimenta.

El que un equipo tenga capacidad de crear su propia infra sin depender de nadie -> empodera al equipo! -> más agilidad, más innovación, más rapidez, etc...
Pero en paralelo se intensifica la necesidad de seguir automatizando, integrando, entregando, desplegando, etc... para soportar esa agilidad -> más necesidad de DevOps!

NUEVO PROBLEMA: CAOS federado
- Cada equipo hace la guerra por su cuenta!
- Cada equipo usa conjuntos de herramientas diferentes
- Pipelines diferentes
- Infraestructura diferente
- Forma de desarrollar, desplegar, operar , monitorizar diferente
- No hay quien gobierne esto
- No puedo mover gente entre equipos

Y volvimos al caos... aquí estamos!

La propuesta de solución a este problema:

# Ingeniería de plataformas

Nuevo modelo:
- Autonomía de los equipos y autoservicio
- Estandarización de herramientas, procesos, plantillas, etc... para que los equipos puedan usarlos
- Reusar el trabajo de otros equipos, y no tener que reinventar la rueda cada vez que quiero montar un pipeline, o una infraestructura, o una forma de monitorizar, etc...

## Qué buscamos con la ingeniería de plataformas?

No centralizar, pero si estandarizar. Necesito un equipo que:
- Defina estandares, herramientas, procesos, plantillas, etc... para que los equipos puedan usarlos.
- De soporte a los equipos para que puedan usar esos estándares, herramientas, procesos, plantillas...
- Quiero que los equipos sigan siendo autogestionados
- Nos gusta mucho el tema del autoservicio, pero de forma estandarizada, con unos límites claros, y con un equipo de soporte detrás que me ayude a resolver los problemas que surjan.
- Quiero reaprovechar el trabajo de otros equipos, y no tener que reinventar la rueda cada vez que quiero montar un pipeline, o una infraestructura, o una forma de monitorizar, etc...
  Al final tenemos 200 microservicios TODOS IGUALES!
  Los mismos pipelines de CI, CD, etc... para todos los microservicios!
  La misma infraestructura para todos los microservicios! (Kubernetes/Contenedores , Cloud, etc...)
  La misma forma de monitorizar, operación, etc... 

## Qué no buscamos con la ingeniería de plataformas?

No queremos volver al modelo IT centralizado, con sus procesos, procedimientos, metodologías, herramientas, etc... para controlar el caos. -> Burocracía y lentitud!
No queremos la anarquía, ni la absoluta, ni la federada! -> Caos!


---

Tengo un microservicio que me permite hacer CRUD por http rest de Animalitos (Fermin)
JAVA/Springboot/Maven/MariaDB/Redis/MinIO, que desplegamos en un cluster de kubernetes... con contenedores.
Por supuesto:
- Monitorizamos el microservicio con Prometheus y Grafana
- Control centralizado de logs con ELK
- La autenticación es delegada a un microservicio de autenticación centralizado (Keycloak)

Arquitectura de ese microservicio:
   
   Capa Controlador (HTTP/Rest)             Controlador Rest
   Capa servicio (Lógica de negocio)        Service
   Capa persistencia                        Repository

> Quiero montar un pipeline de CI para este proyecto? NO!
  Cuál era el objetivo/producto de un pipeline de CI?

  CI? Tener CONTINUAmente en el entorno de INTEGRACION la última versión del código sometida a pruebas automáticas -> INFORME DE PRUEBAS EN TIEMPO REAL! (A)

  La respuesta es NO, porque NO QUIERO montar UN pipeline de CI, NECESITO MONTAR LA HUEVA DE PIPELINES DE CI... para este proyecto!

---

# git?

El concepto clave con git: COMMIT!

## Commit?

- Verbo             Accion de generar un commit.
- Sustantivo        Un snapshot del código COMPLETO del proyecto en un momento dado. BACKUP. ZIP completo de la carpeta!
                    NO ES un paquete de cambios. (SI LO ERA CON SVN, PERO NO CON GIT!)

Todo commit parte de otro. Acabo con una secuencia de commits (backups completos).

Cuando git necesita conocer (o yo) los cambios concretos entre dos commits, git calcula esa diferencia bajo demanda!

## Qué diferencia a git de un sistema de backups tradicional?

Que no tengo una sola secuencia de commits, sino que puedo tener secuencias paralelas entre si: RAMAS!


--- main (master)

    2 reglas:
        Lo que hay en esta rama se considera apto para producción.
        NADIE, bajo pena capital hace un commit en esta rama... Solo puedo copiarle commits de otras ramas.

--- dev/desa/develop/development/desarrollo

    2 reglas:
        Lo que hay en esta rama se considera apto para la siguiente release.
        NADIE, bajo pena capital hace un commit en esta rama... Solo puedo copiarle commits de otras ramas.
            (Esto en desa es un poco más flexible... siempre que el proyecto seamos yo y mi primo. Si somos varios, la trato igual que main)

--- feature/xxx



   Controlador Rest API (HTTP/REST)
   Controlador Rest Impl
   
   Service API (JAVA)
   Service Impl

   Repository API (JAVA)
   Repository Impl (JPA) 

                                                                                                 SQL
    Angular/TS                                Java/Springboot                                    vvv
----------Frontal---------------  -------------------- Backend ----------------------------------------------
    C.Formulario --> Servicio  ----> Controlador HTTP REST ---> Service ----> Repository ----> Base de datos

    Captura info     comunicación    lógica de exposición       lógica          lógica              lógica 
                     backend         del servicio               negocio         de persistencia     del dato



Lógica:
    Captura de datos            <- Usuario
    Comunicar datos al backend  <- Desarrollador de backend



SOLID:
- Single Responsibility Principle (SRP) -> Cada componente del sistema debe atender a un único actor.

Viola el concepto de Cohesión



Ingeniería de software -> NO ES UNA CIENCIA EXACTA!
Cualquier ingeniería opera con restriccciones de tiempo, pasta, recursos.

--- main ---------------------------------- C7             Pruebas de humo            ENTORNO DE PRODUCCION
                                            /
--- release ------------------------------C7            + Pruebas de sistema + Pruebas de aceptación       ENTORNO DE PREPRODUCCION
                                          /     <- Pruebas de sistema
----desa ---> C1 -----------> C3 ------> C7             Para hacer pruebas unitarias/integración  ENTORNO DE INTEGRACION!
               \            /    \     /                                   
---repo------- C1 -> C2 -> C3     \   /
                 \                 \ /
---service----   C1 -> C4 -> C5 -> C7                   Hago pruebas de integración
                              ^
                        Pruebas unitarias

Cuales de esas quiero automatizar? TODAS!
Pero las ejecutaré en distintos momentos, con distintas frecuencias, y con distintos objetivos.
Y montaré pipelines de CI diferentes para cada una de ellas, con distintas herramientas, etc...

Pruebas unitarias?         Prueba que comprueba aspectos de un componente AISLADO!
Pruebas de integración.    Prueba que comprueba aspectos de la COMUNICACION entre componentes.
Pruebas de sistema         Comprueba el funcionamiento del sistema en su conjunto

Bicicleta: ORBEA

    Ruedas                  La monto en un bastidor... le pego un viaje con la mano... veo que gira.. estable.
    Sistema de frenos       Lo monto en un bastidor...
                                Aprieto palanca y miro si las pinzas cierran
                                Incluso podría ver si cierran con la fuerza suficiente? Meto un sensor de presión entre las pinzas
                                    función: apretarPalanca();

    Ruedas
    Sillín                  Pruebas unitarias / del componente aislado
          Cojo el sillín lo monto en un bastidor (4 hierros mal soldaos... en los que confío)?
            - Prueba de carga .. a ver si aguante el peso de una persona de 130kgs
            - Prueba de estres.. me subo y bajo 300.000 veces... a ver si el cuero aguanta o no.
            - Pruebas de seguridad... a ver si cuando giro el gastidor (a los lados) no me resbalo
            - Pruebas de UX.. a ver si cuando llevo 2 horas arriba, el culo me duele o no... a ver si el sillín es cómodo o no.

        Qué gano? Confianza +1     Vamos bien!

Qué cojones pinto yo en todo esto? Diseño e integro componentes... quizás fabrique alguno


Cómo se llama al bastidor y al sensor de presion y esas mierdas que me hacen falta para las pruebas en el mundo del software? TEST DOUBLES: Mocks, Dummy, Fake, Spy, Stub (Martin Fowler)



        Sistema de frenos + rueda  Lo monto en un bastidor... y meto entre las pinza la rueda y la pongo a girar!
                                Aprieto palanca y miro si la rueda se para

                                 función: apretarPalanca();

        Qué gano? Confianza +1     Vamos bien!

Prueba de sistema:
    Cojo la bici! subo a un tio, mochila en la espalda, bocadillo de chiorizo y agua a tuptiplen.. y pa cuenca!

---

Pipeline de CI para las ramas feature UNITARIAS / INTEGRACION

    1. Disponer de un entorno limpio con java 17 y maven 3.9 (Contenedor)       docker container create....
    2. Clonar el repo (la rama feature de turno) en ese entorno:                git clone ....
    3. Compilo el código:                                                       mvn compile
    4. Compilo las pruebas:                                                     mvn test-compile
    5. Ejecuto las pruebas unitarias:                                           mvn test
    6. Genero un informe de cobertura de código:                                mvn jacoco:report
    7. Reviso la calidad del código:                                            mvn sonar:sonar
    8. Genero un informe de pruebas:                                            mvn surefire-report:report

Pipeline de CI para la rama desa / SISTEMA

    1. Disponer de un entorno limpio con java 17 y maven 3.9 (Contenedor)       docker container create....
    2. Clonar el repo (la rama feature de turno) en ese entorno:                git clone ....
    3. Compilo el código:                                                       mvn compile
    4. Compilo las pruebas:                                                     mvn test-compile
    5. Ejecuto las pruebas unitarias:                                           mvn test
    6. Genero un informe de cobertura de código:                                mvn jacoco:report
    7. Reviso la calidad del código:                                            mvn sonar:sonar
    8. Monto una BBDD real                                                      docker container create mariadb
    9. Populo la BBDD con datos reales (o lo que se necesite)                   docker container exec mariadb mysql -u root -p < dump.sql
    10. Monto un entorno REDIS real (o lo que se necesite)                      docker container create redis
    11. Genero una imagen de contenedor del microservicio con el código de la rama desa.     
                                                                                docker build -t mi-microservicio:latest .
    12. Arranco el microservicio en modo desa, apuntando a esa BBDD real.                 
                        docker container create mi-microservicio:latest -e SPRING_PROFILES_ACTIVE=desa -e SPRING_DATASOURCE_URL=jdbc:mariadb://mariadb:3306/mi-bbdd
    13. Ejecuto las pruebas de sistema apuntando a ese microservicio en modo desa.      postman
    14. Ejecuto pruebas de rendimiento apuntando a ese microservicio en modo desa.      jmeter
    15. Genero un informe de pruebas:                                            mvn surefire-report:report

Posiblemente quiero que los git merge --fast-forward de las ramas feature a desa, y de desa a release solo se puedan ejecutar por el usuario:
jenkins/azuredevops/gitlab-ci-user
Y no quiero que ningún humano (NI SI QUIERO YO) lo haga.

Y quiero que para promocionar un commit de featureXXX a desa, que ese trabajo lo haga un pipeline siempre que las pruebas se hayan superado.
Y lo único que voy a hacer es trabajar con tags

    git commit -m 'Todo listo'
    git tag -a v1.1.0 -m "Apto para producción"
    git push origin v1.1.0

    pull request -> Para aprobación (BUROCRACIA)

        -> En automático, al llevar ese commit un tag, que el pipeline acabe haciendo el 
            git merge --fast-forward        // Esto es lo que en git me permite copiar commits de una rama a otra
        de ese commit a desa.


    Jefe de proyecto     Controlar! Cuello de botella!              Departamento IT centralizado con tickets

    Product Owner        Ayudar!!!                                  Departamento centralizado de apoyo a los demas!
    Scrum master         Ayudar!!!                                  Gobierno federal!


---

Queremos:
- Montar un portal para los equipos de desarrollo: IdP (Internal Developer Portal)
- Montar plantillas de proyecto (30 plantillas-300 plantillas)
  - Nuevo proyecto de microservicio con bbdd mariadb:
    - Crea los repos en git
    - Te crea archivos pom.xml 
    - Carpetas con código de ejemplo
    - Pipeline de CI con pruebas unitarias
    - Pipeline de CI con pruebas de sistema
    - Pipeline de CD para subir artefactos al nexus / artifactory
    - Pipeline de CD para despliegue en kubernetes
    - Generame un namespace en el cluster de kubernetes desarrollo
    - Generame un namespace en el cluster de kubernetes preproducción
    - Generame un namespace en el cluster de kubernetes producción
    - Generame un proyecto en el ELK para monitorizar los logs de ese microservicio
    - Generame un proyecto en el Prometheus/Grafana para monitorizar las métricas de ese microservicio
    - Generame un cliente en keycloak para gestionar la autenticación de ese microservicio

Evidentemente, si voy a montar 5 proyectos ESTO NO TIENE SENTIDO! Me cuesta más el ajo que la gallina!
Pero si voy a montar 100 proyectos, o 200 proyectos, o 300 proyectos... ESTO ES IMPRESCINDIBLE!


-> Reducir la carga cognitiva de los desarrolladores, y que puedan centrarse en lo que realmente aporta valor: el código de negocio!


Hay muchas estrategias para adoptar una cultura de Ingeniería de plataformas:
- Crearme mi propio IDP y mis propias plantillas de proyecto
    - Backstage
- Adaptarme a un IDP y plantillas de proyecto ya existentes 
    - CoE de Power Platform de Microsoft
- Buscar herramientas que al menos me ayuden a estandarizar y automatizar parte de mi proceso, aunque no me den un IDP ni plantillas de proyecto completas (Ej: Jenkins, Gitlab CI, Azure DevOps, etc...)
    - Templates de Openshift

---

# Ingeniería de plataformas

Al final es una nueva evolución que busca resolver los problemas nuevos que tenemos al trabajar con met. ágiles, DevOps, Cloud, etc... y que nos han llevado a un nuevo caos: el caos federado.

Hay que atacar el problema desde distintos frentes:

- Plantillas:
  - Plantillas de proyecto JAVA / MAVEN (archivos pom.xml... estructura de carpetas...)
  - Plantillas de pipelines de CI (pruebas unitarias, pruebas de sistema, etc...)
  - Plantillas de pipelines de CD (subida a nexus/artifactory, despliegue en kubernetes, etc...)
  - Plantillas para la generación de imágenes de contenedores (caso que trabaje con contenedores)

- Infraestructura/Plataforma
    - Necesito provisionar infra:
      - Para el entorno de producción (kubernetes, cloud, on premise...)
      - Quizás la BBDD la vas a meter en un motor de BBDD corporativo (usuario, contraseña, cuota de uso, etc...)
      - Para el entorno de preproducción (kubernetes, cloud, on premise...)
      - Configuraciones en múltiples herramientas (multi-tenant):
        - Configuración en el ELK para monitorizar los logs de ese microservicio
        - Configuración en el Prometheus/Grafana para monitorizar las métricas de ese microservicio
        - Configuración en keycloak para gestionar la autenticación de ese microservicio

---

# Infraestructura

## IaC

Terraform HCL (Hashicorp Configuration Language) es un lenguaje de programación declarativo, específico para describir infraestructura.
Cloud Formation es un lenguaje de programación declarativo, específico para describir infraestructura en AWS.
Openstack Heat es un lenguaje de programación declarativo, específico para describir infraestructura en Openstack.

Kubernetes es un lenguaje de programación declarativo, específico para describir infraestructura en contenedores.

    Quiero tener un cluster entre 5 y 10 contenedores de tomcat, con tal versión. Con 4 vcores y 12GB de RAM cada uno.
    Que escale cuando el uso de CPU supere el 80% durante más de 5 minutos, y que baje cuando el uso de CPU baje del 50% durante más de 5 minutos.
    Quiero un balanceador de carga que reparta el tráfico entre esos contenedores.
    Quiero un proxy reverso que apunte a ese balanceador de carga, cuando le lleguen peticiones con el nombre de host "mi-microservicio.com"
    Quiero ...

---

# Kubernetes, Terraform, Springboot, Angular, .net, Ansible.

Qué tiene en común? Todas esas herramientas me permiten crear programas!

Kubernetes:
    - Me permite crear scripts (progrmas) que desplieguen / operen / monitoricen aplicaciones en un cluster basado en contenedores.

Terraform:
    - Me permite crear scripts (programas) que desplieguen / gestionen infraestructura en la nube (AWS, Azure, GCP, etc...)

Ansible:
    - Me permite crear scripts (programas) que configuren infraestructura (servidores, redes, etc...)

Springboot, Angular, .net:
    - Me permiten crear aplicaciones(programas) que implementen la lógica de negocio de mis aplicaciones.

Y para crear un programa, los humanos usamos: Lenguajes de programación.

Una cosa es el lenguaje que use.. y otra la forma en la que use ese lenguaje. A esto, los desarrolladores le damos el nombre "hortera" de "estilo de programación" o "paradigma de programación".

## Paradigmas de programación

- Imperativo                Doy instrucciones a la máquina que debe ir ejecutando secuencialmente. 
                            Es el paradigma más básico. Y al que más acostumbrados estamos.
                                JAVA?   Si
                                Python? Si
                                Bash?   Si
                                JS?     Si
                            En ocasiones necesitamos romper la secuencialidad y nos salen als típicas estructuras de control de flujo: if, for, while, etc...

- Procedural                Cuando junto una de esas secuencias de instrucciones en un bloque al que le pongo un nombre.
                            Posteriormente puedo ejecutar ese bloque de instrucciones cada vez que quiera, simplemente llamando a su nombre.
                                JAVA?   Si
                                Python? Si
                                Bash?   Si
                                JS?     Si 
                            Ese bloque de instrucciones al que le he puesto un nombre, lo llamamos función, método, procedimiento, subrutina, etc... dependiendo del lenguaje y del contexto.

                            Que beneficios tiene?
                                - Reusar código
                                - Mejorar la estructura / legibilidad del código
                                - Mejorar las pruebas
                            Esto es una mejora/Evolución del paradigma imperativo, pero sigue siendo un paradigma bastante básico. 

- Funcional                 Cuando un lenguaje me permite que una variable apunte a una función para posterirmente ejecutar 
                            la función desde la variable, entonces el lenguaje soporta el paradigma funcional.
                            Esto es lo que es.
                            El tema no es lo que es... sino lo que puedo hacer cuando un lenguaje soporta ese paradigma.
                            - Puedo crear funciones que acepten otras funciones como parámetros. Inyectar lógica en tiempo de ejecución.
                            - Puedo crear funciones que devuelvan otras funciones. Generar lógica en tiempo de ejecución. = CLOSURES

- Orientada a objetos       Cuando el lenguaje me permite definir mis propios tipos de datos (clases), con sus propiedades concretas y 
                            sus funcionaldiades específicas.
---
- Declarativo

Adoramos el paradigma declarativo. Cada día más. Y cada día odiamos más el paradigma imperativo.
Lo que tienen en común todas las herramientas que hemos mencionado (Kubernetes, Terraform, Ansible, Springboot, Angular, .net) es que son herramientas declarativas.

@Repository de Springboot
@Injectable de Angular
[Service] de .net
fichero de manifiesto de Kubernetes
playbook de Ansible
script de Terraform

Y además... es curioso... porque en lenguaje humano, tenemos el mismo paradigma.

> Felipe, Si (IF ) hay algo que no sea una silla debajo de la ventana, 
>   Quítalo!                                                    Imperativo
> Felipe, IF no hay silla debajo de la ventana:
>   IF not silla (silla == false) GOTO IKEA! compra silla
> Felipe, pon una silla debajo de la ventana                    Imperativo

Cuál es el problema del lenguaje imperativo? Me olvido de lo que quiero, centrándome en el cómo hacerlo. Esto se complica, si quiero conseguir IDEMPOTENCIA!

> Felipe, debajo de la ventana tiene que haber una silla. Es tu responsabilidad.   Declarativo

Aquí no hay órdenes... solo le explico a Felipe cómo son aquí las cosas.
Delego la responsabilidad de conseguir el estado final que me interesa en Felipe... 
Yo me centro en lo que quiero conseguir.. no en como conseguirlo... y dejo que sea Felipe el que se centre en cómo conseguirlo.
---

# Idempotencia

Esto es una propiedad matemática, que dice que una operación es idempotente si el resultado de aplicar esa operación una vez o varias veces es el mismo.                * 1

En el mundo IT lo entendemos de otra forma: 
    Una función/programa es idempotente cuando siempre llego al mismo resultado, independientemente del estado inicial del sistema, o del número de veces que ejecute esa función/programa.

El lenguaje declarativo tiene una peculiaridad ...En si mismo, sin nada adicional es idempotente!
Adoramos el lenguaje declarativo, porque nos permite conseguir idempotencia de forma sencilla.

Todas las herramienats de software que lo petan hoy en día, lo hacen precisamente por el hecho de ser declarativas, y por lo tanto, idempotentes.

Esto, en el mundo de la automatización ( y la ingeniería de plataformas es un paso más allá de la automatización... es estandarizar la automatización) es una propiedad fundamental... necesaria.

Yo monto un script de despliegue de infra... con terraform.

Pregunta: Cuántas veces voy a ejecutar ese script? MOGOLLON!

---
Tendré la V1.0 de mi sistema, que opera en una infra 1.0

Ahora monto la v2.0 de mi sistema, que añade un Redis para cache... pero para eso necesito una v1.1 de mi infra, con una máquina más... para el redis.

    V1.0.0 del software depende de la V1.0.0 de la infra
    V2.0.0 del software depende de la V1.1.0 de la infra

        V1.0.0 del software funcionaría con la v1.1.0 de la infra? SI.. solo que una máquina la tendría parada y sin usar... pero funcionaría.

$ terraform apply # Cuando tenga la v1.0.0 de la infra
$ terraform apply # Cuando tenga la v1.1.0 de la infra

En este caso, la v1.1.0 se monta sobre una v1.0.0, que ya estaba desplegada.
Habrá cosas que se puedan reusar... otras que no... otras que habrá que crear nuevas.
O quizás lo aplico en otro cliente, que no tiene nada desplegado... y entonces el script debe crear TODO!

ME DA IGUAL! Lo que quiero es que independientemente del estado inicial de la infra, cuando se ejecute el script, al final tenga la v1.1.0 de la infra desplegada y funcionando.


---

Un script de terraform es del tipo:

```tf

# Sease en AWS una regla de firewall (grupo de seguridad) que permita el tráfico por tcp puerto 80

resource "aws_security_group" "mi_grupo_seguridad" {
  name        = "mi-grupo-seguridad"
  description = "Grupo de seguridad para mi aplicación"
  vpc_id      = "vpc-12345678"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    }
}

# Sease en AWS una máquina virtual con la imagen ami-0c55b159cbfafe1f0, del tipo t2.micro, y que tenga asignado el grupo de seguridad que acabo de crear.

resource "aws_instance" "mi_maquina" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.mi_grupo_seguridad.name]
}

```

terraform destroy
terraform apply