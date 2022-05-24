<template>
 <div class="card col d-flex justify-content-center align-items-center" style=" border: 1px solid rgb(78, 51, 62); background-color: rgba(0, 0, 0, 0.3);">
     <h2>검색어 : {{ keyword }}</h2>
     <!-- 자료가 없을 때-->
    <div v-if="result.length === 0">
    <h1>해당 영화에 대한 정보가 없습니다.</h1>
    </div>
    <div v-else>
      <div class="card m-5 d-flex justify-content-center align-items-center" style=" width:1000px; border: 1px solid rgb(78, 51, 62); background-color: rgba(0, 0, 0, 0.6);">
      <div>
        <h2 style="font-weight: bold;">영화제목: {{ result[0].title }} </h2>
        <hr>
          <img :src="movieImage" alt="poster_path" style="width:30%" class="m-2" >
        
        <div class="mt-4 d-flex align-items-center">
        <br>
          <div class="col">
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 28">장르 : 액션 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 12">장르 : 어드벤쳐 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 16">장르 : 애니메이션 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 35">장르 : 코미디 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 80">장르 : 범죄 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 99">장르 : 다큐멘터리 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 18">장르 : 드라마 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 10751">장르 : 가족 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 14">장르 : 판타지 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 36">장르 : 역사 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 27">장르 : 호러 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 10402">장르 : 음악 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 9648">장르 : 미스터리 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 10749">장르 : 로맨스 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 878">장르 : 공상과학 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 10770">장르 : TV result[0] </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 53">장르 : 스릴러 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 10752">장르 : 전쟁 </h5>
            <h5 style="margin-bottom:10px" class="content-font" v-if="result[0].genres[0] === 37">장르 : 서부 영화 </h5>
            
            <h5 style="margin-bottom:10px" class="content-font">평점 : {{ result[0].vote_average }}점</h5>
            <h5 style="margin-bottom:10px" class="content-font">상영 시간 : {{ result[0].runtime }}분</h5>
            <h5 style="margin-bottom:10px" class="content-font">개봉 일자 : {{ result[0].release_date }}</h5>
            <h5 class="m-4">{{ result[0].overview }}</h5>
          </div>
        </div>
      </div>      
    </div>     
  </div>
 </div>
</template>

<script>
import axios from "axios"
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'SearchBar',
  components: {
    // MovieCard,
    
  },
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
      axios.get(`${SERVER_URL}/movies/`)
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
          //  if(this.movie.poster_path!=null)
           return `https://image.tmdb.org/t/p/w500/${this.result[0].poster_path}`
           //https://image.tmdb.org/t/p/w500/를 붙여서 리턴
       },
    },
  created: function () {
    this.keyword = this.$route.query.keyword //검색창에서 받아옴
    this.getMovies()
   
   
}
}
</script>

<style>
</style>

