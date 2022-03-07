import React from "react";
import styled from '@emotion/styled'

const Button = styled.button`
  padding: 4px;
  cursor: pointer;
  background-color: #FB6C6B;
  font-size: 14px;
  border-radius: 4px;
  color: black;
  font-weight: bold;
  &:hover {
    color: white;
  }
`

interface Props {
    children?: React.ReactNode;
    onClick: () => void;
}

const ActionButton: React.FC<Props> = ({
    children,
    onClick,
  }) => { 
  return (
    <Button 
      onClick={onClick}
    >
    {children}
    </Button>
  );
}

export default ActionButton;
