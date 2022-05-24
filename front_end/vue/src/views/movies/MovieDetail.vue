<template>
 <div> 
  <section class="section about-section gray-bg" id="about">
    <div class="container">
          <div class="row align-items-center flex-row-reverse">
              <div class="col-lg-6">
                  <div class="about-text go-to">
                      <h3 class="dark-color">{{ movie.title }}</h3>
                      <h6>{{ movie.overview }}</h6>

                      <div class="row about-list">
                          <div class="col-md-6">
                              <div class="media">
                                  <label>개봉일</label>
                                  <p>{{ movie.release_date }}</p>
                              </div>

                              <div class="media">
                                <label>좋아요</label>
                                  <div class="d-inline-block heart-container ml-3">
                                    <i class="heart fas fa-heart fa-3x" v-show="like" @click="changeLike" style="color: tomato;" data-toggle="tooltip" data-placement="top">

                                    </i> 
                                  </div>
                                  <div class="d-inline-block heart-container ml-3">
                                  <i class="heart far fa-heart fa-3x" v-show="!like" @click="changeLike" style="color: grey;" data-toggle="tooltip" data-placement="top">

                                    </i>
                                  </div>
                              </div>
                          </div>
                          <div class="col-md-6">
                              <div class="media">
                                  <label>장르</label>
                                  <p>
                                    <span v-for="genre in movie.genres" :key="genre.genres" class="mr-2 p-1 mb-1">{{ get_genre(genre)}}</span>
                                  </p>
                              </div>
                              <div class="media">
                                  <label>평점</label>
                                  <p>{{ movie.vote_average }}</p>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
              <div class="col-lg-6">
                  <div class="about-avatar">
                    <img class="detail-poster" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"  alt="영화포스터">
                  </div>
              </div>
          </div>
      </div>
  </section>
        <div>
          <table class="table mb-5" v-if="reviews">
            <thead>
              <tr>
                <th scope="col">작성자</th>
                <th scope="col">내용</th>
                <th scope="col">점수</th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="review in paginatedData" :key="review.id" >
                <td data-label="Username">{{ review.userName }}</td>
                <td data-label="Title"> {{ review.content }}</td>
                <td data-label="Rating"><i class="fas fa-star" style="color: #345389"></i> {{ review.rank }}</td>
                <td width="200">
                  <button type="button" class="btn btn-outline-secondary" data-bs-toggle="modal" data-bs-target="#modifyModal" data-bs-whatever="@getbootstrap" @click="getReviewId(review.id)">수정</button>
                  &nbsp;&nbsp;
                  <button type="button" class="btn btn-outline-danger" @click="deleteReview(review.id)">삭제</button>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="btn-cover" v-if="paginatedData">
            <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">이전</button>
            <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
            <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">다음</button>
          </div>
          <div v-else class="mt-5 text-center">
            <h3> 리뷰를 작성해주세요! </h3>
          </div>
          <div align="right" style="margin-right:50px">
            <button type="button" class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#createModal" data-bs-whatever="@getbootstrap">리뷰 작성</button>
          </div>
          <div style="padding:10px;">
          </div>
          <div class="modal fade" id="createModal" tabindex="-1" aria-labelledby="createModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="createModalLabel">리뷰 작성</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <form>
                  <div class="mb-3">
                    <label for="message-text" class="col-form-label">내용:</label>
                    <textarea type="text" class="form-control" v-model.trim="review.content" id="message-text"></textarea>
                  </div>
                  <div class="mb-3">
                    <label for="review-rank" class="col-form-label">점수:</label>
                    <input type="number" min="0" max="10" step="1" id="review-rank" v-model.trim="review.rank"  >
                  </div>
                </form>
              </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" @click="createReview" data-bs-dismiss="modal">작성</button>
                  </div>
                </div>
              </div>
          </div>
          <div class="modal fade" id="modifyModal" tabindex="-1" aria-labelledby="modifyModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="modifyModalLabel">리뷰 수정</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <form>
                  <div class="mb-3">
                    <label for="message-text" class="col-form-label">내용:</label>
                    <textarea type="text" class="form-control" v-model.trim="review.content" id="message-text"></textarea>
                  </div>
                  <div class="mb-3">
                    <label for="review-rank" class="col-form-label">점수:</label>
                    <input type="number" min="0" max="10" step="1" id="review-rank" v-model.trim="review.rank"  >
                  </div>
                </form>
              </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  <button type="button" class="btn btn-primary" @click="updateReview()" data-bs-dismiss="modal">작성</button>
                </div>
              </div>
            </div>
          </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from 'vue-jwt-decode'

export default {
  name: "MovieDetail",
  data() {
    return {
      user : "",
      movie : "",
      movieId : this.$route.params.movieId,
      like : false,
      reviews : [],
      pageNum: 0,
      pageSize: 10,
      review_id : 0,
      review:{
        content:'',
        rank:'',

        // movie: this.$route.movieId,
        // user: this.user.id
      }

    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getReviewId(review_id) {
      this.review_id = review_id

    },
    
    getReviews() {
      const config = this.getToken()
      axios.get('http://127.0.0.1:8000/movies/' + this.$route.params.movieId +'/reviews/', config)
        .then(res => {
          console.log(res)
          this.reviews = res.data
        })
        .catch(err => console.error(err))
    },
    createReview: function () {
      const config = this.getToken()
      axios.post('http://127.0.0.1:8000/movies/'+ this.$route.params.movieId +'/reviews/create/' ,this.review, config)
        .then((res) => {
          console.log(res)
          this.$router.go(this.$router.currentRoute)
        })
        .catch((err) => {
          console.log(err)
          console.log('게시글 생성에 실패하였습니다.')
          
        })
    },
    deleteReview(review_id) {
      const config = this.getToken()
      axios.delete('http://127.0.0.1:8000/movies/'+ 'review/' + review_id + '/' , config)
        .then((res) => {
          console.log(res)
          alert('삭제되었습니다.')
          this.$router.go(this.$router.currentRoute)

        })
        .catch((err) => {
          console.log(err)
          alert('게시글 작성자만 삭제할 수 있습니다.')
          
        })
    },      
    updateReview() {
      const config = this.getToken()
      axios.put('http://127.0.0.1:8000/movies/'+ 'review/' + this.review_id + '/' ,this.review, config)
        .then((res) => {
          console.log(res)
          this.$router.go(this.$router.currentRoute)
        })
        .catch((err) => {
          console.log(err)
          alert('게시글 작성자만 수정할 수 있습니다.')
          
        })
    },
      

    getUser() {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post('http://127.0.0.1:8000/accounts/profile/', info, config)
      .then((res) => {
        this.user = res.data
        // console.log(res)
        this.checkLike()
      })
    },
    fetchMovies() {
      const config = this.getToken()
      axios.get('http://127.0.0.1:8000/movies/' + this.$route.params.movieId, config)
        .then(res => {
          console.log(res)
          this.movie = res.data
        })
        .catch(err => console.error(err))
    },
    checkLike() {
      const config = this.getToken()
      axios.get('http://127.0.0.1:8000/movies/' + this.$route.params.movieId +"/" + this.user.id + "/like/", config)
        .then( res => {
          this.like = res.data
          // console.log(res.data)
        })
      
    },
    changeLike() {
      const config = this.getToken()
      this.like = !this.like
      axios.get('http://127.0.0.1:8000/movies/' + this.$route.params.movieId +"/like/", config)
        .then( res => {
          console.log(res)

          })
        .catch( err => {
          console.log(err)
        })
    },
    get_genre(genre_id) {
      const genre_dict = {12: '모험',
        14: '판타지',
        16: '애니메이션',
        18: '드라마',
        27: '공포',
        28: '액션',
        35: '코미디',
        36: '역사',
        37: '서부',
        53: '스릴러',
        80: '범죄',
        99: '다큐멘터리',
        878: 'SF',
        9648: '미스터리',
        10402: '음악',
        10749: '로맨스',
        10751: '가족',
        10752: '전쟁',
        10770: 'TV 영화'}
      return genre_dict[genre_id]
    },
    nextPage() {
      this.pageNum += 1;
    },
    prevPage() {
      this.pageNum -= 1;
    }
  },
  computed: {
    pageCount() {
      let listLeng = this.reviews.length,
      listSize = this.pageSize,
      page = Math.floor(listLeng/listSize);

      if (listLeng % listSize > 0) page += 1;
      return page;
    },
    paginatedData() {
      if (this.reviews.length >= 1){
        const start = this.pageNum * this.pageSize,
        end = start + this.pageSize;
        return this.reviews.slice(start, end);
      } else {
        return 0
      }
    }
  },
  created() {
    this.fetchMovies()
    this.getUser()
    this.getReviews()
  }
}
</script>
<style>
body{
    color: #6F8BA4;
    margin-top:20px;
}
.section {
    padding: 100px 0;
    position: relative;
}
.gray-bg {
    background-color: #f5f5f5;
}

/* About Me 
---------------------*/
.about-text h3 {
  font-size: 45px;
  font-weight: 700;
  margin: 0 0 6px;
}
@media (max-width: 767px) {
  .about-text h3 {
    font-size: 35px;
  }
}
.about-text h6 {
  font-weight: 600;
  margin-bottom: 15px;
}
@media (max-width: 767px) {
  .about-text h6 {
    font-size: 18px;
  }
}
.about-text p {
  font-size: 18px;
  max-width: 450px;
}
.about-text p mark {
  font-weight: 600;
  color: #20247b;
}

.about-list {
  padding-top: 10px;
}
.about-list .media {
  padding: 5px 0;
}
.about-list label {
  color: #20247b;
  font-weight: 600;
  width: 88px;
  margin: 0;
  position: relative;
}
.about-list label:after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  right: 11px;
  width: 1px;
  height: 12px;
  background: #20247b;
  -moz-transform: rotate(15deg);
  -o-transform: rotate(15deg);
  -ms-transform: rotate(15deg);
  -webkit-transform: rotate(15deg);
  transform: rotate(15deg);
  margin: auto;
  opacity: 0.5;
}
.about-list p {
  margin: 0;
  font-size: 15px;
}

@media (max-width: 991px) {
  .about-avatar {
    margin-top: 30px;
  }
}

.about-section .counter {
  padding: 22px 20px;
  background: #ffffff;
  border-radius: 10px;
  box-shadow: 0 0 30px rgba(31, 45, 61, 0.125);
}
.about-section .counter .count-data {
  margin-top: 10px;
  margin-bottom: 10px;
}
.about-section .counter .count {
  font-weight: 700;
  color: #20247b;
  margin: 0 0 5px;
}
.about-section .counter p {
  font-weight: 600;
  margin: 0;
}
mark {
    background-image: linear-gradient(rgba(252, 83, 86, 0.6), rgba(252, 83, 86, 0.6));
    background-size: 100% 3px;
    background-repeat: no-repeat;
    background-position: 0 bottom;
    background-color: transparent;
    padding: 0;
    color: currentColor;
}
.theme-color {
    color: #fc5356;
}
.dark-color {
    color: #20247b;
}
.detail-poster{
  width: 300px;
  height: 400px;
}
</style>

