import { PenTool } from 'lucide-react';

export interface NavigationItem {
  href?: string;
  text: string;
  icon?: any;
  component?: React.ReactNode;
}

export const navigationItems: NavigationItem[] = [
  { href: "#", text: "Nuesta historia" },
  { href: "#", text: "Membership" },
  { href: "#", text: "Escritores", icon: PenTool },
];

export const navbarConfig = {
  logo: {
    text: "Medium",
    className: "text-3xl font-bold text-gray-900 tracking-tight"
  },
  theme: {
    backgroundColor: "bg-[#F7F4ED]",
    borderColor: "border-gray-200"
  }
};
