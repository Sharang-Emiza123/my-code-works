import React from "react";
import { useEffect, useState } from "react";

import './App.css';
import MovieCard from "./MovieCard";
import SearchIcon from './search.svg'

//API_KEY check WhatsApp

const API_URL = 'http://www.omdbapi.com/?apikey='



const App = () => {

    const [movies, setMovies] = useState([])    
    const [searchTerm, setSearchTerm] = useState('')

    const searchMovies = async (title) => {
        const response = await fetch(`${API_URL}&s=${title}`)
        const data = await response.json()
        
        setMovies(data.Search);
    }

    // useEffect(() => {
    //     searchMovies('Shawshank Redemption')
    // },[])

    return(
        <div className="app">
            <h1>MovieLand</h1>

            <div className="search">
                <input
                    placeholder="Search for Movies"
                    value={searchTerm}
                    onChange={(w) => {setSearchTerm(w.target.value)}}
                />
                <img
                    src={SearchIcon}
                    alt="search"
                    onClick={() => {searchMovies(searchTerm)}}
                />
            </div>
            {
            movies.length > 0 
                ? (
                    <div className="container">
                        {movies.map((movie) => (
                            <MovieCard movie = {movie}/>
                        ))}
                    </div>
                ) :
                (
                    <div className="empty">
                        <h2>No movies found</h2>
                    </div>
                )
            }
        </div>
    );
}

export default App;
