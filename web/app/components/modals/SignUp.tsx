import NavbarButton from '@/app/components/navbar/NavbarButton';
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTrigger,
  DialogTitle,
} from '@/components/ui/dialog'

const SignUpModal = () => {
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

          <form className="space-y-4 mt-4">
            <input
              type="text"
              placeholder="First and last name"
              className="w-full px-4 py-2 border rounded-lg focus:outline-none"
            />
            <input
              type="text"
              placeholder="User"
              className="w-full px-4 py-2 border rounded-lg focus:outline-none"
            />
            <input
              type="email"
              placeholder="Email"
              className="w-full px-4 py-2 border rounded-lg focus:outline-none"
            />
            <input
              type="password"
              placeholder="Contraseña"
              className="w-full px-4 py-2 border rounded-lg focus:outline-none"
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
