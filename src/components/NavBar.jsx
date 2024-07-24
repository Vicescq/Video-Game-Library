import NavBarS from "./NavBar.module.css"

function NavBar(){
    return(

        <nav>
            <div className={NavBarS.container}>
                <img src="src\assets\controller.svg"/>
                <div className={NavBarS.title}>Library</div>
            </div>
            <div className={NavBarS.container}>
                <div className={NavBarS.dropdownmenu_cont}>
                    <img className={NavBarS.dropdownimg}  src="src\assets\dropdown.svg"/>
                    <ul className={NavBarS.dropdownmenu}>
                        <li>dakdsakldsajlk</li>
                        <li>dakdsakldsajlk</li>
                        <li>dakdsakldsajlk</li>
                    </ul>
                </div>
            </div>
        </nav>

    )
}

export default NavBar