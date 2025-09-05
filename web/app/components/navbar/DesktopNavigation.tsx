import React from 'react';
import NavbarLink from './NavbarLink';
import { navigationItems } from './navigationConfig';
import SignUpModal from '../modals/SignUp';
import LoginModal from '../modals/Login';

const DesktopNavigation: React.FC = () => {

  return (
    <div className="hidden md:flex items-center space-x-8">
      {navigationItems.map((item, index) => {
        return (
          <NavbarLink
            key={index}
            href={item.href || '#'}
            icon={item.icon}
          >
            {item.text}
          </NavbarLink>
        )
      })}
      <div className='space-x-2'>
        <LoginModal />
        <SignUpModal />
      </div>
    </div>
  );
};

export default DesktopNavigation;
