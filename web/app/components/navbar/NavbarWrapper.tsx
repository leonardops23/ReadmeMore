'use client';

import React, { useState } from 'react';
import Navbar from './Navbar';

const NavbarWrapper: React.FC = () => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  return (
    <Navbar 
      isMobileMenuOpen={isMobileMenuOpen}
      setIsMobileMenuOpen={setIsMobileMenuOpen}
    />
  );
};

export default NavbarWrapper;
