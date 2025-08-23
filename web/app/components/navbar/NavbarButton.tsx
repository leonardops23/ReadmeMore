import React from 'react';

interface NavbarButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  className?: string;
  isMobile?: boolean;
  type?: 'button' | 'submit';
}

const NavbarButton: React.FC<NavbarButtonProps> = ({ 
  children, 
  onClick, 
  className = "", 
  isMobile = false,
  type = 'button'
}) => {
  const baseClasses = "bg-gray-900 text-white px-4 py-2 rounded-full text-sm font-medium hover:bg-gray-800 transition-colors duration-200";
  const mobileClasses = isMobile ? "w-full mt-4" : "";
  const finalClasses = `${baseClasses} ${mobileClasses} ${className}`;

  return (
    <button 
      type={type}
      onClick={onClick} 
      className={finalClasses}
    >
      {children}
    </button>
  );
};

export default NavbarButton;
