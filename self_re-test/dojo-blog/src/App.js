import './App.css';
import Navbar from './Navbar';
import Home from './Home';
import Create from './Create';
import BlogDetails from './BlogDetails';
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import NotFound from './NotFound';

function App() {
  // const dynamicValue = "This is from shaun"
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className='content'>
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/create">
            <Create/>
          </Route>
          <Route path="/blogs/:id">
            <BlogDetails/>
          </Route>
          <Route path="*">
            <NotFound />
          </Route>
        </Switch>
        {/* <h1>Hello World</h1>
        <p>{dynamicValue}</p> */}
      </div>
    </div>
    </Router>
  );
}

export default App;
