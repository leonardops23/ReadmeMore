import Link from "next/link";
import React from "react";

interface BootonLinkProps {
  label: String;
}

const BootonLink: React.FC<BootonLinkProps> = ({
  label,
}) => {
  return (
    <Link
      href='#'
      className="bg-black text-white font-semibold p-3 rounded-4xl hover:bg-[#e7c16b] hover:text-black"
    >
      {label}
    </Link>
  )
}

export default BootonLink;
