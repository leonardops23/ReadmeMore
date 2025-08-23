import React from 'react';
import NavbarLink from './NavbarLink';
import NavbarButton from './NavbarButton';
import { navigationItems } from './navigationConfig';

interface MobileNavigationProps {
  isOpen: boolean;
}

const MobileNavigation: React.FC<MobileNavigationProps> = ({ isOpen }) => {

  if (!isOpen) return null;

  return (
    <div className="md:hidden bg-[#F7F4ED] border-t border-gray-200">
      <div className="px-4 py-4 space-y-3">
        {navigationItems.map((item, index) => (
          <NavbarLink 
            key={index}
            href={item.href} 
            icon={item.icon}
            isMobile={true}
          >
            {item.text}
          </NavbarLink>
        ))}
        <NavbarButton isMobile={true}>Get started</NavbarButton>
      </div>
    </div>
  );
};

export default MobileNavigation;
