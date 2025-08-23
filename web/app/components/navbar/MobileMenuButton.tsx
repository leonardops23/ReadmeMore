import React from 'react';
import { Menu, X } from 'lucide-react';

interface MobileMenuButtonProps {
  isOpen: boolean;
  onClick: () => void;
  className?: string;
}

const MobileMenuButton: React.FC<MobileMenuButtonProps> = ({ 
  isOpen, 
  onClick, 
  className = "" 
}) => {
  return (
    <div className="md:hidden">
      <button
        onClick={onClick}
        className={`text-gray-600 hover:text-gray-900 transition-colors duration-200 ${className}`}
        aria-label={isOpen ? "Close menu" : "Open menu"}
      >
        {isOpen ? <X size={24} /> : <Menu size={24} />}
      </button>
    </div>
  );
};

export default MobileMenuButton;
