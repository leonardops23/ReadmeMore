import React from 'react';

interface NavbarLogoProps {
  text?: string;
  className?: string;
}

const NavbarLogo: React.FC<NavbarLogoProps> = ({ 
  text = "Medium", 
  className = "text-3xl font-bold text-gray-900 tracking-tight" 
}) => {
  return (
    <div className="flex items-center">
      <h1 className={className}>{text}</h1>
    </div>
  );
};

export default NavbarLogo;
