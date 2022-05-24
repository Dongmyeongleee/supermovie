<template>
  <div>
    <div class="modal"  id="exampleModal_1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel"> 팔로잉 </h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <span v-for="follower in followers" :key="follower.title"> 
              <div>
              {{ follower.username }}
              </div>
            </span>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal" id="exampleModal_2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel"> 팔로워 </h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <span v-for="following in followings" :key="following.title"> 
              <div>
              {{ following.username }}
              </div>
            </span>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal" id="exampleModal_3" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel"> 좋아요 누른 영화 </h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <span v-for="likes in like" :key="likes.title"> 
              <div>
              {{ likes.title }}
              </div>
            </span>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    <div class="container mt-4 mb-4 p-3 d-flex justify-content-center">
    <div class="card p-4">
        <div class=" image d-flex flex-column justify-content-center align-items-center"> <button class="btn btn-secondary"> <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAeFBMVEX///8AAAD5+fn29vbz8/Pm5ua7u7u3t7efn5+JiYmbm5t0dHSUlJTU1NSkpKQ9PT3Nzc3ExMQYGBgQEBBqamrp6elISEiwsLAhISE4ODiCgoJ7e3vd3d1wcHBdXV1DQ0MvLy9VVVUsLCxiYmIlJSVOTk4TExNXV1f1Y3UPAAAFoUlEQVR4nO2d2XbaQAyG4wWXsIXdkJAU0iZ5/zcsrktjB9uZRbL+4ei74nL+Mx6NthF3d4qiKIqiKIqiKIqiKObEg3w03u6igt12PMoHsfSSCIkPk5fompfJ4TZUTh+PDfJKjuOp9PK8yfet8v6JnEkv0Ydk+I28klEivVBX8qWRwChahbmP0wdDfQX7AM/jo4W+gifpBVtyaLefbfw+SC/ahsxaX8EP6WWbM3ISGEX30gs3ZewoMIrW0ks349lZYCAS3XcwEIm2t8RXxtICvmPmKfDsw0lL6GbuLTCKFtIiukjfCRRGG2kZHXxQCIy20jLa8T+EJbBHMSUSiPudrskUvkhLaYbCjl7AtKcnQoU/pcU0QbmFmJtIc1NcANzEA6nAKMJL3Ph63F95lhZ0BbHAKEJLoi7IFaJlbXwC+2bAbv34lVzhLpUWVYPakhZgWVOqqKLKRFpUDb/0UzO/pEXVsKnCmLJDqhAnDAKjCMnUDFgUIpka+vu+AOnOz1kUDqVlVTCr19uCdF24ltO6QSq2TVgUPkrLqsCjEKm0z6MQ6SvlOYdIlobD8cZK7v9gUYjUKTVlUYiUM6WryVRBqs/Epj16VkBl25p6gH3BKpTeMyhEuvB5wiek4OnubsOgcCAtqs4buUC06hN9hIjksxXQZ2qQsjR/+Uks8Cgt6Aq3tuB2cmlB1xArREoH/4M2CkaKfi8kK0qFSPnu/1AG+ohbeA4wdmQCV5BbSBnpAxrSkhORQDSH7RMq/xvM565CU6FBykBd8UQgEK8bqoZ/uXsP6M1USb3vfaQMWyO+nTVwQdM1ftnhufTyTfCRGITA84fqfBYD+ERLUjeLuoc3MhVc7kXwe/Ar9t4NrLfdxuZkpW8L7Iu2kpkXpN6xMvjGxCOz54irCbij1kEyNLg4RqABvSnZtlPeNtDvs8ZmdmreydXbLET70shmPlnXZ4Ec15N5SBe8CXE6WOSz4Wg4yxeDNFzboiiKoiiKogROfCbZDNKk+CG9GFLSwXx2Pz7tq0mN5f40vp/NB4EHv2em+fjtd0cAvHwb58Gkga84DLeGeZrtMDyVSWabE37OoNq6u0kyt2lD6yyMY3l4dO+rWT7hf66Z/WjWOkfo5Fs6onh38Q6bQE3puhMnkBppn1zgte7Rv+bGqrYtvpst78Ie5+1ayjH3o+AZ5DjyjBsoQfhUU45na598iG9jRtrd3UQmK5B6SlsTkq/0NhyDd66R67OhnQXZhVAzGM8j/GZE2ob7OIKfCEwBoRupa0bf4+hj2mmlJpx6zUDG/RjROg89Soypn1OiSUxkBJ4l9pWOkxLY23OhX2ICe5qlyBUMmtHDH3zwjIQyh/2ZPvWTbXuYoymOWbO2sP63V8oyaceSJWfY37cz2gyjQeUZAGkP21BMhENYwnUUfctKdLzyCOSYBeUKS1mDZ+qcKxyVVI7ShDt7eoEodvQCuT3lmRvoA/W9j3HXVyF+rohlZkpojc1JWk4DH5QCeWau+0KZ6+9+fyYF4XDM/kowdtBtolxyrRuy1BuiIS2hMqeS6cNuiMo1PH/PQQPNG1Tp/GEXJLlFhj+rouOVoliDedtfoOgMw/O5qxDYmlhawzf4f6Y8fwpAh3/TNG/bmj/efyKIF9t/xTfWx7akBb7WVLYeaoJvYx9WDrEJz7wisk96wc835exwpsKvU5piWic3fgdRorvLFq9In+e/Kanx6ZRCTUHV8UlI9dkG7I5PA3G/fcCu+PQP49/3BQ8eCqXXbogqbAenvaQb9+YT/NCpxD2AQs9gXHDPZITgdxe4+97I2e4q7plv/AC/xL01GjsZ/Il7Wvj29zAMx9vH9b79Gz+IEN/P8779CDiIG9GzDozUGNyMd7uwxex4CZYET2jibM0+N8GR1Tq7reF9iqIoiqIoiqIoiqK08we7LGaJQSXemgAAAABJRU5ErkJggg==" height="100" width="100" /></button> <span class="name mt-3"> {{ user.username }}</span> <span class="idd">님 환영합니다!</span>
            <div class="d-flex flex-row justify-content-center align-items-center mt-3 "> <span class="number" data-bs-toggle="modal" data-bs-target="#exampleModal_1"> {{ followers.length }} <span class="follow">Followers</span></span> </div>
            <div class="d-flex flex-row justify-content-center align-items-center mt-3"> <span class="number" data-bs-toggle="modal" data-bs-target="#exampleModal_2"> {{ follwings.length }} <span class="follow">Followings</span></span> </div>
            <div class="d-flex flex-row justify-content-center align-items-center mt-3"> <span class="number" data-bs-toggle="modal" data-bs-target="#exampleModal_3"> {{ like.length }} <span class="follow">좋아요 누른 영화</span></span> </div>
            <div class="text mt-3"> <span>Welcome to Movie Dream. Please enjoy your time <br><br> Movie Dream에 오신걸 환영합니다!! </span> </div>
            <div class="gap-3 mt-3 icons d-flex flex-row justify-content-center align-items-center"> <span><i class="fa fa-twitter"></i></span> <span><i class="fa fa-facebook-f"></i></span> <span><i class="fa fa-instagram"></i></span> <span><i class="fa fa-linkedin"></i></span> </div>
            <div class=" px-2 rounded mt-4 date "> <span class="join">Joined May,2021</span> </div>
        </div>
    </div>
</div>
    <!-- <h1>profile</h1>
    <h5>이름: {{ user.username }}</h5>
    <h5>좋아요한 영화:<span v-for="id in like" :key="id" class="mr-2 p-1 mb-1">{{ id.title }},</span></h5>
    <h5>팔로우중인사람: {{ followers }}</h5>
    <h5>팔로잉한사람: {{ follwings }}</h5> -->

    <!-- Scrollable modal -->
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from 'vue-jwt-decode'

export default {
  name: "Profile",
  data: function () {
    return {
      user: '',
      like: [],
      userrank: [],
      followers: [],
      follwings: [],
      movie: []   
    }
  },
  methods:{
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization:`JWT ${token}`
        }
      }
      return config
    },

    getUser() {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post('http://127.0.0.1:8000/accounts/profile/', info, config)
      .then( (res) => {
        console.log(res)
        this.user = res.data
        this.like = res.data.like_movies
        this.userrank = res.data.user_rank
        this.follwings = res.data.followings
        this.followers = res.data.followers
      })

    },

  },
  created() {
    this.getUser()

    

  }
}
</script>

<style>

</style>