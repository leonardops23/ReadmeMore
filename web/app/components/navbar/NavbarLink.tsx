import React from 'react';
import { LucideIcon } from 'lucide-react';

interface NavbarLinkProps {
  href: string;
  children: React.ReactNode;
  icon?: LucideIcon;
  className?: string;
  isMobile?: boolean;
}

const NavbarLink: React.FC<NavbarLinkProps> = ({ 
  href, 
  children, 
  icon: Icon, 
  className = "", 
  isMobile = false 
}) => {
  const baseClasses = isMobile 
    ? "block text-gray-600 hover:text-gray-900 transition-colors duration-200 text-sm"
    : "text-gray-600 hover:text-gray-900 transition-colors duration-200 text-sm";
  
  const finalClasses = Icon 
    ? `${baseClasses} flex items-center gap-1` 
    : baseClasses;

  return (
    <a href={href} className={`${finalClasses} ${className}`}>
      {Icon && <Icon size={16} />}
      {children}
    </a>
  );
};

export default NavbarLink;
