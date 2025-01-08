import './App.css'
import {useEffect} from "react";
import axios from "axios";

function App() {


    useEffect(() => {
        axios.get("http://localhost:5091/api/categories")
            .then(resp => {
                console.log("Результат асинхрого методу на сервер", resp);
            });
        console.log("Use Effect");
    }, []);

    console.log("Render component");

    return (
        <>
            <h1 className="text-3xl font-bold underline text-center">
                Hello world!
            </h1>
        </>
    )
}

export default App
