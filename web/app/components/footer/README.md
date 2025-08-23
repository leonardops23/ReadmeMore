# Footer Components

Esta carpeta contiene todos los componentes relacionados con el footer de la aplicación.

## Estructura

```
footer/
├── index.ts          # Exportaciones centralizadas
├── Footer.tsx        # Componente principal del footer
├── FooterLink.tsx    # Enlace reutilizable del footer
├── FooterSection.tsx # Sección de enlaces del footer
├── SocialIcon.tsx    # Icono de red social
└── README.md         # Esta documentación
```

## Componentes

### Footer
Componente principal que renderiza todo el footer de la página.

### FooterLink
Enlace reutilizable con estilos consistentes y hover effects.

**Props:**
- `href`: URL del enlace
- `children`: Contenido del enlace
- `className`: Clases CSS adicionales (opcional)

### FooterSection
Sección del footer con título y lista de enlaces.

**Props:**
- `title`: Título de la sección
- `children`: Lista de enlaces

### SocialIcon
Icono de red social con configuración personalizable.

**Props:**
- `href`: URL de la red social
- `ariaLabel`: Etiqueta de accesibilidad
- `icon`: SVG del icono
- `hoverColor`: Clase CSS para el color del hover

## Uso

```tsx
import { Footer } from '@/components/footer'

// En tu componente
<Footer />
```

## Ventajas de esta estructura

1. **Organización**: Todos los componentes del footer están en un lugar
2. **Mantenibilidad**: Fácil de encontrar y modificar
3. **Reutilización**: Componentes modulares y reutilizables
4. **Escalabilidad**: Fácil agregar nuevos componentes del footer
5. **Separación de responsabilidades**: Cada componente tiene una función específica
