# Navbar Components

Esta carpeta contiene una estructura modular y reutilizable para el navbar de la aplicación.

## Estructura de Archivos

```
navbar/
├── index.ts                 # Exportaciones principales
├── Navbar.tsx              # Componente principal del navbar
├── NavbarLogo.tsx          # Componente del logo
├── NavbarLink.tsx          # Componente de enlaces de navegación
├── NavbarButton.tsx        # Componente de botones
├── DesktopNavigation.tsx   # Navegación para escritorio
├── MobileNavigation.tsx    # Navegación para móvil
├── MobileMenuButton.tsx    # Botón del menú móvil
├── navigationConfig.ts     # Configuración centralizada
└── README.md               # Esta documentación
```

## Componentes

### Navbar
Componente principal que orquesta todos los elementos del navbar.

### NavbarLogo
Componente reutilizable para el logo, acepta texto y clases personalizadas.

### NavbarLink
Componente para enlaces de navegación con soporte para iconos y estilos móviles/desktop.

### NavbarButton
Componente para botones con estilos consistentes y soporte para móvil.

### DesktopNavigation
Navegación visible solo en pantallas de escritorio.

### MobileNavigation
Navegación visible solo en dispositivos móviles.

### MobileMenuButton
Botón para abrir/cerrar el menú móvil.

## Configuración

El archivo `navigationConfig.ts` centraliza:
- Elementos de navegación
- Configuración del logo
- Temas y colores

## Uso

```tsx
import { Navbar } from '@/components/navbar';

// En tu componente
const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

<Navbar 
  isMobileMenuOpen={isMobileMenuOpen}
  setIsMobileMenuOpen={setIsMobileMenuOpen}
/>
```

## Ventajas de esta Estructura

1. **Modularidad**: Cada componente tiene una responsabilidad específica
2. **Reutilización**: Los componentes pueden usarse en otros lugares
3. **Mantenibilidad**: Cambios en un componente no afectan otros
4. **Configurabilidad**: Fácil personalización desde un archivo central
5. **Separación de Responsabilidades**: Desktop y móvil están separados
6. **TypeScript**: Tipado completo para mejor desarrollo
