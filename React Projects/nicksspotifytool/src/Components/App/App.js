import React from "react";
import "./App.css";
import SearchBar from "../SearchBar/SearchBar";
import SearchResults from "../SearchResults/SearchResults";
import Playlist from "../Playlist/Playlist";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      searchResults: [
        { name: "name1", artist: "artist1", album: "album1", id: 1 },
      ],
      playlistName: "My Playlist",
      playlistTracks: [
        { name: "name1", artist: "artist1", album: "album1", id: 1 },
      ],
    };
  }

  addTrack = (track) => {
    this.state.playlistTracks.push(track);
  };

  render() {
    return (
      <div>
        <h1>
          Nick's<span className="highlight"> Awesome </span>
          <span className="highlight-green">Spotify </span>Tool
        </h1>
        <div className="App">
          <SearchBar />
          <div className="App-playlist">
            <SearchResults searchResults={this.state.searchResults} />
            <Playlist
              playlistName={this.state.playlistName}
              playlistTracks={this.state.playlistTracks}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default App;
