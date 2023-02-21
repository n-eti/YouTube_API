const VideoPlayer = ({ videoId }) => {
  return (
    <div>
      <iframe
        id="ytplayer"
        type="text/html"
        width="640"
        height="360"
        src={`/video/${videoId}`}
        frameborder="0"
      ></iframe>
    </div>
  );
};

export default VideoPlayer;
