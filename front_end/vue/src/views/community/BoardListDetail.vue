<template>
  <div>
    <h1 style="margin-top:50px">게시글 상세보기</h1>
    <div class="card text-black bg-white mb-3" style="max-width: 150rem; margin-left:300px; margin-right:300px; margin-top:50px;">
      <h3 class="card-header"> {{ boardDetail.title }}</h3>
      <div class="card-body">
        <p class="card-title"> {{ boardDetail.created_at }}</p>
        <p class="card-text comment-card1" > 작성자 : {{ boardDetail.username }} </p>
        <p class="card-text comment-card1" > 내용 : 
          <br>{{ boardDetail.content }} </p>
          <section class="mb-5" style="margin-top:150px">
              <div class="card bg-light">
                  <div class="card-body">
                      <form class="mb-4"><textarea class="form-control" rows="3" placeholder="댓글을 입력후 enter을 눌러주세요." v-model="comment_content" @keypress.enter="createComment" ></textarea></form>
                      <div class="d-flex mb-4">
                        <div v-for="(comment, idx) in comments" :key="idx">
                          <div class="flex-shrink-0"><img class="rounded-circle" src="https://dummyimage.com/50x50/ced4da/6c757d.jpg" alt="..." /></div>
                          <div class="ms-3">
                              <div class="fw-bold">익명의 사용자</div>
                               {{comment.content}} 
                          </div>
                      </div>
                  </div>
              </div>
            </div>
          </section>
        <button @click="deleteBoard">delete</button>
      </div>
    </div>
  </div>
  
</template>
<script>
import axios from 'axios'


export default {
  name: 'BoardListDetail',
  data() {
    return {
      boardDetail: [],
      boardId: this.$route.params.boardId,
      comment_content: '',
      comments: [Array, Object],
      user: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getBoardDetail: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.boardId}/`,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)
          this.boardDetail = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },

    getComments: function () { //댓글 가져오기
      const config = this.getToken()
      axios.get(`http://127.0.0.1:8000/community/${this.boardId}/board_comment_list_or_create/`, config)
        .then((res) => {
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createComment: function () { //댓글생성
      const config = this.getToken()
      const commentItem = {
        content: this.comment_content,
      }
      if (commentItem.content) {
          axios.post(`http://127.0.0.1:8000/community/${this.boardId}/board_comment_list_or_create/`, commentItem, config)
          .then( () => {
            this.getComments()
            this.comment_content = ''
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
    deleteBoard: function () {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/${this.boardId}/`,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)
          this.boardDetail = res.data
          alert('게시글이 삭제되었습니다.')
        })
        .catch(err => {
          console.log(err)
          alert('게시글 삭제가 실패했습니다.')
        })
    },
    updateBoard: function () {
      const config = this.setToken()
      axios.put(`http://127.0.0.1:8000/community/`, this.board1, config)
        .then(() => {
          this.BoardListDetail(this.boards[this.boards.length -1].id)
        })
        .catch((err) => {
          console.log('게시글 수정에 실패하였습니다.')
          console.log(err)
          
        })
      },
  },
  computed: {
    commentsList: function () {
      // console.log('댓글입니다')
      // console.log(this.comments)
      return this.comments
    }
  },
  created: function () {
    this.getBoardDetail()
    this.getComments()
  }
}


</script>

<style>


	.tbAdd{border-top:1px solid #888;}
	.tbAdd th, .tbAdd td{border-bottom:1px solid #eee; padding:5px 0; }
	.tbAdd td{padding:10px 10px; box-sizing:border-box; text-align:left;}
	.tbAdd td.txt_cont{height:300px; vertical-align:top;}
	.btnWrap{text-align:center; margin:20px 0 0 0;}
	.btnWrap a{margin:0 10px;}
	.btnAdd {background:#43b984}
	.btnDelete{background:#f00;}


</style>