import {Link} from 'react-router-dom';

const Navbar = () => {
    return (
        <>
        <h1>This is the navebar</h1>
        <Link to="/">Home</Link>
        <Link to="/create">New Blog</Link>
        </>
      );
}
 
export default Navbar;