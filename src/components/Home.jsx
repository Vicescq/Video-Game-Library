import HomeS from "./Home.module.css"
import NavBar from "./NavBar.jsx"

function Home(){
    return(
        <>
        <NavBar/>
        <div className={HomeS.container}>
            <div className={HomeS.status}>
                <div><span>All</span></div>
                <div><span>Current</span></div>
                <div><span>Paused</span></div>
                <div><span>Dropped</span></div>
                <div><span>Done</span></div>
            </div>
            <table>
                <thead>
                    <tr >
                        <th scope="col">#</th>
                        <th scope="col">Image</th>
                        <th scope="col">Title</th>
                        <th scope="col">Score</th>
                        <th scope="col">Status</th>
                        <th scope="col">Notes</th>
                    </tr>
                    <tr>
                        <td>a</td>
                        <td>a</td>
                        <td>a</td>
                        <td>a</td>
                        <td>a</td>
                        <td>a</td>
                    </tr>
                    
                </thead>
                <tbody></tbody>
            </table>

        </div>
        </>
    )
}

export default Home