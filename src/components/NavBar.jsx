import { useEffect } from "react"
import NavBarS from "./NavBar.module.css"
import { useState, useRef } from "react"

function NavBar(){
    const [dropdown, setDropdown] = useState(false)
    const navref = useRef(null)
    const dropdownref = useRef(null)

    useEffect(() => {
        let dropdown_handler = (e) => {
            if(e.target == dropdownref.current){
                setDropdown(!dropdown)
            }
            if(dropdown){
                if(!navref.current.contains(e.target)){
                    setDropdown(false)
                }
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
                <div className={NavBarS.dropdownmenu_cont}>
                    <img className={NavBarS.dropdownimg}  src="src\assets\dropdown.svg" ref={dropdownref}/>
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