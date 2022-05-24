<template>
  <div>
    <h1 style="margin-top:50px">자유 게시판</h1>
    <header>
      <div>
        <div class="container" style="width:80%">
          <div align="right" style="margin-right:50px">
            <button type="button" class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">게시글 작성</button>
          </div>
          <br>
          <table class="table mb-5" v-if="boards">
            <thead>
              <tr>
                <th scope="col">게시글 번호</th>
                <th scope="col">제목</th>
                <th scope="col">작성자</th>
                <th scope="col">자세히</th>
              </tr>
            </thead>
            <tbody> 
              <tr v-for="board in paginatedData" :key="`board_${board.id}`">
                <td class="table-id"> {{ board.id }} </td>
                <td class="table-title"> {{ board.title }} </td>
                <td class="table-id"> {{ board.username }} </td>
                <td @click="BoardListDetail(board.id)"> Detail </td>
              </tr>
            </tbody>
          </table>
          <div class="btn-cover" v-if="paginatedData">
            <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">이전</button>
            <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
            <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">다음</button>
          </div>
          <div v-else class="mt-5 text-center">
            <h3> 게시글를 작성해주세요. </h3>
          </div>
        </div>
      </div>
    </header>
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">게시글 작성</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">제목:</label>
            <input type="text" v-model.trim="board1.title" placeholder="제목을 입력해주세요">
          </div>
          <div class="mb-3">
            <label for="message-text" class="col-form-label">내용:</label>
            <textarea type="text" class="form-control" v-model.trim="board1.content" id="message-text"></textarea>
          </div>
        </form>
      </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="createBoard" data-bs-dismiss="modal">Post</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'BoardList',
  data: function () {
    return {
      boards: [],
      board1:{
      title: '',
      content: '',
      },
      pageNum: 0,
      pageSize: 10,
    }
  },
  mounted() {
    if (localStorage.getItem('jwt')) {
      this.getBoards()
    } else {
      this.$router.push({name: 'Login'})
      }
    },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers:{
          Authorization: `JWT ${token}`
        }
      }
      return config
    },

    BoardListDetail(board_id){
      this.$router.push({ name: 'BoardListDetail', params: {boardId:board_id}})
    },
    getBoards: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/',
        headers: this.getToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)
          this.boards = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    createBoard: function () {
      const config = this.setToken()
      axios.post(`http://127.0.0.1:8000/community/`, this.board1, config)
        .then(() => {
          this.BoardListDetail(this.boards[this.boards.length -1].id)
        })
        .catch((err) => {
          console.log('게시글 작성에 실패하였습니다.')
          console.log(err)
          
        })
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
      let listLeng = this.boards.length,
      listSize = this.pageSize,
      page = Math.floor(listLeng/listSize);

      if (listLeng % listSize > 0) page += 1;
      return page;
    },
    paginatedData() {
      if (this.boards.length >= 1){
        const start = this.pageNum * this.pageSize,
        end = start + this.pageSize;
        return this.boards.slice(start, end);
      } else {
        return 0
      }
    }
  },
  created: function () {
  this.getBoardDetail()
  this.getComments()
  }
}
</script>

<style scoped>
  .table-id {
    text-align: center;
    max-width: 1rem;
  }
  .table-title {
    max-width: 3rem;
  }
  .board-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }


header h1{position:absolute; top:0; left:100px;}
header ul.menu:after{display:block; clear:both; content:'';}
header ul.menu{position:absolute; top:20px; right:50px;}
header ul.menu li{float:left; padding:10px 20px; list-style:none;}

.pagination{
  justify-content: center;
  justify-items: center;
}


.table-hovor{
  display: block;
  margin: 10%;
  padding: 5%;
  width: 400px;
  max-width: 100%;
  height: auto !important;
  border: 2px solid black;

}

</style>