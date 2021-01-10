'use strict';

const e = React.createElement;

class SayHi extends React.Component {
  constructor(props) {
    super(props);
    this.state = { clicked: false };
  }

  render() {
    if (this.state.clicked) {
      return 'Hello World';
    }

    return e(
      'button',
      { onClick: () => this.setState({ clicked: true }),
      class:'reactBtn' },
      'Saludar'
    );
  }
}
const domContainer = document.querySelector('#reactDiv');
ReactDOM.render(e(SayHi), domContainer);