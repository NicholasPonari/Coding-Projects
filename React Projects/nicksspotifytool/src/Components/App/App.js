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
    this.addTrack = this.addTrack.bind(this);
    this.removeTrack = this.removeTrack.bind(this);
    this.playlistName = this.playlistName.bind(this);
    this.savePlaylist = this.savePlaylist.bind(this);
    this.search = this.search.bind(this);
  }

  addTrack(track) {
    if (
      this.state.playlistTracks.find((savedTrack) => savedTrack.id === track.id)
    ) {
      return;
    }
    this.setState({ playlistTracks: [...this.state.playlistTracks, track] });
  }

  removeTrack(track) {
    this.setState({
      playlistTracks: this.state.playlistTracks.filter(
        (currentTrack) => currentTrack.id !== track.id
      ),
    });
  }

  savePlaylist() {
    const trackURIs = this.state.playlistTracks.map((track) => track.uri);
  }

  search(searchTerm) {
    console.log(searchTerm);
  }

  render() {
    return (
      <div>
        <h1>
          Nick's<span className="highlight"> Awesome </span>
          <span className="highlight-green">Spotify </span>Tool
        </h1>
        <div className="App">
          <SearchBar onSearch={this.search} />
          <div className="App-playlist">
            <SearchResults
              searchResults={this.state.searchResults}
              onAdd={this.addTrack}
            />
            <Playlist
              onRemove={this.removeTrack}
              playlistName={this.state.playlistName}
              playlistTracks={this.state.playlistTracks}
              onSave={this.savePlaylist}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default App;
