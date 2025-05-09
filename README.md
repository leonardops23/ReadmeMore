# Sistema de Ventas React + PostgreSQL

## 📋 Descripción
Sistema de gestión de ventas desarrollado con React y PostgreSQL, diseñado para administrar inventario, ventas y clientes de manera eficiente.

## 🚀 Tecnologías Utilizadas
- React
- Vite
- PostgreSQL
- Node.js

## 🛠️ Estructura del Proyecto
```
SistemadeVentas-react-postql/
├── public/
│   └── vite.svg
├── src/
│   ├── components/      # Componentes reutilizables
│   ├── pages/          # Páginas de la aplicación
│   ├── utils/          # Utilidades y helpers
│   ├── assets/         # Recursos estáticos
│   ├── App.jsx         # Componente principal
│   ├── App.css         # Estilos del componente principal
│   ├── main.jsx        # Punto de entrada
│   └── index.css       # Estilos globales
├── package.json        # Dependencias y scripts
├── vite.config.js      # Configuración de Vite
└── .gitignore         # Archivos ignorados por Git
```

## ⚙️ Instalación

1. Clonar el repositorio:
```bash
git clone [URL del repositorio]
```

2. Instalar dependencias:
```bash
npm install
```

3. Configurar variables de entorno:
Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
```env
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=nombre_base_datos
```

## 🚀 Uso

1. Iniciar el servidor de desarrollo:
```bash
npm run dev
```

2. Abrir el navegador en `http://localhost:5173`

## 🤝 Contribución
1. Hacer un Fork del proyecto
2. Crear una nueva rama (`git checkout -b feature/nueva-caracteristica`)
3. Hacer commit de los cambios (`git commit -m 'Añadir nueva característica'`)
4. Hacer push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abrir un Pull Request

## 📄 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
