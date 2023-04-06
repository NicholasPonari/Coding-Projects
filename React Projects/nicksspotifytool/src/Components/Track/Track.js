import "./Track.css";

function Track({ isRemoval }) {
  const renderAction = () => {
    return isRemoval ? (
      <button className="Track-action">-</button>
    ) : (
      <button className="Track-action">+</button>
    );
  };

  return (
    <div className="Track">
      <div className="Track-information">
        <h3>{this.props.track.name}</h3>
        <p>
          {this.props.track.artist} | {this.props.track.album}
        </p>
      </div>
      {renderAction()}
    </div>
  );
}

export default Track;
