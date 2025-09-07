"use client";

import NavbarButton from '@/app/components/navbar/NavbarButton';
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTrigger,
  DialogTitle,
} from '@/components/ui/dialog'
import React, { useState } from 'react';
import { register } from '@/app/services/auth';


const SignUpModal = () => {
  const [formData, setFormData] = useState({
    email: '',
    first_name: '',
    last_name: '',
    password: '',
    password_confirmation: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleRegister = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await register(formData);
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
      <Dialog>
        <DialogTrigger>
          <NavbarButton>
            Get started
          </NavbarButton>
        </DialogTrigger>
        <DialogContent className="sm:max-w-md">
          <DialogHeader>
            <DialogTitle>Crear cuenta</DialogTitle>
          </DialogHeader>
          <form className="space-y-4 mt-4" onSubmit={handleRegister}>
            <input
              type="text"
              placeholder="Nombre"
              name="first_name"
              className="w-full px-4 py-2 border rounded-lg focus:outline-none"
              onChange={(e) => handleChange(e)}
              value={formData.first_name}
            />
            <input
              type="text"
              placeholder="Apellido"
              name="last_name"
              className="w-full px-4 py-2 border rounded-lg focus:outline-none"
              onChange={(e) => handleChange(e)}
              value={formData.last_name}
            />
            <input
              type="email"
              placeholder="Email"
              name="email"
              className="w-full px-4 py-2 border rounded-lg focus:outline-none"
              onChange={(e) => handleChange(e)}
              value={formData.email}
            />
            <input
              type="password"
              placeholder="Contraseña"
              name="password"
              className="w-full px-4 py-2 border rounded-lg focus:outline-none"
              onChange={(e) => handleChange(e)}
              value={formData.password}
            />
            <input
              type="password"
              placeholder="Confirmar contraseña"
              name="password_confirmation"
              className="w-full px-4 py-2 border rounded-lg focus:outline-none"
              onChange={(e) => handleChange(e)}
              value={formData.password_confirmation}
            />
            <button
              type="submit"
              className="w-full bg-secondary-button py-2 rounded-lg cursor-pointer hover:bg-primary hover:text-accent transition-all shadow-sm"
            >
              Registrarse
            </button>
          </form>
        </DialogContent>
      </Dialog>
    </>
  )
}

export default SignUpModal;
