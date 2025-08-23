import Link from "next/link"

interface FooterLinkProps {
  href: string
  children: React.ReactNode
  className?: string
}

const FooterLink: React.FC<FooterLinkProps> = ({ 
  href, 
  children, 
  className = "text-gray-600 hover:text-blue-600 transition-colors duration-200 block" 
}) => {
  return (
    <Link href={href} className={className}>
      {children}
    </Link>
  )
}

export default FooterLink
