import "./TrackList.css";
import Track from "../Track/Track";

function TrackList(props) {
  return (
    <div className="TrackList">
      {props.tracks.map((track) => (
        <Track
          key={track.id}
          track={track}
          onAdd={this.onAdd}
          onRemove={this.onRemove}
          isRemoval={this.isRemoval}
        />
      ))}
    </div>
  );
}

export default TrackList;
