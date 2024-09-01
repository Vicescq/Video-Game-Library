import NavBarS from "./NavBar.module.css"
import { useEffect, useState, useRef } from "react"

function NavBar(){
    const [dropdown, setDropdown] = useState(false)
    const navref = useRef(null)
    const dropdownimgref = useRef(null)

    useEffect(() => {
        let dropdown_handler = (e) => {
            if(e.target == dropdownimgref.current){
                setDropdown(!dropdown)
            }
            
            if(!navref.current.contains(e.target)){
                setDropdown(false)
            }
        }
        document.addEventListener("mousedown", dropdown_handler)
        return () => {
            document.removeEventListener("mousedown", dropdown_handler)
        }
    }, [dropdown])

    return(

        <nav ref={navref}>
            <div className={NavBarS.container}>
                <img src="src\assets\controller.svg"/>
                <div className={NavBarS.title}>Library</div>
            </div>
            
            <div className={NavBarS.container}>
                <ul className={NavBarS.expandedmenu}>
                    <li><img className={NavBarS.searchbarimg} src="src\assets\searchbar.svg"/></li>
                    <li><img src="src\assets\sort.svg"/></li>
                </ul>
                <div className={NavBarS.dropdownmenu_cont}>
                    <img src="src\assets\dropdown.svg" ref={dropdownimgref}/>
                    {
                        dropdown ?
                        <ul className={NavBarS.dropdownmenu}>
                            <li>dakdsakldsajlk</li>
                            <li>dakdsakldsajlk</li>
                            <li>dakdsakldsajlk</li>
                        </ul>
                        :null
                    }
                </div>
            </div>
        </nav>

    )
}

export default NavBar