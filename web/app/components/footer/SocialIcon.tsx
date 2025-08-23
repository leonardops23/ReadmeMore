interface SocialIconProps {
  href: string
  ariaLabel: string
  icon: React.ReactNode
  hoverColor: string
}

const SocialIcon: React.FC<SocialIconProps> = ({ 
  href, 
  ariaLabel, 
  icon, 
  hoverColor 
}) => {
  return (
    <a 
      href={href} 
      aria-label={ariaLabel}
      className={`text-gray-400 ${hoverColor} transition-colors duration-200`}
    >
      {icon}
    </a>
  )
}

export default SocialIcon
