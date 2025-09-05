import Link from "next/link";
import React from "react";

interface MenuLinksProps {
  label: string;
  onclick?: () => void
}

const MenuLinks: React.FC<MenuLinksProps> = ({
  label,
  onclick,
}) => {
  return (
    <Link href={'#'} onClick={onclick}>
      <div>
        {label}
      </div>
    </Link>
  )
}
