import React from 'react';

const Footer: React.FC = () => {
  const footerLinks = [
    'Help', 'Status', 'About', 'Careers', 'Press', 'Blog', 
    'Privacy', 'Rules', 'Terms', 'Text to speech'
  ];

  return (
    <footer className="bg-[#F7F4ED] border-t border-gray-200 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap justify-center items-center gap-6">
          {footerLinks.map((link, index) => (
            <a
              key={index}
              href="#"
              className="text-sm text-gray-500 hover:text-gray-700 transition-colors duration-200"
            >
              {link}
            </a>
          ))}
        </div>
      </div>
    </footer>
  );
};

export default Footer;
