import Image from 'next/image';
import React from 'react';

interface NavbarLogoProps {
  src: string;
  className?: string;
}

const NavbarLogo: React.FC<NavbarLogoProps> = ({ 
  src,
  className,
}) => {
  return (
    <div className="flex items-center">
      <Image
        alt='logo-auris-bg-preview'
        src={src}
        width={100}
        height={100}
        className={className}
        unoptimized
      />
    </div>
  );
};

export default NavbarLogo;
