"use client";

import React from 'react';
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger
} from '@/components/ui/dialog';
import { NavbarButton } from '../navbar';
import { useState } from 'react';


const LoginModal: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  async function handleLogin(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();

    console.log('Email:', email);
    console.log('Password:', password);
  }
  
  return (
    <Dialog>
      <DialogTrigger>
          <NavbarButton>
            Ingresar
          </NavbarButton>
        </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Iniciar sesión</DialogTitle>
        </DialogHeader>
        <form className="space-y-4 mt-4" onSubmit={handleLogin}>
            <input
              type="email"
              placeholder="Email"
              className="w-full px-4 py-2 border rounded-lg focus:outline-none"
              onChange={(e) => setEmail(e.target.value)}
            />
            <input
              type="password"
              placeholder="Contraseña"
              className="w-full px-4 py-2 border rounded-lg focus:outline-none"
              onChange={(e) => setPassword(e.target.value)}
            />
            <button
              type="submit"
              className="w-full bg-secondary-button py-2 rounded-lg cursor-pointer hover:bg-primary hover:text-accent transition-all shadow-sm"
            >
              Iniciar sesión
            </button>
          </form>
      </DialogContent>
    </Dialog>
  );
};

export default LoginModal;
