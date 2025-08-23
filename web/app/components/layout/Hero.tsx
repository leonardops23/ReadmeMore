import React from 'react';

const Hero: React.FC = () => {
  return (
    <section className="min-h-[80vh] flex items-center">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Content */}
          <div className="lg:pr-8">
            <h1 className="text-6xl sm:text-7xl lg:text-8xl font-bold text-gray-900 leading-tight mb-6">
              Entre
              <br />
              <span className="italic">historias</span> e ideas
            </h1>
            <p className="text-xl sm:text-2xl text-gray-600 mb-8 leading-relaxed max-w-lg">
              Un espacio para compartir experiencias que inspiran y pensamientos que transforman.
            </p>
            <button className="bg-gray-900 text-white px-8 py-4 rounded-full text-lg font-medium hover:bg-gray-800 transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl">
              Start reading
            </button>
          </div>

          {/* Decorative Image */}
          <div className="relative lg:block hidden">
            <div className="relative w-full h-96">
              {/* Background shapes */}
              <div className="absolute top-0 right-0 w-72 h-72 bg-green-400 rounded-full opacity-20 animate-pulse"></div>
              <div className="absolute bottom-0 left-0 w-48 h-48 bg-green-500 rounded-lg rotate-12 opacity-30"></div>
              <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-64 h-64">
                <img
                  src="/img-main-layaut-removebg-preview.png"
                  alt="Decorative illustration"
                  className="w-full h-full object-cover rounded-2xl shadow-2xl"
                />
              </div>
              {/* Geometric elements */}
              <div className="absolute top-8 left-8 w-4 h-4 bg-gray-900 transform rotate-45"></div>
              <div className="absolute bottom-8 right-8 w-3 h-3 bg-green-500 rounded-full"></div>
              <div className="absolute top-1/3 right-12 w-2 h-2 bg-gray-600 rounded-full"></div>
              <div className="absolute bottom-1/3 left-12 w-2 h-2 bg-green-600 rounded-full"></div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
