# Diseño y desarrollo de una API REST para gestión de cuentas bancarias

La empresa necesita una API REST para gestionar cuentas bancarias. Los clientes podrán crear, consultar, actualizar y eliminar cuentas. La API debe asegurar la integridad de los datos y manejar adecuadamente los errores. El dominio de la banca requiere que las operaciones sean idempotentes y que se maneje la consistencia de los datos en caso de fallos temporales. Los clientes se autenticarán mediante JWT.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | API REST en dominio de banca |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de endpoints y modelos de datos

**Objetivo:** Definir los endpoints necesarios y los modelos de datos para la gestión de cuentas bancarias.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar los endpoints necesarios para crear, consultar, actualizar y eliminar cuentas bancarias.
- Definir los modelos de datos necesarios para representar una cuenta bancaria.
- Asegurar que los modelos de datos incluyan validaciones adecuadas para los campos requeridos.

**Entregable:** Documentación de los endpoints y modelos de datos definidos.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los atributos necesarios para una cuenta bancaria (número de cuenta, saldo, titular, etc.).
- Piensa en las validaciones necesarias para asegurar la integridad de los datos.

</details>

### Fase 2: Implementación de endpoints y manejo de errores

**Objetivo:** Implementar los endpoints definidos y manejar adecuadamente los errores.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Implementar los endpoints para crear, consultar, actualizar y eliminar cuentas bancarias.
- Asegurar que los endpoints manejen adecuadamente los errores y devuelvan respuestas apropiadas.
- Implementar la autenticación mediante JWT para asegurar que solo usuarios autorizados puedan acceder a los endpoints.

**Entregable:** Endpoints implementados y autenticación mediante JWT.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los posibles errores que pueden ocurrir al interactuar con la base de datos y cómo manejarlos.
- Piensa en cómo implementar la autenticación mediante JWT de manera segura.

</details>

### Fase 3: Pruebas y optimización

**Objetivo:** Realizar pruebas unitarias y de integración para asegurar la funcionalidad y optimizar el rendimiento de la API.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Realizar pruebas unitarias para cada endpoint implementado.
- Realizar pruebas de integración para asegurar que los endpoints funcionen correctamente en conjunto.
- Optimizar el rendimiento de la API identificando y solucionando posibles cuellos de botella.

**Entregable:** Pruebas unitarias y de integración realizadas, y rendimiento optimizado.

<details>
<summary>Pistas de conocimiento</summary>

- Considera diferentes escenarios de prueba para asegurar la funcionalidad de la API.
- Piensa en cómo identificar y solucionar posibles cuellos de botella en el rendimiento.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una API REST y para qué se utiliza en el dominio de la banca?
- **paraQueSirve**: ¿Para qué sirven los endpoints definidos en la API?
- **comoSeUsa**: ¿Cómo se utilizan los modelos de datos en la API para representar una cuenta bancaria?
- **erroresComunes**: ¿Cuáles son los errores comunes que pueden ocurrir al interactuar con la base de datos y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica la implementación de la autenticación mediante JWT y cómo afectan al diseño de la API?

## Criterios de Evaluacion

- Definición correcta de endpoints y modelos de datos para la gestión de cuentas bancarias.
- Implementación adecuada de los endpoints y manejo de errores.
- Autenticación segura mediante JWT.
- Realización de pruebas unitarias y de integración para asegurar la funcionalidad de la API.
- Optimización del rendimiento de la API.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
