import "./TrackList.css";
import Track from "../Track/Track";

function TrackList(props) {
  return (
    <div className="TrackList">
      {props.tracks.map((track) => (
        <Track key={track.id} track={track} />
      ))}
    </div>
  );
}

export default TrackList;
