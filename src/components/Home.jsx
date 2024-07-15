import HomeS from "./Home.module.css"

function Home(){
    return(
        <div className={HomeS.container}>
            <div className={HomeS.top_container}>
                <h1>Video Game Library</h1>
                <div className={HomeS.top_search}>
                    <img src="src\assets\searchbar.svg"/>
                </div> 
            </div>
            <div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde quaerat facilis ipsum magni inventore quas maiores fugit mollitia aliquam ad cum hic tenetur esse laboriosam nisi quasi, explicabo vero delectus!</div>
            


        </div>
    )
}

export default Home