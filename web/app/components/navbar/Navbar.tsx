import React from 'react';
import NavbarLogo from './NavbarLogo';
import DesktopNavigation from './DesktopNavigation';
import MobileNavigation from './MobileNavigation';
import MobileMenuButton from './MobileMenuButton';
import { navbarConfig } from './navigationConfig';


interface NavbarProps {
  isMobileMenuOpen: boolean;
  setIsMobileMenuOpen: (open: boolean) => void;
}

const Navbar: React.FC<NavbarProps> = ({ isMobileMenuOpen, setIsMobileMenuOpen }) => {
  const toggleMobileMenu = () => setIsMobileMenuOpen(!isMobileMenuOpen);

  return (
    <nav className={`${navbarConfig.theme.backgroundColor} border-b ${navbarConfig.theme.borderColor} sticky top-0 z-50`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <NavbarLogo 
            src='/logo-auris-bg-preview.png'
            className=''
          />

          {/* Desktop Navigation */}
          <DesktopNavigation />

          {/* Mobile menu button */}
          <MobileMenuButton 
            isOpen={isMobileMenuOpen}
            onClick={toggleMobileMenu}
          />
        </div>
      </div>

      {/* Mobile Navigation */}
      <MobileNavigation isOpen={isMobileMenuOpen} />
    </nav>
  );
};

export default Navbar;
