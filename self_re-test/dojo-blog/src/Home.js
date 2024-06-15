import BlogList from './BlogList';
import useFetch from './useFetch';

const Home = () => {

    const {data: blogs, ispending, error} = useFetch('http://localhost:8000/blogs');
    // let name = "Sese"

    // const [name,setName] = useState('Sese');
    // const [age, setAge] = useState(25);


    // const handleClick = () => {
    //     // console.log("Hello my people")
    //     // name = 'Shawn'
    //     // console.log(name)
    //     setName('Justice')
    //     setAge(30)
    // }

    // const handleClickAgain = (name,e) => {
    //     console.log('Hello ' + name, e.target);
    // }

    // const [blogs, setBlogs] = useState(null);
    // const [ispending, setIsPending] = useState(true);
    // const [error, setError] = useState(null);

    // const [name, setName] = useState("mario");

    // const handleDelete = (id) => {
    //     const newBlogs = blogs.filter(blog => blog.id !== id);
    //     setBlogs(newBlogs);
    // }

    // useEffect(()=>{
    //     console.log('use effect ran');
    //     console.log(name);
    // }, [name]);

    // useEffect(() => {
    //     setTimeout(() => {
    //         fetch("http://localhost:8000/blogs")
    //             .then(res => {
    //                 if(!res.ok) {
    //                     throw Error('Could not fetch the data for that resource');
    //                 }
    //                 return res.json();
    //             })
    //             .then(data => {
    //                 setBlogs(data);
    //                 setIsPending(false);
    //                 setError(null);
    //             })
    //             .catch((e) => {
    //                 setIsPending(false);
    //                 setError(e.message);
    //             });
    //     }, 1000);
    // }, []);


    return ( 
        <>
        {/* <h1>Yo yo yo</h1>
        <p>{name} is {age} years old</p>
        <button onClick={handleClick}>Click Me</button>
        <button onClick={(e) => handleClickAgain('Shawn',e)}>Click me Again</button> */}

        <div className="home">
            {error && <div>{error}</div>}
            {ispending && <div>Loading...</div>}
            {blogs && <BlogList blogs={blogs} title="All Blogs"/>}
            {/* {blogs && <BlogList blogs={blogs} title="All Blogs" handleDelete={handleDelete}/>} */}

            {/* <BlogList blogs={blogs.filter((blog)=> blog.author === 'mario')} title="Mario's Blogs" /> */}
        </div>
        {/* <p>{name}</p>
        <button onClick={()=> setName('luigi')}>change name</button> */}
        </>
     );
}
 
export default Home;