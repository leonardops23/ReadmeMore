import React from 'react';
import NavbarLink from './NavbarLink';
import NavbarButton from './NavbarButton';
import { navigationItems } from './navigationConfig';

const DesktopNavigation: React.FC = () => {

  return (
    <div className="hidden md:flex items-center space-x-8">
      {navigationItems.map((item, index) => (
        <NavbarLink 
          key={index}
          href={item.href} 
          icon={item.icon}
        >
          {item.text}
        </NavbarLink>
      ))}
      <NavbarButton>Get started</NavbarButton>
    </div>
  );
};

export default DesktopNavigation;
