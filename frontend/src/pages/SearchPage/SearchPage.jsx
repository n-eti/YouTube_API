import axios from "axios";
import React, { useState } from "react";
import SearchBar from "../../components/SearchBar/SearchBar";
import VideoDisplay from "../../components/VideoDisplay/VideoDisplay";

const SearchPage = ({}) => {
  const [videos, setVideos] = useState([]);

  let videoThumbs = videos.map((video) => <VideoDisplay data={video
  }/>) 

  async function fetchSearchResults(searchTerm) {
    let response = await axios.get(
      `https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q=${searchTerm}&type=video&key=AIzaSyACDkhVL41ty7K077xwrNiTYj6KKsdizoQ`
    );
    setVideos(response.data.items);
    
  }
  return (
    <div>
      <SearchBar placeholder="Enter video name" onSubmit={fetchSearchResults} />
      {videoThumbs}
    </div>
  );
};

export default SearchPage;
