import * as React from 'react';


interface IProps {
    text: string
}

export const MainPage: React.FunctionComponent<IProps> = ({ text }) => {
    return (
      <h1>{text}</h1>
    )
};
