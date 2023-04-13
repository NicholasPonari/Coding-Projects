import "./Playlist.css";
import TrackList from "../TrackList/TrackList";

function Playlist(props) {
  return (
    <div className="Playlist">
      <input value="New Playlist" />
      <TrackList
        tracks={props.playlistTracks}
        onRemove={props.removeTrack}
        isRemoval={true}
        onChange={props.handleNameChange}
      />
      <button className="Playlist-save" onClick={this.props.onSave}>
        SAVE TO SPOTIFY
      </button>
    </div>
  );
}

export default Playlist;
