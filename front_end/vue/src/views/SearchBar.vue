<template>
 <div class="card col d-flex justify-content-center align-items-center" style=" border: 1px solid rgb(78, 51, 62); background-color: rgba(0, 0, 0, 0.3);">
     <h2>검색어 : {{ keyword }}</h2>
     <!-- 자료가 없을 때-->
    <div v-if="result.length === 0">
    <h1> 검색 결과가 존재하지 않습니다.</h1>
    </div>

    <div v-else>
      <div class="card m-5 d-flex justify-content-center align-items-center" style=" width:1000px; border: 1px solid rgb(78, 51, 62); background-color: rgba(0, 0, 0, 0.6);">
        <div>
          <h2 style="font-weight: bold;">영화제목: {{ result[0].title }} </h2>
          <hr>
            <img :src="movieImage" alt="poster_path" style="width:30%" class="m-2" >
            
        </div>
      </div>
    </div>
 </div>
</template>

<script>
import axios from "axios"

export default {
  name: 'SearchBar',

  data: function () {
    return {
      keyword: '',
      movies: [],
      result: [],
      src: '',
      videoId: '',
    
    }
  },
  methods: {

    getMovies: function () {
      axios.get(`http://127.0.0.1:8000/movies/`)
        .then((res) => {
          this.movies = res.data
          for(var i=0; i<this.movies.length; i++) {
            if (this.keyword === this.movies[i].title) {
              this.result.push(this.movies[i])
            }
          }
        })
    },   
  },
  
  computed:{
       movieImage: function () {
           return `https://image.tmdb.org/t/p/w500/${this.result[0].poster_path}`
    }
  },

  created: function () {
    this.keyword = this.$route.query.keyword 
    this.getMovies()
  }
}
</script>

<style>

</style>