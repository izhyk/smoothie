import * as React from 'react';

import axios from 'axios';
import {MainPage} from "../../components/MainPage/MainPage";

export default class MainPageContainer extends React.Component {
    public state = {
        data: ''
    };

  public componentDidMount() {
    axios.get(`http://localhost:8080/`)
      .then(res => {
        const data = res.data;
        this.setState({ data: data.text });
      })
  }

  public render() {
    return (
      <MainPage text={this.state.data}/>
    )
  }
}
