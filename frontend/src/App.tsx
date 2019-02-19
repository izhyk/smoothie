import * as React from 'react';
import './App.css';
import MainPageContainer from "./containers/MainPageContainer/MainPageContainer";

class App extends React.Component {
  public render() {
    return (
      <div className="App">
        <MainPageContainer />
      </div>
    );
  }
}

export default App;
