import axios from "axios";
import React, { useState } from "react";

const SearchPage = ({}) => {
    const [videos, setVideos] = useState([]);

  async function fetchSearchResults(searchTerm) {
    let response = await axios.get(
      `https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q=${searchTerm}&type=video&key=AIzaSyACDkhVL41ty7K077xwrNiTYj6KKsdizoQ`
    );
    setVideos(response.data.items)
    console.log(response.data.items)
      }
  return (
    <div>
      <h3>search bar to come</h3>
      
    </div>
  );
};

export default SearchPage;
