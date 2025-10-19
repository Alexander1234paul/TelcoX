#  Reto de Desarrollo Fullstack – TelcoX

##  Descripción del Proyecto
Este proyecto fue desarrollado como parte del **Reto de Desarrollo Fullstack para una empresa de telecomunicaciones (TelcoX)**.  
El objetivo principal fue diseñar e implementar una **plataforma de autogestión** que permita a los clientes visualizar su consumo, saldo, minutos y datos en tiempo real, simulando la integración con un sistema BSS.

La idea es ofrecer una solución moderna, escalable y fácil de usar que optimice la atención al cliente y reduzca la carga de soporte técnico.

---

##  Objetivos del Desarrollo
Durante el desarrollo del reto se trabajó con un enfoque completo **Fullstack**, abarcando:

### Módulo de Visualización de Consumo
- Implementé un módulo que muestra el consumo de datos, saldo y minutos de un cliente en tiempo real.
- Este módulo se conecta con un **backend ficticio (API REST Flask)** que simula la respuesta de un sistema BSS.
- Se diseñó una **interfaz simple e intuitiva** en Angular para que el usuario pueda visualizar su información rápidamente.

### 4️ Despliegue con Docker
- Se configuró un entorno Docker completo con tres servicios:
  - **MySQL**: Base de datos principal.
  - **Flask Backend**: API REST.
  - **Angular Frontend + Nginx**: Interfaz de usuario productiva.
- La orquestación se realiza mediante **docker-compose** para un despliegue rápido y portable.

---

## Tecnologías Utilizadas

### **Frontend**
- Angular 17  
- TypeScript  
- Bootstrap 5 / CSS3  
- Angular Material  

### **Backend**
- Python 3.10  
- Flask  
- Flask-SQLAlchemy  
- Flask-CORS  
- PyMySQL  
- Pytest  

### **Infraestructura**
- Docker  
- Docker Compose  
- MySQL 8.0  
- Nginx  

---

##  Configuración y Ejecución

###  Requisitos previos
- Docker y Docker Compose instalados  
- Puerto 4200 (frontend) y 5000 (backend) disponibles  

###  Levantar todo el entorno
```bash
docker-compose up --build
