<template>
  <div>
    <form action="">
    <div class="form-group">
      <label for="title">제목</label>
      <input type="text" v-model.trim="board.title" class="form-control" id="title" placeholder="제목을 입력해주세요">
    </div>
    <div class="form-group">
      <label for="content">내용</label>
      <input type="text" v-model.trim="board.content" class="form-control" id="content" placeholder="내용을 입력해주세요">
    </div>
    <button class="btn btn-primary" @click="createBoard" style="margin:5px">작성하기</button>
    <button class="btn btn-primary" @click="backList" style="margin:5px">뒤로가기</button>
  </form>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'BoardCreate',
  data: function() {
    return {
      board:{
        title: '',
        content: '',
      }
    }
  },
  methods: {

    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    backList(){
      this.$router.push({ name:'BoardList' })
    },
    createBoard: function () {
      const config = this.getToken()
      axios.post(`http://127.0.0.1:8000/community/`, this.board, config)
        .then(() => {
          this.$router.push({ name:'BoardList' })
        })
        .catch((err) => {
          console.log('게시글 작성에 실패하였습니다.')
          console.log(err)
          
        })
        }
    }
  }
</script>
  

