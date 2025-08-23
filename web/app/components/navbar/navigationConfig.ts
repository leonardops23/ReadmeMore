import { PenTool } from 'lucide-react';

export interface NavigationItem {
  href: string;
  text: string;
  icon?: any;
}

export const navigationItems: NavigationItem[] = [
  { href: "#", text: "Our story" },
  { href: "#", text: "Membership" },
  { href: "#", text: "Write", icon: PenTool },
  { href: "#", text: "Sign in" },
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
