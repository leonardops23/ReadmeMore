import React from "react";
import Link from "next/link";

interface LinksProps {
  src: String;
  label: String;
}

const LinksAccess: React.FC<LinksProps> = ({
  src,
  label,
}) => {
  return (
    <Link
      href={`${src}`}
    >
      {label}
    </Link>
  )
}

export default LinksAccess;
