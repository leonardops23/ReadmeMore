interface FooterSectionProps {
  title: string
  children: React.ReactNode
}

const FooterSection: React.FC<FooterSectionProps> = ({ title, children }) => {
  return (
    <div>
      <h3 className="text-sm font-semibold text-gray-900 tracking-wider uppercase mb-4">
        {title}
      </h3>
      <ul className="space-y-3">
        {children}
      </ul>
    </div>
  )
}

export default FooterSection
