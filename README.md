# 🐍 Automatización de Pruebas - AutomationExercise.com  
**Python + Playwright + Behave**

---

## 📋 Descripción del Proyecto

Este proyecto de automatización de pruebas está diseñado para verificar la funcionalidad del sitio web [AutomationExercise.com](https://www.automationexercise.com/). Utiliza un stack moderno de herramientas que incluye **Playwright** para la interacción con el navegador y **Behave** para la implementación de pruebas basadas en comportamiento (BDD).

### 🛠 Tecnologías Utilizadas
- **Python** - Lenguaje de programación principal
- **Playwright** - Framework de automatización de navegadores
- **Behave** - Framework BDD (Behavior Driven Development)
- **HTML Reports** - Generación de reportes ejecutivos

---

## 🚀 ¿ Cómo ejecutar las pruebas ?


### Prerrequisitos
- Python 3.8 o superior
- Acceso a internet para descargar dependencias y ejecutar pruebas

### ⚙️ Configuración

#### 🐧 Linux / macOS
```bash
# Instalar soporte para entornos virtuales
sudo apt install python3-venv -y

# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Instalar navegadores para Playwright
playwright install
```


#### 🖥️ Windows
```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
.venv\Scripts\activate.bat

# Instalar dependencias
pip install -r requirements.txt

# Instalar navegadores para Playwright
playwright install
```

### 🧪 Comandos de ejecución de Pruebas

#### ▶️ Ejecución Básica
```bash
behave
```
#### 📊 Ejecución con Reporte HTML
```bash
behave -v --no-capture -f behave_html_formatter:HTMLFormatter -o reports/report.html
```
