"use client";

import React from 'react';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog';

const LoginModal: React.FC = () => {
  return (
    <Dialog>
      <DialogTrigger>
        <span className="text-gray-600 hover:text-gray-900 transition-colors duration-200 text-sm">Ingresar</span>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Iniciar sesión</DialogTitle>
        </DialogHeader>
        <div className="flex flex-col gap-3">
          {/* Replace with your real login form */}
          <input className="border rounded px-3 py-2" placeholder="Email" />
          <input className="border rounded px-3 py-2" type="password" placeholder="Password" />
          <button className="bg-gray-900 text-white px-4 py-2 rounded-full text-sm font-medium hover:bg-gray-800 transition-colors duration-200">Entrar</button>
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default LoginModal;


