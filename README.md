# Prime-Calculator API 🚀

Este proyecto consiste en una API desarrollada en Python para el cálculo y verificación de números primos. Su objetivo principal es demostrar el ciclo de vida completo de una funcionalidad ("feature") aplicando la metodología BLOW (BDD Layered Organization of Work).

## 🎯 Propósito del Proyecto

Simular el flujo de trabajo desde la concepción de una idea de negocio (ej. descuentos basados en fechas primas) hasta su despliegue automatizado en producción, garantizando calidad en cada etapa mediante los 4 Cuadrantes de Agile Testing.

## 📂 Estructura del Proyecto (Modularidad Orientada al Dominio)

Siguiendo las buenas prácticas de gestión de configuración:

- **`/src/backend`**: Código fuente de la API.
- **`/src/backend/tests`**: Suite de pruebas organizada por niveles.
- **`.github/workflows`**: Definición de los pipelines de CI/CD.

## 🧪 Estrategia de Pruebas (Agile Testing Quadrants)

### Q1: Unit Testing (Tecnología / Soporte)

- **Enfoque**: Lógica matemática del algoritmo de números primos.
- **Metodología**: TDD (Test-Driven Development) siguiendo el ciclo Fallo-Paso-Refactor.
- **Herramienta**: pytest.

### Q2: Acceptance Testing (Negocio / Soporte)

- **Enfoque**: Comportamiento de la API desde el punto de vista del usuario.
- **Metodología**: ATDD (Acceptance Test-Driven Development) y BDD.
- **Práctica**: "The Three Amigos" para definir escenarios en Gherkin.

### Q3: Exploratory Testing (Negocio / Crítica)

- **Enfoque**: Pruebas manuales y feedback del producto en entornos de Staging.
- **Herramienta**: Monitorización proactiva de interacciones de usuario.

### Q4: Technical Testing (Tecnología / Crítica)

- **Seguridad**: Análisis estático (SAST) y de composición (SCA) para evitar vulnerabilidades.
- **Rendimiento**: Pruebas de carga (Load Testing) para asegurar la estabilidad bajo picos de tráfico.

## 🌿 Gestión de Ramas y Git

Utilizamos un modelo de Domain Oriented Branching:

- **`main`**: Rama de producción (PROD). Protección activada: requiere PR y paso de tests.
- **`dev`**: Rama de integración.
- **`feat/*`**: Ramas de corta duración para funcionalidades específicas.

## 🚀 Pipeline CI/CD (GitHub Actions)

El flujo de automatización incluye:

- **Build**: Compilación y preparación del entorno.
- **Test**: Ejecución de Q1 y Q2 en cada push y pull_request.
- **Security Check**: Escaneo de dependencias y código.
- **Deploy**: Despliegue continuo a Staging/Producción.

## 📊 Métricas DORA

El éxito del proceso se mide mediante:

- **Lead Time for Changes**: Tiempo desde el primer commit hasta el despliegue en verde.
- **Deployment Frequency**: Frecuencia de entregas exitosas.
